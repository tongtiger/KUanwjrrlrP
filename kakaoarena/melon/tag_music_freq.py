import pickle
import json
import pickle
from tqdm import tqdm

train_data = json.load(open("../data/train.json", "rb"))

tag_music_freq = {}

for data in tqdm(train_data):
    for tag in data['tags']:
        if tag not in tag_music_freq:
            tag_music_freq[tag] = []
            for song in data['songs']:
                tag_music_freq[tag].append(song)
        else:
            for song in data['songs']:
                tag_music_freq[tag].append(song)

with open("../tag_music_freq.dic", "wb") as f:
    pickle.dump(tag_music_freq, f)
