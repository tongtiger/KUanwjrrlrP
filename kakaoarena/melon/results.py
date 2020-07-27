import json
from gensim.models import FastText
import pickle
from tqdm import tqdm
import random

#필요한 자료 및 모델
val_data = json.load(open("data/test.json", "rb"))   #맞춰야 하는 데이터

with open("tag_name.list", "rb") as f:
    tag_list = pickle.load(f)   #태그 리스트

with open("music_tag.dic", "rb") as f:
    music_tag = pickle.load(f)  #태그를 음악에 따라 묶은 것

with open("tag_music_freq.dic", "rb") as f:
    tag_music_freq = pickle.load(f)

fasttext = FastText.load("FastText.model")


#예상 내용이 들어가는 리스트, 일단 태그 10개, 곡 100개 만족하는거는 나중에 따로 처리해주고, 일단 채워넣는 단계
results = []

#def type1_presager(data, ...):

def type1_vote(frequency):
    for tag, freq in tags.items():
        if freq == frequency:
            answer_tags.append(tag)
        else:
            pass

def type1_submit_answer():
    for answer_tag in answer_tags[:9+ 1]:
        result['tags'].append(answer_tag)

def type2_presager(topn):
    predictions = fasttext.most_similar(positive=[word for word in data['plylst_title'].split(" ")], topn=topn)
    for prediction in predictions:
        if prediction[0] in tag_list:
            if prediction[0] not in result['tags']:
                result['tags'].append(prediction[0])
            else:
                pass
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
        result['songs'].append(answer_song)


def type3_presager(topn):
    pre_predictions.clear()
    predictions = fasttext.most_similar(positive=[tag for tag in data['tags']] + [tag for tag in tags], topn=topn)
    for prediction in predictions:
        if prediction[0] in tag_list:
            if prediction[0] not in pre_predictions:
                pre_predictions.append(prediction[0])
            else:
                pass
        else:
            pass

def type4_presager(topn):
    predictions = fasttext.most_similar(positive=[tag for tag in data['tags']] + [tag for tag in data['tags']], topn=topn)
    for prediction in predictions:
        if prediction[0] in tag_list:
            if prediction[0] not in result['tags']:
                result['tags'].append(prediction[0])
            else:
                pass
        else:
            pass


