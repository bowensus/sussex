import os
import random
import math
from nltk.tokenize import word_tokenize
import operator

training_dir = "../nlp/sentence-completion/Holmes_Training_Data"
random_seed = 35

def get_training_testing(training_dir, split):
    filenames = os.listdir(training_dir)
    n = len(filenames)
    print("There are {} files in the training directory: {}".format(n,training_dir))
    random.seed(random_seed)
    random.shuffle(filenames)
    index = int(n * split)
    return (filenames[:index], filenames[index:])

training_files, heldout_files = get_training_testing(training_dir, 0.5)


class Language_Model():

    def __init__(self, training_dir, files):
        self.training_dir = training_dir
        self.files = files
        self.unigram = {}
        self.bigram = {}
        self.train()

    def train(self):
        self.process_files()
        self.make_unknowns()
        self.convert_to_probs()

    def process_line(self, line):
        tokens = ["__START"] + word_tokenize(line) + ["__END"]
        previous = "__END"
        for token in tokens:
            self.unigram[token] = self.unigram.get(token, 0) + 1

            current = self.bigram.get(previous, {})
            current[token] = current.get(token, 0) + 1
            self.bigram[previous] = current
            # eg: I want to go to the shop to buy a book.
            # self.bigram[to] = {go:1, the:1, buy:1}
            previous = token

    def process_files(self):
        for afile in self.files:
            try:
                # concatenate address value and file name to generate directory name
                with open(os.path.join(self.training_dir, afile)) as instream:
                    for line in instream:
                        line = line.rstrip()
                        if len(line) > 0:
                            self.process_line(line)
            except UnicodeDecodeError:
                pass

    def convert_to_probs(self):
        self.unigram = {k: v / sum(self.unigram.values()) for (k, v) in self.unigram.items()}

        # eg: I want to go to the shop to buy a book.
        # self.bigram = {to:{go:0.33, the:0.33, buy:0.33}, ..., }
        self.bigram = {key: {k: v / sum(all_next.values()) for (k, v) in all_next.items()} for (key, all_next) in
                       (self.bigram.items())}

    def get_prob(self, token, context='', method="unigram"):
        if method == "unigram":
            return self.unigram.get(token, 0)
        elif method == "bigram":
            # eg: token == "go", context == ["I", "want", "to"], context[-1] == "to"
            return self.bigram.get(context[-1], {}).get(token, 0)
        else:
            print("Not Implement")
            return 0

    def nextlikely(self, current='', method="unigram"):
        blacklist = ["__START"]

        if method == "unigram":
            dist = self.unigram
        elif method == "bigram":
            dist = self.bigram.get(current, {})

        mostlikely = list(dist.items())
        filtered = [(w, p) for (w, p) in mostlikely if w not in blacklist]
        words, probdist = zip(*filtered)
        res = random.choices(words, probdist)[0]
        return res

    def generate(self, k=1, end="__END", limit=20, method="unigram"):
        current = "__START"
        tokens = []
        while current != end and len(tokens) < limit:
            current = self.nextlikely(current=current, method=method)
            tokens.append(current)
        return " ".join(tokens[:-1])

    def compute_prob_line(self, line, method="unigram"):
        tokens = ["__START"] + word_tokenize(line) + ["__END"]
        acc = 0
        for i, token in enumerate(tokens[1:]):
            # the prob of this sentence : acc
            # tokens = ["__START", "I", "want", "to", "go", ..., "__END"]
            # eg: i=0, token="I"
            #     i=1, token="want"
            #     i=2, token="to"
            #     i=3, token="go"
            #     token="go", i=3, tokens[:4]=["__START", "I", "want", "to"]
            acc += math.log(self.get_prob(token, tokens[:i + 1], method))
        return acc, len(tokens[1:])

    def compute_probability(self, filenames=[], method="unigram"):

        if filenames == []:
            filenames = self.files

        total_p = 0
        total_n = 0

        for i, afile in enumerate(filenames):
            print("Processing file {}: {}".format(i, afile))
            try:
                with open(os.path.join(self.training_dir, afile)) as instream:
                    for line in instream:
                        line = line.rstrip()
                        if len(line) > 0:
                            p, n = self.compute_prob_line(line, method=method)
                            total_p += p
                            total_n += n
            except UnicodeDecodeError:
                pass
        return total_p, total_n

    def compute_preplexity(self, filenames=[], method="unigram"):
        p, n = self.compute_probability(filenames=filenames, method=method)
        pp = math.exp(-p / n)
        return pp

    def make_unknowns(self, known=2):
        unknown = 0
        for (k, v) in list(self.unigram.items()):
            if v < known:
                # if the times < known, it would be regard as unknown, and add them into unknown
                del self.unigram[k]
                self.unigram["__UNKNOWN"] = self.unigram.get("__UNKNOWN", 0) + v
        for (key, all_next) in list(self.bigram.items()):
            for (k, v) in list(all_next.items()):
                isknown = self.unigram.get(k, 0)
                if isknown == 0:
                    all_next["__UNKNOWN"] = all_next.get("__UNKNOWN", 0) + v
                    # equal to directly replace k with "__UNKNOWN"
                    del all_next[k]
            isknown = self.unigram.get(k, 0)
            if isknown == 0:
                del self.bigram[key]
                current = self.bigram.get("__UNKNOWN", {}) + v
                current.update(all_next)
                # if key is unknown word, replace its key , keep dict value
                self.bigram["__UNKNOWN"] = current
            else:
                self.bigram[key] = all_next
                
                
max_files = 5
model = Language_Model(training_dir, training_files[:max_files])
model.generate(method="bigram")
