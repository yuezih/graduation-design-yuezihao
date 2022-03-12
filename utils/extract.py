import json
from jieba import analyse
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager

with open('../../Dataset/Fashion-MMT/Clean/anno_clean.json', 'r') as f:
    anno = json.load(f)

# manager1 = Manager()
# id2words_dict = manager1.dict()
# manager2 = Manager()
# word2images_dict = manager2.dict()
zh_id2words_dict = {}
en_id2words_dict = {}
word2images_dict = {}

tfidf = analyse.extract_tags

def save_into_imgdict(zh_words, i):
    for word in zh_words:
        if word not in word2images_dict:
            word2images_dict[word] = [anno[i]['images'][0]]
        else:
            word2images_dict[word].append(anno[i]['images'][0])

def get_tags(i):
    trg_text = anno[i]['zh']
    tags_list = tfidf(trg_text)
    print(i, tags_list)
    zh_id2words_dict[i] = tags_list
    save_into_imgdict(tags_list, i)

    trg_text = anno[i]['en']
    tags_list = tfidf(trg_text)
    print(i, tags_list)
    en_id2words_dict[i] = tags_list
    save_into_imgdict(tags_list, i)

def main():
    # with ProcessPoolExecutor() as executor:
    #     executor.map(get_tags, range(10))
    for i in range(len(anno)):
        get_tags(i)
    with open('../../Dataset/Fashion-MMT/Clean/anno_vocab.json', 'w') as f:
        for i in range(len(anno)):
            anno[i]['zh_words'] = zh_id2words_dict[i]
            anno[i]['en_words'] = en_id2words_dict[i]
            print(f'{i} finished')
        json.dump(anno, f)
    with open('../../Dataset/Fashion-MMT/Clean/word2images.json', 'w') as f:
        json.dump(word2images_dict, f)

if __name__ == '__main__':
    main()