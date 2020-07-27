import json
import pickle
from tqdm import tqdm

train_data = json.load(open("../data/train.json", "rb"))

tag_name = []

for data in tqdm(train_data):
    for tag in data['tags']:
        if tag not in tag_name:
            tag_name.append(tag)
        else:
            pass

with open("../tag_name.list", "wb") as f:
    pickle.dump(tag_name, f)