import pickle

filename = "tmp.pkl"

with open(filename, "rb") as file:
    reader = pickle.load(file)

print(reader, "\n", "no. of unique actors",len(reader))
