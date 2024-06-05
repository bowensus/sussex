from setting import Dataset
from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# loading pre-model
model_name = "hfl/chinese-roberta-wwm-ext"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# processing
def get_data(catagory="training"):
    data_set = Dataset()
    data_set.get_file(catagory)
    data_set.get_tokens()
    data_set.normalise()
    text_set = data_set.get_sentence(data_set.samples)
    text_label = data_set.get_label(data_set.samples)
    return text_set, text_label

train_set, train_label = get_data()
test_set, test_label = get_data("validation")

X_train, y_train, X_test, y_test = train_set, train_label, test_set, test_label

print(y_train[:3])

# get bert embeddings
def get_bert_embeddings(text):
    inputs = tokenizer(text, padding=True, truncation=True, max_length=512, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

# transform to bert data
X_train_bert = [get_bert_embeddings(text) for text in X_train]
X_test_bert = [get_bert_embeddings(text) for text in X_test]

# SVC classify
svm_clf = SVC(kernel='linear')
svm_clf.fit(X_train_bert, y_train)

# test
y_pred = svm_clf.predict(X_test_bert)

print("Classification Report:")
print(classification_report(y_test, y_pred))

