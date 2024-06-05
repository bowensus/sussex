from setting import Dataset
import torch
import torch.nn as nn
import torch.optim as optim
from torch.nn.utils.rnn import pad_sequence

def get_data(catagory="training"):
    data_set = Dataset()
    data_set.get_file(catagory)
    data_set.get_tokens()
    data_set.normalise()
    num_words = data_set.get_words_num(data_set.samples)

    words_to_idx = data_set.pre_processing(data_set.samples)
    labels = data_set.get_label(data_set.samples)

    sents_length = [len(sent) for sent in words_to_idx]
    sents_average = sum(sents_length) / len(sents_length)

    X_data = [torch.tensor(sent) for sent in words_to_idx]
    X_data_truncated = [torch.tensor(sent[:7]) for sent in words_to_idx]
    # padding for x_train
    X_data = pad_sequence(X_data, batch_first=True, padding_value=0)
    Y_data = torch.tensor(labels)
    return X_data, Y_data, num_words

X_train, Y_train, num_train = get_data("training")
X_val, Y_val, num_val = get_data("validation")

num_train += 1

# Define BLSTM model for propaganda detection
class BLSTM(nn.Module):

    def __init__(self, num_words, embedding_dim, lstm_units, num_classes):
        super(BLSTM, self).__init__()
        self.embedding = nn.Embedding(num_words, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, lstm_units, bidirectional=True, batch_first=True)
        self.fc = nn.Linear(lstm_units*2, num_classes)

    def forward(self, x):
        embedding = self.embedding(x)
        lstm_out, _ = self.lstm(embedding)
        # Concatenate the last hidden state from both directions
        lstm_out = torch.cat((lstm_out[:, -1, :lstm_units], lstm_out[:, 0, lstm_units:]), dim=1)
        output = self.fc(lstm_out)
        return lstm_out

# Model parameters
embedding_dim = 50
lstm_units = 128
num_classes = 2

# set model and loss fuction
blstm_model = BLSTM(num_train, embedding_dim, lstm_units, num_classes)
optimizer = optim.Adam(blstm_model.parameters(), lr=0.01)
criterion = nn.CrossEntropyLoss()

# Training loop
num_epochs = 5
for epoch in range(num_epochs):
    blstm_model.train()
    optimizer.zero_grad()
    outputs = blstm_model(X_train)
    loss = criterion(outputs, Y_train)
    loss.backward()
    optimizer.step()

    print(f'Epoch {epoch+1}/{num_epochs}, Loss: {loss.item():.4f}')

# Inference
blstm_model.eval()
with torch.no_grad():
    # Forward pass on test data
    outputs = blstm_model(X_val)
    # Predicted labels
    preds = torch.argmax(outputs, dim=1)
    # Calculate accuracy
    accuracy = (preds == Y_val).float().mean()
    print("Accuracy:", accuracy.item())
