import json
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager

with open('../../Dataset/Fashion-MMT/Clean/anno_vocab.json', 'r') as f:
    anno = json.load(f)
with open('../../Dataset/Fashion-MMT/Clean/src_word2id.json', 'r') as f:
    src_word2id = json.load(f)

manager = Manager()

trg_dict = {}

def get_lookup_list(i):
    lookup_list = []
    words = list(set(anno[i]['en_words']))
    for word in words:
        for id in src_word2id[word]:
            if id != i:
                lookup_list.append(anno[id]['zh'])
    lookup_list = sorted(set(lookup_list), key=lookup_list.count, reverse=True)
    lookup_list = lookup_list[:10]
    print(i, anno[i]['zh'], lookup_list[0])
    trg_dict[i] = lookup_list

def main():
    with ProcessPoolExecutor(max_workers=40) as executor:
        executor.map(get_lookup_list, range(len(anno)))
    # for i in range(10):
    #     get_lookup_list(i)
    with open('../../Dataset/Fashion-MMT/Clean/anno_trg_vocab.json', 'w') as f:
        for i in range(len(anno)):
            anno[i]['lookup'] = trg_dict[i]
            print(f'{i} finished')
        json.dump(anno, f)

if __name__ == '__main__':
    main()