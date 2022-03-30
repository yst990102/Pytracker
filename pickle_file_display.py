import pickle

file = "output.file"

with open(file, "rb") as f:
    pickle_load_result = pickle.load(f)
    print(pickle_load_result)
    f.close()