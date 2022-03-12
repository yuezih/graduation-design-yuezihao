'''
从anno_test.json文件中读取数据，数据格式如下：
[
    {
        "id": integer,
        "en": string,
        "zh": string,
        "images": list of strings,
        "category": string,
        "attr": list of strings,
        "split": string
    },
]
建立一个数据类，包含id，en，zh，images，category，attr，split
建立一个数据集类，包含数据类的列表
'''

import json

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

class Data:
    def __init__(self, id, en, zh, images, category, attr, split):
        self.id = id
        self.en = en
        self.zh = zh
        self.images = images
        self.category = category
        self.attr = attr
        self.split = split

def get_data(data):
    data_list = []
    for d in data:
        data_list.append(Data(d['id'], d['en'], d['zh'], d['images'][0], d['category'], d['attr'], d['split']))
    return data_list


def main():
    data = load_data('anno_clean.json')
    data_list = get_data(data)
    # 用所有数据构建一个字典，key为attr，value为images
    attr_dict = {}
    for d in data_list:
        for attr in d.attr:
            if attr not in attr_dict:
                attr_dict[attr] = []
            attr_dict[attr].append(d.images)
    # 将字典保存为json文件
    with open('attr_dict.json', 'w', encoding='utf-8') as f:
        json.dump(attr_dict, f)

if __name__ == '__main__':
    main()