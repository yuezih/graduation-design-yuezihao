import json
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager

with open('../../Dataset/Fashion-MMT/Clean/anno_vocab.json', 'r') as f:
    anno = json.load(f)
with open('../../Dataset/Fashion-MMT/Clean/word2images_int.json', 'r') as f:
    word2images_dict = json.load(f)

manager = Manager()
id_dict = manager.dict()

def get_lookup_list(i):
    lookup_list = []
    words = list(set(anno[i]['zh_words'] + anno[i]['en_words']))
    for word in words:
        lookup_list += word2images_dict[word]
    lookup_list = sorted(set(lookup_list), key=lookup_list.count, reverse=True)
    lookup_list = lookup_list[:20]
    print(i, lookup_list)
    id_dict[i] = lookup_list

def main():
    with ProcessPoolExecutor() as executor:
        executor.map(get_lookup_list, range(len(anno)))
    with open('../../Dataset/Fashion-MMT/Clean/anno_vocab_lookup.json', 'w') as f:
        for i in range(len(anno)):
            anno[i]['lookup'] = id_dict[i]
            print(f'{i} finished')
        json.dump(anno, f)

if __name__ == '__main__':
    main()