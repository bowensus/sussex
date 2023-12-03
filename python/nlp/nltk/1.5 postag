import nltk
from nltk.corpus import treebank
import math
nltk.download('punkt')
nltk.download('treebank')

tagged = treebank.tagged_words()
tagged = [(w, tag) for w, tag in tagged if w.isalpha()]

def find_tagged(tagged):
    words = [w[0] for w in tagged]
    words_tagged = {w: {} for w in words}
    for w in tagged:
        if w[1] not in words_tagged[w[0]].keys():
            words_tagged[w[0]].update({w[1]:1})
        else:
            words_tagged[w[0]][w[1]] += 1
    return words_tagged

words_tagged = find_tagged(tagged)

def postag_count(w):
    postag_list = list(words_tagged[w].keys())
    return len(postag_list)

def entorpy(w):
    count = sum(words_tagged[w].values())
    rst = 0
    for i in words_tagged[w].values():
        rst += (i/count) * math.log(i/count, 2)
    return -rst

print("while: {:.5f} show: {:.5f} the: {:.5f}". format(entorpy("white"), entorpy("show"), entorpy("the")))

ratio = 0.7
n = int(len(tagged) * ratio)
training_set = tagged[:n]
testing_set = tagged[n:]
training_tagged = find_tagged(training_set)
testing_tagged = find_tagged(testing_set)

def pro_postag(tagged):
    for w in tagged.keys():
        tagged[w].update({tag:tagged[w][tag]/sum(tagged[w].values()) for tag in tagged[w].keys()})

pro_postag(training_tagged)
training_words = [w[0] for w in training_set]

def uni_postag(words, probility):
    uni = []
    for w in words:
        tag_predict = max(probility[w], key=probility[w].get)
        uni.append((w, tag_predict))
    return uni

uni_training = uni_postag(training_words, training_tagged)

def evaluate_uni_postag(test, gold_standard):
    cnt = 0
    for i, w in enumerate(test):
        if w[1] == gold_standard[i][1]:
            cnt += 1
    accuracy = cnt / len(test)
    return accuracy

accuracy = evaluate_uni_postag(uni_training, training_set)
print("{:.2f}%". format(accuracy*100))
