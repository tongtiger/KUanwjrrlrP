import json
from gensim.models import FastText
import pickle
from tqdm import tqdm
import random

def type2_presager(topn):
    predictions = fasttext.most_similar(positive=[word for word in data['plylst_title'].split(" ")], topn=topn)
    for prediction in predictions:
        if prediction[0] in tag_list:
            result['tags'].append(prediction[0])
        else:
            pass

def type2_vote(frequency):
    for song, freq in musics.items():
        if freq == frequency:
            answer_songs.append(song)
        else:
            pass

def type2_submit_answer():
    for answer_song in answer_songs[:99 + 1]:
        data['songs'].append(answer_song)



val = json.load(open("../results.json", "rb"))

with open("../tag_name.list", "rb") as f:
    tag_list = pickle.load(f)   #태그 리스트

with open("../music_tag.dic", "rb") as f:
    music_tag = pickle.load(f)  #태그를 음악에 따라 묶은 것

with open("../tag_music_freq.dic", "rb") as f:
    tag_music_freq = pickle.load(f)


for data in tqdm(val):
    if len(data['songs']) == 100 and len(data['tags']) == 10:
        pass
    else:
        musics = {}
        data['songs'].clear()
        for tag in data['tags']:
            for song in tag_music_freq[tag][:1500]:
                if song not in musics:
                    musics[song] = 1
                else:
                    musics[song] += 1

        # 투표 결과 반영
        answer_songs = []
        type2_vote(frequency=10)
        if len(answer_songs) >= 100:
            type2_submit_answer()
        else:
            type2_vote(frequency=9)
            if len(answer_songs) >= 100:
                type2_submit_answer()
            else:
                type2_vote(frequency=8)
                if len(answer_songs) >= 100:
                    type2_submit_answer()
                else:
                    type2_vote(frequency=7)
                    if len(answer_songs) >= 100:
                        type2_submit_answer()
                    else:
                        type2_vote(frequency=6)
                        if len(answer_songs) >= 100:
                            type2_submit_answer()
                        else:
                            type2_vote(frequency=5)
                            if len(answer_songs) >= 100:
                                type2_submit_answer()
                            else:
                                type2_vote(frequency=4)
                                if len(answer_songs) >= 100:
                                    type2_submit_answer()

                                else:
                                    type2_vote(frequency=3)
                                    if len(answer_songs) >= 100:
                                        type2_submit_answer()
                                    else:
                                        type2_vote(frequency=2)
                                        if len(answer_songs) >= 100:
                                            type2_submit_answer()
                                        else:
                                            type2_vote(frequency=1)
                                            type2_submit_answer()

for data in val:
    if len(data['songs']) != 100:
        print("Dfd")
        print(len(data['songs']))
        k = 100-len(data['songs'])
        for song in list(music_tag.keys()):
            if k != 0:
                if song not in data['songs']:
                    data['songs'].append(song)
                    k -= 1
                else:
                    pass
            else:
                pass
        print(len(data['songs']))
    elif len(data['tags']) != 10:
        print("kkk")

for data in val:
    data['tags'] = list(set(data['tags']))
    if len(data['tags']) != 10:
        print(data['tags'])
    else:
        pass

with open("../data/results.json", "w", encoding='UTF8') as f:
    json.dump(val, f, ensure_ascii=False)