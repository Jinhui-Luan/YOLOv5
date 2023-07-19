import os
import cv2
import json
import numpy as np
 
 
def txt_write(x,img_x,img_y,txt):
    data = x['points']
    n = 1
    for x in data:
        for i in x:
            if n % 2 == 0:
                txt.write(' ' + str(round(i/img_x,6)))
                n += 1
            else:
                txt.write(' ' + str(round(i/img_y,6)))
                n += 1  
    txt.write('\n') 
 
 
def json2txt(json_path,save_path):
    txt = open(save_path,'w')
    with open(json_path, "r") as f:
        data = f.read()
    data = json.loads(data)
    img_x = data['imageHeight']
    img_y = data['imageWidth']
    shapes = data['shapes']
 
    for x in shapes:
        #print(x['label'])
        #此处面向不同分类，需要改动下面的标签值，如果是多分类，那么需要增加新的if
        #只是单分类的话，可以直接去掉if，把里面的模块拿出来用
 
        if x['label']=='pier stud':
            txt.write('0') 
            txt_write(x,img_x,img_y,txt)
        elif x['label']=='bent cap':
            txt.write('1') 
            txt_write(x,img_x,img_y,txt)
        elif x['label']=='beam hoisting':
            txt.write('2') 
            txt_write(x,img_x,img_y,txt)   
        elif x['label']=='else':
            txt.write('3') 
            txt_write(x,img_x,img_y,txt)
        elif x['label']=='bridge start':
            txt.write('4') 
            txt_write(x,img_x,img_y,txt)
    txt.close()
    
#单文件测试
# save_dir = "/workspace/" #文件路径
# name = 'test'
# save_path = save_dir + name + '.txt' # 也可以是.doc
# json_path = '/json/65161.json'
# json2txt(json_path,save_path)
 
#文件夹
json_dir = 'D:\\Data\\UAV\\Ji-Wei Highway\\Temp\\JSONAnnotations\\'
save_dir = 'D:\\Data\\UAV\\Ji-Wei Highway\\Temp\\TXTAnnotations\\'
files = os.listdir(json_dir)
os.makedirs(save_dir, exist_ok=True)
num = 1
for file in files :
    name = file.split('/')[-1].split('.')[0]
    print(file)
    json_path = json_dir + '/' + name + '.json'
    save_path = save_dir + '/' + name + '.txt'
    json2txt(json_path,save_path)
    print(num,'/',len(files),':',name)
    num += 1