import spacy
import json
from jieba import analyse

tfidf = analyse.extract_tags

src = open('/data2/yzh/Dataset/Multi-30K/multi30k_bpe/annotation/trn.en.bpe.txt', 'r', encoding='utf-8').readlines()

id2tags = dict()
tags2id = dict()

def get_tags(i):
    src_text = src[i]
    tags_list = tfidf(src_text)
    print(i, src_text)
    id2tags[i] = tags_list
    for tag in tags_list:
        if tag not in tags2id:
            tags2id[tag] = [i]
        else:
            tags2id[tag].append(i)


for i in range(len(src)):
    get_tags(i)
with open('/data2/yzh/Dataset/Multi-30K/id2tags_bpe.trn.json', 'w', encoding='utf-8') as f:
    json.dump(id2tags, f, ensure_ascii=False)
with open('/data2/yzh/Dataset/Multi-30K/tags2id_bpe.trn.json', 'w', encoding='utf-8') as f:
    json.dump(tags2id, f, ensure_ascii=False)
print('done')