#위에서 정의한 함수 4개는 아래와 같이 사용될 예정, topn만 조정하여 태그 개수 충족
for data in tqdm(val_data):
    result = {'id': data['id'], 'songs': [], 'tags': []}    #results 안에 들어갈 데이터(딕셔너리)

    #type1 problem
    if data['tags'] == [] and data['plylst_title'] == '':
        tags = {}
        for song in data['songs']:
            if song in music_tag:
                for tag in music_tag[song]:
                    if tag not in tags:
                        tags[tag] = 1
                    else:
                        tags[tag] += 1
            else:
                pass

        answer_tags = []
        type1_vote(frequency=10)
        if len(answer_tags) >= 10:
            type1_submit_answer()
        else:
            type1_vote(frequency=9)
            if len(answer_tags) >= 10:
                type1_submit_answer()
            else:
                type1_vote(frequency=8)
                if len(answer_tags) >= 10:
                    type1_submit_answer()
                else:
                    type1_vote(frequency=7)
                    if len(answer_tags) >= 10:
                        type1_submit_answer()
                    else:
                        type1_vote(frequency=6)
                        if len(answer_tags) >= 10:
                            type1_submit_answer()
                        else:
                            type1_vote(frequency=5)
                            if len(answer_tags) >= 10:
                                type1_submit_answer()
                            else:
                                type1_vote(frequency=4)
                                if len(answer_tags) >= 10:
                                    type1_submit_answer()

                                else:
                                    type1_vote(frequency=3)
                                    if len(answer_tags) >= 10:
                                        type1_submit_answer()
                                    else:
                                        type1_vote(frequency=2)
                                        if len(answer_tags) >= 10:
                                            type1_submit_answer()
                                        else:
                                            type1_vote(frequency=1)
                                            type1_submit_answer()

        if 0 < len(result['tags']) < 10:
            k = 10 - len(result['tags'])
            predictions = fasttext.most_similar(positive=[tag for tag in result['tags']], topn = 150)
            for prediction in predictions:
                if k != 0:
                    if prediction[0] in tag_list:
                        if prediction[0] not in result['tags']:
                            result['tags'].append(prediction[0])
                            k -= 1
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            print(len(result['tags']))
        elif len(result['tags']) == 0:
            for i in range(10):
                result['tags'].append(tag_list[i])
        else:
            pass

        # 투표
        musics = {}
        for tag in result['tags']:
            for song in tag_music_freq[tag][:500]:
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

        if len(result['songs']) == 100 and len(result['tags']) == 10:
            pass
        else:
            print(len(result['songs']), ",", len(result['tags']))
            print("type1")

    #type2 problem
    elif data['tags'] == data['songs'] == []:
        type2_presager(topn=100)
        if len(result['tags']) >= 10:
            result['tags'] = result['tags'][:9 + 1]
        else:
            result['tags'].clear()
            type2_presager(topn=200)
            if len(result['tags']) >= 10:
                result['tags'] = result['tags'][:9 + 1]
            else:
                result['tags'].clear()
                type2_presager(topn=500)
                if len(result['tags']) >= 10:
                    result['tags'] = result['tags'][: 9 + 1]
                else:
                    result['tags'].clear()
                    type2_presager(topn=1500)
                    if len(result['tags']) >= 10:
                        result['tags'] = result['tags'][: 9 + 1]
                    else:
                        result['tags'].clear()
                        type2_presager(topn=4000)
                        if len(result['tags']) >= 10:
                            result['tags'] = result['tags'][: 9 + 1]
                        else:
                            result['tags'].clear()
                            type2_presager(topn=7000)
                            result['tags'] = result['tags'][: 9 + 1]


        # 투표
        musics = {}
        for tag in result['tags']:
            for song in tag_music_freq[tag][:500]:
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
        if len(result['songs']) == 100 and len(result['tags']) == 10:
            pass
        else:
            print(len(result['songs']), ",", len(result['tags']))
            print("type2")

    #type3 problem
    elif data['tags'] != [] and data['songs'] != [] and data['plylst_title'] == '':
        song_tag_basket = []
        for song in data['songs']:
            if song not in song_tag_basket:
                song_tag_basket.append(song)
            else:
                pass
        tags_freq = {}
        for song in song_tag_basket:
            if song in music_tag:
                for tag in music_tag[song]:
                    if tag not in tags_freq:
                        tags_freq[tag] = 1
                    else:
                        tags_freq[tag] += 1
            else:
                pass
        tags = []
        for tag, freq in tags_freq.items():
            if freq == 1:
                pass
            else:
                tags.append(tag)

        pre_predictions = []

        type3_presager(topn=50)

        if len(pre_predictions) >= 10:
            for i in range(10):
                result['tags'].append(pre_predictions[i])
        else:
            type3_presager(topn=100)
            if len(pre_predictions) >= 10:
                for i in range(10):
                    result['tags'].append(pre_predictions[i])
            else:
                type3_presager(topn=500)
                if len(pre_predictions) >= 10:
                    for i in range(10):
                        result['tags'].append(pre_predictions[i])
                else:
                    type3_presager(topn=1500)
                    if len(pre_predictions) >= 10:
                        for i in range(10):
                            result['tags'].append(pre_predictions[i])
                    else:
                        type3_presager(topn=7000)
                        for i in range(10):
                            result['tags'].append(pre_predictions[i])

        # 투표
        musics = {}
        for tag in result['tags']:
            for song in tag_music_freq[tag][:500]:
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
        if len(result['songs']) == 100 and len(result['tags']) == 10:
            pass
        else:
            print(len(result['songs']), ",", len(result['tags']))
            print("type3")

    #type4 problem
    else:
        type4_presager(topn=50)
        if len(result['tags']) >= 10:
            result['tags'] = result['tags'][:9 + 1]
        else:
            type4_presager(topn=100)
            if len(result['tags']) >= 10:
                result['tags'] = result['tags'][:9 + 1]
            else:
                type4_presager(topn=500)
                if len(result['tags']) >= 10:
                    result['tags'] = result['tags'][:9 + 1]
                else:
                    type4_presager(topn=1500)
                    if len(result['tags']) >= 10:
                        result['tags'] = result['tags'][:9 + 1]
                    else:
                        type4_presager(topn=4000)
                        if len(result['tags']) >= 10:
                            result['tags'] = result['tags'][:9 + 1]
                        else:
                            type4_presager(topn = 7000)
                            result['tags'] = result['tags'][:9+1]

        # 투표
        musics = {}
        for tag in result['tags']:
            for song in tag_music_freq[tag][:500]:
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

        if len(result['songs']) == 100 and len(result['tags']) == 10:
            pass
        else:
            print(len(result['songs']), ",", len(result['tags']))
            print("type4")

    results.append(result)


with open("results.json", "w", encoding='UTF8') as f:
    json.dump(results, f, ensure_ascii=False)

