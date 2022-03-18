import json
import os

with open('../../Dataset/Fashion-MMT/Clean/anno_clean_lookup.json', 'r') as f:
    anno = json.load(f)
with open('../../Dataset/Fashion-MMT/Clean/attr_dict.json', 'r') as f:
    attr_dict = json.load(f)


def main():
    id = 39999
    print(anno[id]['zh'])
    print(anno[id]['en'])
    print(anno[id]['attr'])

    img_list = anno[id]['lookup']
    os.system('mkdir /data2/yzh/FashionMMT/driver/{}'.format(id))
    img_id = 1
    for img_name in img_list:
        img_path = '/data8/syq/FashionMMT/images/' + img_name
        new_img_path = '/data2/yzh/FashionMMT/driver/'+str(id)+'/lookup_'+str(img_id)+'.jpg'
        os.system('cp ' + img_path + ' ' + new_img_path)
        img_id += 1

    # attr_list = anno[id]['attr']
    # for attr in attr_list:
    #     lookup_id = 1
    #     if attr == 'ribbed':
    #         num = 10
    #     else:
    #         num = 5
    #     lookup_list = attr_dict[attr][:num]
    #     for lookup in lookup_list:
    #         img_path = '/data8/syq/FashionMMT/images/' + lookup
    #         new_img_path = '/data2/yzh/FashionMMT/driver/' + str(id)+ '/{}_{}.jpg'.format(attr, lookup_id)
    #         os.system('cp ' + img_path + ' ' + new_img_path)
    #         lookup_id += 1
    # print('Done')

if __name__ == '__main__':
    main()