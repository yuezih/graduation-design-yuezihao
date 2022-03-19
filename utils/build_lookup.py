import json
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager

with open('../../Dataset/Fashion-MMT/Clean/anno_vocab.json', 'r') as f:
    anno = json.load(f)
with open('../../Dataset/Fashion-MMT/Clean/src_word2id.json', 'r') as f:
    src_word2id = json.load(f)

manager = Manager()

trg_dict = Manager().dict()

def get_lookup_list(i):
    lookup_id_list = []
    words = list(set(anno[i]['en_words']))
    for word in words:
        if word in src_word2id:
            for id in src_word2id[word]:
                if id != i:
                    lookup_id_list.append(id)
    lookup_id_list = sorted(set(lookup_id_list), key=lookup_id_list.count, reverse=True)[:10]
    lookup_list = []
    for id in lookup_id_list:
        lookup_list.append(anno[id]['zh'])
    print(i, '\nsrc: ', anno[i]['zh'], '\nref: ', lookup_list[0])
    trg_dict[i] = lookup_list

exe_len = len(anno)

def main():
    with ProcessPoolExecutor() as executor:
        executor.map(get_lookup_list, range(exe_len))
    with open('../../Dataset/Fashion-MMT/Clean/anno_trg_vocab.json', 'w') as f:
        for i in range(exe_len):
            anno[i]['lookup'] = trg_dict[i]
            print(f'{i} saved')
        json.dump(anno, f)

if __name__ == '__main__':
    main()