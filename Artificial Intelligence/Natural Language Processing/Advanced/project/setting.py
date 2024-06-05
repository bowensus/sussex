import csv
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# nltk.download("stopwords")
# nltk.download("punkt")
stop_words = set(stopwords.words("english"))


class Dataset:

    def __init__(self):
        # set file path
        self.training_file_path = "dataset/propaganda_train.tsv"
        self.validation_file_path = "dataset/propaganda_val.tsv"
        self.samples = []

    def get_file(self, path="training"):

        file_path = self.training_file_path
        if path != "training":
            file_path = self.validation_file_path

        with open(file_path, 'r', newline='', encoding="utf-8") as file:
            tsv_reader = csv.reader(file, delimiter='\t')

            # skip the first line, which is "label" and "sample"
            next(tsv_reader)

            for row in tsv_reader:
                self.samples.append((*row[1:], row[0]))

    def get_tokens(self):
        # transform string to tokens
        self.samples = [(word_tokenize(sent[0]), sent[1]) for sent in self.samples]

    def normalise(self, lemmatized=False):
        samples = self.samples[:]
        self.samples = []

        for tokens in samples:
            new_tokens = []
            token_add_running = False

            label = 0
            if tokens[1] != "not_propaganda":
                label = 1

            for w in tokens[0]:

                # The part between <BOS> and <EOS> is the content that needs to be tested.
                if w == "BOS":
                    token_add_running = True
                if w == "EOS":
                    token_add_running = False
                if token_add_running and w.isalpha() and w not in stop_words:
                    # improves the generalization ability of the model
                    if lemmatized == True:
                        lemmatizer = WordNetLemmatizer()
                        w = lemmatizer.lemmatize(w, pos='v')
                    new_tokens.append(w)
            new_tokens.append("EOS")

            self.samples.append((new_tokens, label))

    def get_rate(self):
        propag = 0
        non = 0
        for sent in self.samples:
            if sent[1] == 0:
                non += 1
            else:
                propag += 1
        return propag, non

    def pre_processing(self, data):
        words = []
        for tokens in data:
            for w in tokens[0]:
                if w != "BOS" and w != "EOS" and w not in words:
                    words.append(w)

        words_to_idx = {}
        words_to_idx = {w: i + 3 for i, w in enumerate(words)}
        words_to_idx["BOS"] = 1
        words_to_idx["EOS"] = 2

        idx_data = []
        for sent, label in data:
            idx_sent = []
            for w in sent:
                idx_sent.append(words_to_idx[w])
            idx_data.append(idx_sent)

        return idx_data

    def get_label(self, data):
        labels = []
        for tokens in data:
            labels.append(tokens[1])
        return labels

    def get_words_num(self, data):
        words = []
        for tokens in data:
            for w in tokens[0]:
                if w != "BOS" and w != "EOS" and w not in words:
                    words.append(w)
        return len(words) + 2

    def get_sentence(self, data):
        sentences = []
        for sent in data:
            sentence = ' '.join(sent[0])
            sentences.append(sentence)
        return sentences

    def print_samples(self, n):
        if n <= len(self.samples):
            print(self.samples[:n])
        else:
            print(self.samples)




