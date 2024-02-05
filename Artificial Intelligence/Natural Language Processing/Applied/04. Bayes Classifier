import nltk
import pandas as pd
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
import random
import matplotlib.pyplot as plt
import math

nltk.download("stopwords")
nltk.download("movie_reviews")

pos_reviews = movie_reviews.fileids("pos")
neg_reviews = movie_reviews.fileids("neg")

def reviews_data(review, category):
    data = []
    for file in review:
        data.append((list(movie_reviews.words(file)), category))
    return data

pos_reviews = reviews_data(pos_reviews, "pos")
neg_reviews = reviews_data(neg_reviews, "neg")

def split_data(review, ratio):
    random.shuffle(review)
    n = len(review)
    train = review[:int(n*ratio)]
    test = review[int(n*ratio):]
    return (train, test)

pos_training_data, pos_testing_data = split_data(pos_reviews, 0.7)
neg_training_data, neg_testing_data = split_data(neg_reviews, 0.7)

pos_training_data = [file[0] for file in pos_training_data]
neg_training_data = [file[0] for file in neg_training_data]
pos_testing_data = [file[0] for file in pos_testing_data]
neg_testing_data = [file[0] for file in neg_testing_data]

def filter_stopwords(review):
    stop_words = stopwords.words("english")
    filter_data = []
    for i, file in enumerate(review):
        filter_data.append([])
        for w in file:
            if w not in stop_words and w.isalpha():
                filter_data[i].append(w)
    return filter_data

pos_training_data = filter_stopwords(pos_training_data)
neg_training_data = filter_stopwords(neg_training_data)

# BayesClassification
def words_list(reviews):
    all_words = []
    for review in reviews:
        all_words += review
    return all_words

pos_words = words_list(pos_training_data)
neg_words = words_list(neg_training_data)

pos_testing_data = filter_stopwords(pos_testing_data)
neg_testing_data = filter_stopwords(neg_testing_data)
pos_testing_words = words_list(pos_testing_data)
neg_testing_words = words_list(neg_testing_data)

def words_final(words, test):
    words += list(set(words))
    for w in set(test):
        if w not in words:
            words.append(w)
    return words

pos_words = words_final(pos_words, pos_testing_words + neg_testing_words)
neg_words = words_final(neg_words, pos_testing_words + neg_testing_words)

pos_doc = nltk.FreqDist(pos_words)
neg_doc = nltk.FreqDist(neg_words)
pos_len = len(pos_words)
neg_len = len(neg_words)

class BayesClassification:

    def __init__(self, content):
        self.content = content
        self.pos = 0.5
        self.neg = 0.5

    def predict(self):
        pos_possibility = math.log(self.pos, 10)
        for w in self.content:
            x = math.log(pos_doc[w]/pos_len, 10)
            pos_possibility += x
        neg_possibility = math.log(self.neg, 10)
        for w in self.content:
            x = math.log(neg_doc[w]/neg_len, 10)
            neg_possibility += x
        if pos_possibility > neg_possibility:
            return 1
        elif pos_possibility < neg_possibility:
            return 0
        else:
            return random.randint(0, 1)

pos_result = []
for review in pos_testing_data:
    file = BayesClassification(review)
    pos_result.append(file.predict())
neg_result = []
for review in neg_testing_data:
    file = BayesClassification(review)
    neg_result.append(file.predict())

pos_recall_rate = pos_result.count(1) / len(pos_result)
neg_recall_rate = neg_result.count(0) / len(neg_result)
pos_precision = pos_result.count(1) / (pos_result.count(1) + neg_result.count(1))
neg_precision = neg_result.count(0) / (pos_result.count(0) + neg_result.count(0))
accuracy = (pos_result.count(1) + neg_result.count(0)) / len(pos_result + neg_result)
error_rate = (pos_result.count(0) + neg_result.count(1)) / len(pos_result + neg_result)

df1 = pd.DataFrame([[pos_result.count(1), pos_result.count(0), len(pos_result)],
                     [neg_result.count(1), neg_result.count(0), len(neg_result)],
                     [pos_result.count(1) + neg_result.count(1), pos_result.count(0) + neg_result.count(0),
                      len(pos_result + neg_result)]], index=("+ve", "-ve", "total"), columns=("+ve", "-ve", "total"))

print("pos_recall_rate = {:.2f}". format(pos_recall_rate))
print("neg_recall_rate = {:.2f}". format(neg_recall_rate))
print("pos_precision = {:.2f}". format(pos_precision))
print("neg_precision = {:.2f}". format(neg_precision))
print("accuracy = {:.2f}". format(accuracy))
print("error_rate = {:.2f}". format(error_rate))
