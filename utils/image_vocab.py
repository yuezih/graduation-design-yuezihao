import json
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Manager

with open('../results/pretrain/word2int.json', 'r') as f:
    w2i = json.load(f)
with open('../results/pretrain/int2word.json', 'r') as f:
    i2w = json.load(f)
with open('../../Dataset/Fashion-MMT/Clean/anno_clean.json', 'r') as f:
    anno = json.load(f)
with open('../../Dataset/Fashion-MMT/Clean/word2images.json', 'r') as f:
    w2img = json.load(f)

w2img_int = {}

# w2i是一个字典，key是word，value是id
# 把img_id追加到w2i中
def img2int(i):
    img_id = anno[i]['images'][0]
    w2i[img_id] = len(w2i)
    i2w[len(w2i)-1] = img_id
    print(i, w2i[img_id], img_id)

def main():
    for i in range(len(anno)):
        img2int(i)
    with open('../../Dataset/Fashion-MMT/Clean/word2int_3.json', 'w') as f:
        json.dump(w2i, f)
    with open('../../Dataset/Fashion-MMT/Clean/int2word_3.json', 'w') as f:
        json.dump(i2w, f)
    for word in w2img:
        img_int_list = []
        for img_name in w2img[word]:
            img_int_list.append(w2i[img_name])
        w2img_int[word] = img_int_list
        print(word, img_int_list)
    with open('../../Dataset/Fashion-MMT/Clean/word2images_int.json', 'w') as f:
        json.dump(w2img_int, f)

if __name__ == '__main__':
    main()