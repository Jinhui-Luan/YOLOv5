# coding=utf-8
# 使用OpenCV视频中提取帧图片并保存(cv2.VideoCapture)
import os
import glob
import cv2
import shutil


def extract_frames(video_path, extract_folder, frame_rate):
    video_name = video_path.split('\\')[-1].split('.')[0]                                           # 视频名称
    print('Start to extract frames for {}.mp4.\n'.format(video_name))
    os.makedirs(extract_folder, exist_ok=True)

    video = cv2.VideoCapture(video_path)
    index = 1                                                                                       # 读取视频帧数
    count = 0                                                                                       # 提取视频帧数

    # 遍历视频中的所有帧
    while True:
        retval, frame = video.read()                                                                # 逐帧读取视频

        if retval:
            # 按照设置的频率保存图片
            if index % frame_rate == 0:
                print('Extracting the No.{} frame in {}.mp4!\n'.format(str(index), video_name))
                extract_path = os.path.join(extract_folder, '{}-{:04d}.jpg'.format(video_name, index))
                if os.path.exists(extract_path):
                    print('Already extracted.')
                    index += 1 
                    continue
                cv2.imwrite(extract_path, frame)
                count += 1                                                                          # 提取视频帧数 + 1
                # cv2.waitKey(0)
            index += 1                                                                              # 读取视频帧数 + 1
        else:
            print('Successfully extracted {} frames from total {} frames.\n'.format(count, index))
            break

    video.release()                                                                                 # 释放掉实例化的视频


def main():
    video_path_list = glob.glob(os.path.join('D:\\Data\\UAV\\Ji-Wei Highway\\Videos', '*cut.mp4'))  # 视频路径列表
    video_path_list.sort()
    # print(video_path_list)
    extract_folder = 'D:\\Data\\Uav\\Ji-Wei Highway\\Images'                                        # 存放提取视频帧的位置
    frame_rate = 100                                                                                # 帧提取频率

    for video_path in video_path_list:
        extract_frames(video_path, extract_folder, frame_rate)                                      # 提取帧图片，并保存到指定路径


if __name__ == '__main__':
    main()
