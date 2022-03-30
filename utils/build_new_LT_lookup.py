import json
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager

with open('../../Dataset/Fashion-MMT/Clean/anno_vocab.json', 'r') as f:
    anno = json.load(f)
with open('../../Dataset/Fashion-MMT/Clean/src_word2id.json', 'r') as f:
    src_word2id = json.load(f)

manager = Manager()

id2ids_dict = manager.dict()
id2imgs_dict = manager.dict()

def get_lookup_list(i):
    lookup_id_list = []
    words = list(set(anno[i]['en_words']))
    for word in words:
        if word in src_word2id:
            for id in src_word2id[word]:
                if id != i:
                    lookup_id_list.append(id)
    lookup_id_list = sorted(set(lookup_id_list), key=lookup_id_list.count, reverse=True)[:10]
    lookup_id_list = [i] + lookup_id_list[:9]
    lookup_list = []
    for id in lookup_id_list:
        lookup_list.append(anno[id]['images'][0])
    print(i, '\nsrc: ', anno[i]['zh'], '\nsrc: ', anno[lookup_id_list[0]]['zh'], '\nref: ', anno[lookup_id_list[1]]['zh'])
    id2ids_dict[i] = lookup_id_list
    id2imgs_dict[i] = lookup_list

exe_len = len(anno)
# exe_len = 200

def main():
    with ProcessPoolExecutor() as executor:
        executor.map(get_lookup_list, range(exe_len))
    # for i in range(exe_len):
    #     get_lookup_list(i)
    with open('../../Dataset/Fashion-MMT/Clean/anno_new_LT.json', 'w') as f:
        for i in range(exe_len):
            anno[i]['lookup_id'] = id2ids_dict[i]
            anno[i]['lookup_img'] = id2imgs_dict[i]
            print(f'{i} saved')
        json.dump(anno, f)
    print('done')

if __name__ == '__main__':
    main()