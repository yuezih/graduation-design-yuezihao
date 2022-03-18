import json
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager

with open('../../Dataset/Fashion-MMT/Clean/anno_clean.json', 'r') as f:
    anno = json.load(f)

def main():
    cnt = 0
    for i in range(len(anno)):
        i_cnt = len(anno[i]['images']) if len(anno[i]['images']) < 5 else 5
        cnt += i_cnt
    print(cnt, len(anno))
    print(cnt / len(anno))

if __name__ == '__main__':
    main()

# with open('../../Dataset/Fashion-MMT/Clean/anno_trg_vocab.json', 'r') as f:
#     anno = json.load(f)
#
# for i in range(len(anno)):
#     if anno[i]['split'] == 'tst':
#         print('=====================')
#         print('zh :\t', anno[i]['zh'])
#         print('Ref_1 :\t', anno[i]['lookup'][0])
#         print('Ref_2 :\t', anno[i]['lookup'][1])
#         print('Ref_3 :\t', anno[i]['lookup'][2])