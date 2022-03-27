import json
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager

src = open('/data2/yzh/Dataset/Multi-30K/multi30k_bpe/annotation/tst2017.en.bpe.txt', 'r', encoding='utf-8').readlines()
trn = open('/data2/yzh/Dataset/Multi-30K/multi30k_bpe/annotation/trn.en.bpe.txt', 'r', encoding='utf-8').readlines()
with open('/data2/yzh/Dataset/Multi-30K/id2tags_bpe.tst2017.json', 'r') as f:
    id2tags = json.load(f)
with open('/data2/yzh/Dataset/Multi-30K/tags2id_bpe.trn.json', 'r') as f:
    tags2id = json.load(f)

manager = Manager()

imglist_dict = manager.dict()

def get_lookup_list(i):
    lookup_id_list = []
    words = list(set(id2tags[str(i)]))
    for word in words:
        if word in tags2id:
            for id in tags2id[word]:
                lookup_id_list.append(id)
    lookup_id_list = sorted(set(lookup_id_list), key=lookup_id_list.count, reverse=True)[:10]
    print(i, '\nsrc: ', src[i], end='')
    print('ref: ', trn[lookup_id_list[0]], end='')
    imglist_dict[i] = lookup_id_list

exe_len = len(src)
# exe_len = 20

def main():
    with ProcessPoolExecutor() as executor:
        executor.map(get_lookup_list, range(exe_len))
    # for i in range(exe_len):
    #     get_lookup_list(i)
    with open('/data2/yzh/Dataset/Multi-30K/img_list_bpe.tst2017.json', 'w') as f:
        json.dump(imglist_dict._getvalue(), f)
    print('done')

if __name__ == '__main__':
    main()