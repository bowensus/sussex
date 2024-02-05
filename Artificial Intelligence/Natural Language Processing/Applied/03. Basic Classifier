import nltk
import pandas as pd
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
import random
import matplotlib.pyplot as plt

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

pos_training_data = [file[0] for file in training_data]
neg_training_data = [file[0] for file in training_data]
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

# nltk.download('averaged_perceptron_tagger')

def pos_tagged(review):
    tagged_data = []
    for file in review:
        tagged_data.append(nltk.pos_tag(file))
    return tagged_data

pos_tagged_data = pos_tagged(pos_training_data)
neg_tagged_data = pos_tagged(neg_training_data)

def adj_words(review):
    words = []
    for file in review:
        for w in file:
            if w[1] == "JJ":
                words.append(w[0])
    return words

pos_selected_words = adj_words(pos_tagged_data)
neg_selected_words = adj_words(neg_tagged_data)

def words_times(words, k):
    doc = nltk.FreqDist(words)
    word_time = []
    for w in doc.most_common(k):
        word_time.append(w)
    return word_time

pos_word = list(set(pos_selected_words))
neg_word = list(set(neg_selected_words))

pos_times = words_times(pos_selected_words, 100)
neg_times = words_times(neg_selected_words, 100)

def words_select(select_words, sample_words):
    filter_words = []
    for w in select_words:
        isPrime = 1
        for word in sample_words:
            if w[0] == word[0]:
                isPrime = 0
                break
        if isPrime == 1:
            filter_words.append(w)
    return filter_words

pos_words = words_select(pos_times, neg_times)
neg_words = words_select(neg_times, pos_times)

pos_bag = [w[0] for w in pos_words[:10]]
neg_bag = [w[0] for w in neg_words[:10]]

class BasicClassification:
    def __init__(self, content):
        self.content = content
        self.pos = 0
        self.neg = 0

    def classify(self, pos_bag, neg_bag):
        for w in self.content:
            if w in pos_bag:
                self.pos += 1
            if w in neg_bag:
                self.neg += 1
        if self.pos > self.neg:
            return 1
        if self.pos < self.neg:
            return 0
        else:
            return random.randint(0, 1)

pos_result = []
for file in pos_testing_data:
    rst = BasicClassification(file)
    pos_result.append(rst.classify(pos_bag, neg_bag))
neg_result = []
for file in neg_testing_data:
    rst = BasicClassification(file)
    neg_result.append(rst.classify(pos_bag, neg_bag))

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
