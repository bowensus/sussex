import csv
import random
import numpy as np
from collections import Counter
import numpy.random
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import torch
import torch.nn as nn
from torch import optim
from torch.utils.data import Dataset, DataLoader
from sklearn.metrics import mean_absolute_error

# read files and transform to numpy array
def get_data(path):
    with open(path, newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        data = list(reader)
        data = np.array(data)
    return data

trade_data = get_data("Food trade indicators - FAOSTAT_data_en_2-22-2024.csv")
consumer_data = get_data("Consumer prices indicators - FAOSTAT_data_en_2-22-2024.csv")
production_data = get_data("Crops production indicators - FAOSTAT_data_en_2-22-2024.csv")
employment_data = get_data("Employment - FAOSTAT_data_en_2-27-2024.csv")
exchange_data = get_data("Exchange rate - FAOSTAT_data_en_2-22-2024.csv")
fertilizers_data = get_data("Fertilizers use - FAOSTAT_data_en_2-27-2024.csv")
balance_data = get_data("Food balances indicators - FAOSTAT_data_en_2-22-2024.csv")
foreign_data = get_data("Foreign direct investment - FAOSTAT_data_en_2-27-2024.csv")
landuse_data = get_data("Land use - FAOSTAT_data_en_2-22-2024.csv")
pesticides_data = get_data("Pesticides use - FAOSTAT_data_en_2-27-2024.csv")

def unified_unit(data):
    # unit comsumer data
    for row in data:
        if row[12] == '%':
            row[13] = float(row[13]) * 100

unified_unit(consumer_data)

years = list(range(2010, 2023))

# get the values of features and labels
def get_labels(col_y, col_l, col_v, target, data):
    idx = 0
    feature_values = {}
    country_counts = Counter(int(row[2]) for row in data)

    for country in country_counts.keys():
        for year in years:
            value = 0
            for i, row in enumerate(data[idx:]):
                if int(row[2]) == country and int(row[col_y]) == year and row[col_l] == target:
                    value += float(row[col_v])
                # To iterate over the rows corresponding to the current country and then stop.
                if i >= country_counts[country]:
                    break
            # Add up the values of the labels in the current country and the current year.
            feature_values[(country, year)] = value
        # Once all the years of the current country have been traversed, update to the next slice
        # for traversing the rows of the next country.
        idx += country_counts[country]
    return feature_values

comsumers = get_labels(4, 0, 13, "CP", consumer_data)
production = get_labels(8, 0, 11, "QCL", production_data)
employment = get_labels(8, 0, 15, "OEA", employment_data)
exchange = get_labels(8, 0, 13, "PE", exchange_data)
fertilizers = get_labels(8, 0, 11, "RFB", fertilizers_data)
foreign = get_labels(8, 0, 11, "FDI", foreign_data)
landuse = get_labels(8, 0, 11, "RL", landuse_data)
pesticides = get_labels(8, 0, 11, "RP", pesticides_data)
export_value = get_labels(8, 5, 11, "Export Value", trade_data)
import_value = get_labels(8, 5, 11, "Import Value", trade_data)
import_quantity = get_labels(8, 5, 11, "Import Quantity", balance_data)
export_quantity = get_labels(8, 5, 11, "Export Quantity", balance_data)
losses = get_labels(8, 5, 11, "Losses", balance_data)

dataset = []
countries = []
for country in Counter(int(row[2]) for row in trade_data):
    if country not in countries:
        countries.append(country)

def get_dataset(data):
    set = []
    data_countries = [item[0] for item in data.keys()]
    for country in countries:
        for year in years:
            if country not in data_countries:
                set.append(0)
            else:
                set.append(data[(country, year)])
    dataset.append(set)

get_dataset(comsumers)
get_dataset(production)
get_dataset(employment)
get_dataset(exchange)
get_dataset(fertilizers)
get_dataset(foreign)
get_dataset(landuse)
get_dataset(pesticides)
get_dataset(import_value)
get_dataset(import_quantity)
get_dataset(export_quantity)
get_dataset(losses)
get_dataset(export_value)

countries = [country for country in countries for i in range(len(years))]
num = len(countries)
years = [years[i % len(years)] for i in range(num)]

dataset.insert(0, countries)
dataset.insert(1, years)

dataset = np.array(dataset)
dataset = np.transpose(dataset)

# np.savetxt('output.csv', dataset, delimiter=',')

features = dataset[:, 2:-1]
labels = dataset[:, -1]

# features normalisation
features_scaler = MinMaxScaler()
features = features_scaler.fit_transform(features)

# training : validation = 0.8 : 0.2
random_seed = 1
all_ids = np.arange(0, dataset.shape[0])
train_set_size = 2100
val_set_size = 539
train_set_ids, val_set_ids = train_test_split(all_ids, test_size=val_set_size, train_size=train_set_size,
                                             random_state=random_seed, shuffle=True)

# get training set and validation set
training_features = features[train_set_ids, :]
training_labels = [labels[i] for i in train_set_ids]

val_features = features[val_set_ids, :]
val_labels = [labels[i] for i in val_set_ids]

# setting random seed and keep the result consistant every time
random.seed(random_seed)
torch.manual_seed(random_seed)
numpy.random.seed(random_seed)


# define the FNN(MLP) Model
class FNN(nn.Module):

    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()

        self.hidden_layers = nn.ModuleList()
        for i in range(3):
            if i == 0:
                self.hidden_layers.append(nn.Linear(input_size, hidden_size))
            else:
                self.hidden_layers.append(nn.Linear(hidden_size, hidden_size))
        self.output_layer = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        for hidden_layer in self.hidden_layers:
            x = torch.relu(hidden_layer(x))
        output = self.output_layer(x)
        return output


# transfer the numpy data type to torch tensor type
class MetDataset(Dataset):
    def __init__(self, features, labels):
        self.features = torch.tensor(features, dtype=torch.float32)
        self.labels = torch.tensor(labels, dtype=torch.float32)

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return self.features[idx, :], self.labels[idx]


features_count = training_features.shape[1]

# Setting hyperparameters
p_layers = [10, 20, 30]
num_epochs = 20
learning_rates = [0.001, 0.01, 0.1]
# input_matrix(batch_size, features_count), output_matrix(hidden_size[-1], output_size)
batch_sizes = [16, 32, 64]

parameters = [(batch_size, rate, p_layer) for batch_size in batch_sizes for rate in learning_rates for p_layer in p_layers]

def training_model(parameter):
    p_layer, rate, batch_size = parameter

    input_size = features_count
    hidden_size = p_layer
    output_size = 1

    my_MLP = FNN(input_size, hidden_size, output_size)

    # loading data by batch
    train_set = MetDataset(training_features, training_labels)
    train_dataloader = DataLoader(train_set, batch_size=batch_size)

    val_set = MetDataset(val_features, val_labels)
    val_dataloader = DataLoader(val_set, batch_size=batch_size)

    # Setting up the stochastic gradient descent optimizer for updating the model weights
    optimizer = optim.SGD(my_MLP.parameters(), lr=rate)
    # loss_function = nn.MSELoss()

    # start training the model
    for epoch in range(num_epochs):

        my_MLP.train()

        # traininig
        for batch, (x_train, y_train) in enumerate(train_dataloader):
            # The gradient of the parameter is zeroed. In PyTorch, gradients are cumulative.
            optimizer.zero_grad()

            train_pred = my_MLP.forward(x_train)
            # train_loss = loss_function(train_pred, y_train)

            # train_loss.backward()
            optimizer.step()

        # Evaluating on the validation set
        val_predictions = []
        val_true_labels = []
        my_MLP.eval()

        # validation
        for batch, (x_val, y_val) in enumerate(val_dataloader):
            val_pred = my_MLP.forward(x_val)
            val_predictions.extend(val_pred.tolist())
            val_true_labels.extend(y_val.tolist())
        avg_val_mae = mean_absolute_error(val_true_labels, val_predictions)

    return avg_val_mae

accuracies = []
for parameter in parameters:
    accuracies.append((parameter, training_model(parameter)))
accuracies_sorted = sorted(accuracies, key=lambda x : x[1], reverse=False)

print("trade_data: \n", trade_data)
print("dataset: \n", dataset)
print("features: \n", features)
print("labels: \n", labels)
print("all parameters try: \n", accuracies_sorted)
print('\n', accuracies_sorted[0])
