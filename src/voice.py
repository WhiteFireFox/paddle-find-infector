import os
import cv2
import glob
import matplotlib.pyplot as plt

# 图片合成视频
def GetVideo(path):
    img = cv2.imread('/home/aistudio/img/0.jpg')
    size = (img.shape[1], img.shape[0])

    fps = 10  # 一秒写10张图片 
    video_path = '/home/aistudio/train.mp4'  # 导出路径
    video = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc('D', 'I', 'V', 'X'), fps, size)
    for i in range(len(glob.glob(pathname=path+'*.jpg'))):
        item = path + str(i) + '.jpg' 
        img = cv2.imread(item)
        video.write(img)  # 写入视频
    video.release()

# 查看效果
img = cv2.imread('img/145.jpg')
%matplotlib inline
plt.imshow(img)
plt.show()

# 合成
GetVideo('/home/aistudio/img/')
