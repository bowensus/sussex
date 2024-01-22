import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize, word_tokenize
import math

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("gutenberg")

books_ids = gutenberg.fileids()
books = {b:gutenberg.words(b) for b in books_ids}

all_words = []
for i in range(len(books_ids)):
    all_words += list(books[books_ids[i]])

gutenberg_sentences = sent_tokenize(' '.join(all_words))
gutenberg_tokens = []
for sent in gutenberg_sentences:
    gutenberg_tokens.append(word_tokenize(sent))

tokens = []
for i, sent in enumerate(gutenberg_tokens):
    tokens.append([])
    for w in sent:
        if w.isdigit():
            tokens[i].append("NUM")
        elif w.isalpha():
            tokens[i].append(w.lower())

word_tokens = []
for token in tokens:
    word_tokens += token

doc = nltk.FreqDist(word_tokens)
common_words = doc.most_common(100)

def generate_features(tokens, words, window=3):
    words_closed = {w: [] for w in set(words)}

    for sent in tokens:
        for i, w in enumerate(sent):
            if i - window >= 0:
                words_closed[w].extend(sent[i - window:i])
            if i + window < len(sent):
                words_closed[w].extend(sent[i + 1:i + window + 1])

    for w in list(words_closed.keys()):
        doc = nltk.FreqDist(words_closed[w])
        words_closed[w] = {w:doc[w] for w in words_closed[w]}
    return words_closed

words_closed = generate_features(tokens, word_tokens)

print(words_closed["house"]["summer"])

words_feature = dict()

for w in list(words_closed.keys()):
    words_feature[w] = sum(words_closed[w].values())

n = sum(words_feature.values())
print(n)

def calculate_PPMI(word1, word2, n):
    pmi_AB = words_closed[word1][word2]
    pmi_A = words_feature[word1]
    pmi_B = words_feature[word2]
    ppmi = max(math.log2(pmi_AB*n/(pmi_A*pmi_B)), 0)
    return ppmi

ppmi = calculate_PPMI("summer", "house", n)
print(ppmi)

def dot_AB(word1, word2):
    words_set = set(words_closed[word1].keys()) & set(words_closed[word2].keys())
    ret = 0
    for w in words_set:
        ret += calculate_PPMI(word1, w, n) * calculate_PPMI(word2, w, n)
    return ret

def len_A(word):
    words_set = set(words_closed[word].keys())
    ret = 0
    for w in words_set:
        ret += math.pow(calculate_PPMI(word, w, n), 2)
    return ret

cos_AB = dot_AB("summer", "winter") / math.sqrt(len_A("summer") * len_A("winter"))

print(cos_AB)
