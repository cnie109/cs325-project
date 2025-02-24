import pickle

data = {}
with open("./data/train", "rb") as file:
    data = pickle.load(file, encoding='bytes')

print(data.keys())

