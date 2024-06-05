from setting import Dataset
import math
import random


class Bigram:

    def __init__(self, path="training"):
        self.dataset = Dataset()
        self.dataset.get_file(path)
        self.dataset.get_tokens()
        self.dataset.normalise()
        self.bigram = []
        self.propag_features = []
        self.non_features = []
        self.rate = self.dataset.get_rate()
        self.all_num = self.rate[0] + self.rate[1]

    def build_training_model(self):
        for tokens in self.dataset.samples:
            index = 0
            while True:
                self.bigram.append(([tokens[0][index], tokens[0][index+1]], tokens[1]))
                index += 1
                if index >= len(tokens[0])-1:
                    break

    def build_val_model(self):
        for tokens in self.dataset.samples:
            index = 0
            sent = []
            while True:
                sent.append([tokens[0][index], tokens[0][index+1]])
                index += 1
                if index >= len(tokens[0])-1:
                    break
            self.bigram.append((sent, tokens[1]))

    def build_features(self):
        for tokens in self.bigram:
            if tokens[1] == 1:
                self.propag_features.append(tokens[0])
            else:
                self.non_features.append(tokens[0])


class BayesClassifier:

    def __init__(self):
        self.training_set = Bigram("training")
        self.val_set = Bigram("validation")
        self.testing = []

    def initialise(self):
        self.training_set.build_training_model()
        self.training_set.build_features()
        self.val_set.build_val_model()

    def smoothing(self):
        for sent in self.val_set.bigram:
            for tokens in sent[0]:
                if tokens not in self.training_set.propag_features:
                    self.training_set.propag_features.append(tokens)
                if tokens not in self.training_set.non_features:
                    self.training_set.non_features.append(tokens)

        for tokens in self.training_set.non_features:
            if tokens not in self.training_set.propag_features:
                self.training_set.propag_features.append(tokens)
        for tokens in self.training_set.propag_features:
            if tokens not in self.training_set.non_features:
                self.training_set.non_features.append(tokens)

    def get_prob(self):
        self.training_set.propag_features = [tuple(tokens) for tokens in self.training_set.propag_features]
        self.training_set.propag_features = [(tokens, self.training_set.propag_features.count(tokens) / len(self.training_set.propag_features))
                                             for tokens in self.training_set.propag_features]
        # remove repeated items
        self.training_set.propag_features = list(set(self.training_set.propag_features))

        self.training_set.non_features = [tuple(tokens) for tokens in self.training_set.non_features]
        self.training_set.non_features = [(tokens, self.training_set.non_features.count(tokens) / len(self.training_set.non_features))
                                          for tokens in self.training_set.non_features]
        self.training_set.non_features = list(set(self.training_set.non_features))


    def classify(self):
        propag = self.training_set.rate[0]
        non = self.training_set.rate[1]
        propag_prob = propag / self.training_set.all_num
        non_prob = non / self.training_set.all_num

        propag_dict = dict(self.training_set.propag_features)
        non_dict = dict(self.training_set.non_features)

        for sent in self.val_set.bigram:
            pridict_propag = propag_prob
            pridict_non = non_prob

            for tokens in sent[0]:
                key = tuple(tokens)
                pridict_propag -= math.log(propag_dict[key], 10)
            for tokens in sent[0]:
                key = tuple(tokens)
                pridict_non -= math.log(non_dict[key], 10)

            if pridict_propag > pridict_non:
                rst = 1
            elif pridict_propag < pridict_non:
                rst = 0
            else:
                rst = random.randint(0, 1)

            self.testing.append(rst)

    def calculate_score(self):
        labels = self.val_set.dataset.get_label(self.val_set.bigram)
        true_positive = sum(1 for i, j in zip(self.testing, labels) if i == 1 and j == 1)
        false_positive = sum(1 for i, j in zip(self.testing, labels) if i == 1 and j == 0)
        false_negative = sum(1 for i, j in zip(self.testing, labels) if i == 0 and j == 1)

        precision = true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0
        recall = true_positive / (true_positive + false_negative) if (true_positive + false_negative) > 0 else 0
        f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
        print("Precision:", precision)
        print("Recall:", recall)
        print("F1 Score:", f1_score)



test = BayesClassifier()
test.initialise()

test.smoothing()
test.get_prob()

test.classify()



