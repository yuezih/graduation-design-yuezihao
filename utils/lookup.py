import json
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager

with open('../../Dataset/Fashion-MMT/Clean/anno_clean.json', 'r') as f:
    anno = json.load(f)
with open('../../Dataset/Fashion-MMT/Clean/attr_dict.json', 'r') as f:
    attr_dict = json.load(f)

manager = Manager()
id_dict = manager.dict()

def get_lookup_list(i):
    lookup_list = []
    for attr in anno[i]['attr']:
        lookup_list += attr_dict[attr]
    # 保留lookup_list中出现频率最高的5个值
    lookup_list = sorted(lookup_list, key=lookup_list.count, reverse=True)
    lookup_list = lookup_list[:5]
    print(i, lookup_list)
    id_dict[i] = lookup_list

def main():
    with ProcessPoolExecutor() as executor:
        executor.map(get_lookup_list, range(len(anno)))
    with open('../../Dataset/Fashion-MMT/Clean/anno_clean_lookup.json', 'w') as f:
        for i in range(len(anno)):
            anno[i]['lookup'] = id_dict[i]
            print(f'{i} finished')
        json.dump(anno, f)

if __name__ == '__main__':
    main()