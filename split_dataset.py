import os
import glob
import numpy as np
import shutil
from sklearn.model_selection import train_test_split


def copy_to_target_path(fname_list, source_path, target_path, mode):
    for fname in fname_list:
        data_source_path = os.path.join(source_path, 'JPEGImages', fname+'.jpg')
        data_target_path = os.path.join(target_path, 'images', mode, fname+'.jpg')
        shutil.copyfile(data_source_path, data_target_path)

        label_source_path = os.path.join(source_path, 'Annotations', fname+'.txt')
        if os.path.exists(label_source_path):
            label_target_path = os.path.join(target_path, 'labels', mode, fname+'.txt')
            shutil.copyfile(label_source_path, label_target_path)


def split_train_val_test(source_path, target_path, split_rate):
    data_fname_list = os.listdir(os.path.join(source_path, 'JPEGImages'))               # 图片名称列表
    np.random.seed(100)                                                                 # 设定随机数种子
    length = len(data_fname_list)                                                       # 数据数量
    shuffled_indices = np.random.permutation(length)                                    # 随机索引

    train_size = int(length * split_rate[0])                                            # 训练集大小
    val_size = int(length * split_rate[1])                                              # 验证集大小

    train_indices = shuffled_indices[:train_size]                                       # 训练集索引
    val_indices = shuffled_indices[train_size:train_size+val_size]                      # 验证集索引
    test_indices = shuffled_indices[train_size+val_size:]                               # 测试集索引

    train_fname_list = [data_fname_list[idx].split('.')[0] for idx in train_indices]    # 训练集名称列表
    val_fname_list = [data_fname_list[idx].split('.')[0] for idx in val_indices]        # 验证集名称列表
    test_fname_list = [data_fname_list[idx].split('.')[0] for idx in test_indices]      # 测试集名称列表

    copy_to_target_path(train_fname_list, source_path, target_path, 'train')            # 拷贝训练集到目标路径
    print('Successfully generate train data!\n')
    copy_to_target_path(val_fname_list, source_path, target_path, 'val')                # 拷贝验证集到目标路径
    print('Successfully generate val data!\n')
    copy_to_target_path(test_fname_list, source_path, target_path, 'test')              # 拷贝测试集到目标路径
    print('Successfully generate test data!\n')

 
if __name__ == '__main__':
    source_path = 'D:\\Data\\UAV\\Ji-Wei Highway\\Labeled Images\\'                     # 初始路径
    target_path = 'D:\\Projects\\YOLOv5\\dataset\\'                                     # 目标路径

    os.makedirs(target_path, exist_ok=True)
    if os.listdir(target_path):
        shutil.rmtree(target_path)
        os.mkdir(target_path)
    
    # 创建数据集图片与标签目标路径
    os.makedirs(os.path.join(target_path, 'images', 'train'), exist_ok=True)
    os.makedirs(os.path.join(target_path, 'images', 'val'), exist_ok=True)
    os.makedirs(os.path.join(target_path, 'images', 'test'), exist_ok=True)
    os.makedirs(os.path.join(target_path, 'labels', 'train'), exist_ok=True)
    os.makedirs(os.path.join(target_path, 'labels', 'val'), exist_ok=True)
    os.makedirs(os.path.join(target_path, 'labels', 'test'), exist_ok=True)

    split_rate = [0.6, 0.2, 0.2]                                                        # 数据集划分比例

    split_train_val_test(source_path, target_path, split_rate)