import json
import pickle
from tqdm import tqdm

train_data = json.load(open("../data/train.json", "rb"))

music_tag = {}

for data in tqdm(train_data):
    for song in data['songs']:
        if song not in music_tag:
            music_tag[song] = []
            for tag in data['tags']:
                music_tag[song].append(tag)
        else:
            for tag in data['tags']:
                music_tag[song].append(tag)

with open("../music_tag.dic", "wb") as f:
    pickle.dump(music_tag, f)