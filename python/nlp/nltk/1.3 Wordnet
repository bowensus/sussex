import nltk
import pandas
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic as wn_ic
nltk.download('wordnet')
nltk.download('wordnet_ic')

cat_synsets = wn.synsets("cat", wn.NOUN)
for i, s in enumerate(cat_synsets):
    wordforms = [l.name() for l in s.lemmas()]
    print("{}:{}\n\t{}". format(i, wordforms, s.definition()))

cat_synsets = wn.synsets("cat", wn.NOUN)

for h in cat_synsets[6].hyponyms():
    h_words = [w.name() for w in h.lemmas()]
    print("{}:{}".format(h_words, h.definition()))

print()
for h in cat_synsets[6].hypernyms():
    h_words=[w.name() for w in h.lemmas()]
    print("{}:{}".format(h_words,h.definition()))

def distance_to_root(synset, n):
    h_synset = synset.hypernyms()
    step = n
    if h_synset == []:
        return step
    else:
        step += 1
        return distance_to_root(h_synset[0], step)

steps = distance_to_root(cat_synsets[6], 1)
print(steps)

brown_ic=wn_ic.ic("ic-brown.dat")
print(wn.path_similarity(cat_synsets[0], cat_synsets[1]))
print(wn.res_similarity(cat_synsets[0], cat_synsets[1], brown_ic))
print(wn.lch_similarity(cat_synsets[0], cat_synsets[1], brown_ic))

def norn_similarity(word1, word2, measure):
    synset1 = wn.synsets(word1, wn.NOUN)
    synset2 = wn.synsets(word2, wn.NOUN)
    similarity = []
    for synset in synset1:
        for synset_ in synset2:
            if measure == "path":
                similarity.append(wn.path_similarity(synset, synset_))
            elif measure == "res":
                similarity.append(wn.res_similarity(synset, synset_, brown_ic))
            elif measure == "lin":
                similarity.append(wn.lch_similarity(synset, synset_, brown_ic))
    similarity.sort()
    return similarity[-1]

path_similarity = norn_similarity("chicken", "car", "path")
resnik_similarity = norn_similarity("chicken", "car", "res")
lin_similarity = norn_similarity("chicken", "car", "lin")
print("The path similarity of chicken and car is", path_similarity)
print("The resnik similarity of chicken and car is", resnik_similarity)
print("The lin similarity of chicken and car is", lin_similarity)
