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
    lookup_list = sorted(set(lookup_list), key=lookup_list.count, reverse=True)
    # 将anno[i]['images'][0]移出lookup_list
    if anno[i]['images'][0] in lookup_list:
        lookup_list.remove(anno[i]['images'][0])
    lookup_list = [anno[i]['images'][0]] + lookup_list[:4]
    print(i, lookup_list)
    id_dict[i] = lookup_list

def main():
    with ProcessPoolExecutor() as executor:
        executor.map(get_lookup_list, range(len(anno)))
    with open('../../Dataset/Fashion-MMT/Clean/anno_clean_lookup_pro.json', 'w') as f:
        for i in range(len(anno)):
            anno[i]['lookup'] = id_dict[i]
            print(f'{i} finished')
        json.dump(anno, f)

if __name__ == '__main__':
    main()