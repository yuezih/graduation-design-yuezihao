import re
import spacy
import json

# NLP = spacy.load('en_core_web_sm')
# NLP_DE = spacy.load('de_core_news_sm')

src = open('/data2/yzh/Dataset/Multi-30K/multi30k_bpe/annotation/trn.en.bpe.txt', 'r', encoding='utf-8').readlines()
trg = open('/data2/yzh/Dataset/Multi-30K/multi30k_bpe/annotation/trn.de.bpe.txt', 'r', encoding='utf-8').readlines()

# def tokenize_en(text):
#     text = re.sub(r"\s", " ", text)
#     if (len(text), 100):
#         text = text[:100]
#     return [
#         x.text for x in NLP.tokenizer(text) if x.text != " " and len(x.text) >= 1]

# def tokenize_de(text):
#     text = re.sub(r"\s", " ", text)
#     if (len(text), 100):
#         text = text[:100]
#     return [
#         x.text for x in NLP_DE.tokenizer(text) if x.text != " " and len(x.text) >= 1]

stoi = dict()
itos = dict()

# UNK, PAD, BOS, EOS, MASK = 0, 1, 2, 3, 4
special_tokens = ['<unk>', '<pad>', '<bos>', '<eos>', '<mask>']
for i in range(5):
    stoi[special_tokens[i]] = i
    itos[i] = special_tokens[i]

id = 5

for s in range(len(src)):
    src_tokens = src[s].strip().split()
    for t in src_tokens:
        if t not in stoi:
            stoi[t] = id
            itos[id] = t
            id += 1
            print(t, ' => ', id)

for s in range(len(trg)):
    trg_tokens = trg[s].strip().split()
    for t in trg_tokens:
        if t not in stoi:
            stoi[t] = id
            itos[id] = t
            id += 1
            print(t, ' => ', id)

with open('/data2/yzh/Dataset/Multi-30K/stoi_bpe.json', 'w') as f:
    json.dump(stoi, f)
with open('/data2/yzh/Dataset/Multi-30K/itos_bpe.json', 'w') as f:
    json.dump(itos, f)

print(len(stoi))

# src_len_dict = dict()
# trg_len_dict = dict()
#
# for i in range(len(src)):
#     len_src = len(src[i].strip().split())
#     len_trg = len(trg[i].strip().split())
#     src_len_dict[len_src] = src_len_dict.get(len_src, 0) + 1
#     trg_len_dict[len_trg] = trg_len_dict.get(len_trg, 0) + 1
#     # 按key升序打印字典
# print(sorted(src_len_dict.items(), key=lambda x: x[0]))
# print(sorted(trg_len_dict.items(), key=lambda x: x[0]))