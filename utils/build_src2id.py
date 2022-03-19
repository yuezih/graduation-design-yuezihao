import json

import numpy as np

name = np.load('../../Dataset/Fashion-MMT/public_split/trn_ids.npy', 'r')
with open('../../Dataset/Fashion-MMT/Clean/anno_vocab.json', 'r') as f:
    anno = json.load(f)

src_word2id = {}

def main():
    for i in range(len(name)):
        anno_id = int(name[i])
        for word in anno[anno_id]['en_words']:
            if word not in src_word2id:
                src_word2id[word] = [anno_id]
            else:
                if anno_id not in src_word2id[word]:
                    src_word2id[word].append(anno_id)
    with open('../../Dataset/Fashion-MMT/Clean/src_word2id.json', 'w') as f:
        json.dump(src_word2id, f)

if __name__ == '__main__':
    main()