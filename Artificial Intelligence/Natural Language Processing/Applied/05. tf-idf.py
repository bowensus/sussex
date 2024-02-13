import nltk
from nltk.corpus import gutenberg
from nltk.corpus import stopwords
import math
# from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('gutenberg')

book_ids=gutenberg.fileids()
books={b:gutenberg.words(b) for b in book_ids}

eng_stopwords = stopwords.words("english")

def normalise(book_ids):
    for book in book_ids:
        books[book] = [w for w in books[book] if w.isalpha() and w.lower() not in eng_stopwords]

normalise(book_ids)

def get_count(book_ids):
    for book in book_ids:
        doc = nltk.FreqDist(books[book])
        books[book] = {w:doc[w] for w in books[book]}

get_count(book_ids)

def doc_AB(book_ids, i, j):
    words = list(set(books[book_ids[i]].keys()) & set(books[book_ids[j]].keys()))
    ret = 0
    for w in words:
        ret += books[book_ids[i]][w] * books[book_ids[j]][w]
    return ret

ret_AB = doc_AB(book_ids, 0, 1)
print("dot_AB =", ret_AB)

def norm(book_ids, i):
    norm = 0
    for w in books[book_ids[i]].keys():
        norm += books[book_ids[i]][w] * books[book_ids[i]][w]
    norm = math.sqrt(norm)
    return norm

norm_A = norm(book_ids, 0)
norm_B = norm(book_ids, 1)
cos_AB = ret_AB / (norm_A*norm_B)
print("cos_sim =", cos_AB)

def get_tf(word, book_ids, i):
    tf_num = books[book_ids[i]][word] / len(books[book_ids[i]])
    return tf_num

def get_df(word, book_ids):
    df_num = 0
    for book in book_ids:
        if word in books[book].keys():
            df_num += 1
    return df_num

def get_idf(num):
    idf_num = math.log2(len(books) / num)
    return idf_num

books_tfidf = dict()

for i in range(len(book_ids)):
    tfidf_values = {w: get_tf(w, book_ids, i) * get_idf(get_df(w, book_ids)) for w in books[book_ids[i]].keys()}
    books_tfidf[book_ids[i]] = tfidf_values

def sort_tfidf(book_ids, i):
    sort_items = sorted(books_tfidf[book_ids[i]].items(), key=lambda x:x[1], reverse=True)
    return sort_items

sort_book_tfidf = sort_tfidf(book_ids, 0)
print(sort_book_tfidf[:3])
