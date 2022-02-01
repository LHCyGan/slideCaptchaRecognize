'''
predict.py有几个注意点
1、如果想要保存，利用r_image.save("img.jpg")即可保存。
2、如果想要获得框的坐标，可以进入detect_image函数，读取top, left, bottom, right这四个值。
3、如果想要截取下目标，可以利用获取到的top,left,bottom,right这四个值在原图上利用矩阵的方式进行截取。
'''
import cv2
import numpy

from centernet import CenterNet
from PIL import Image

centernet = CenterNet()

path = r"D:/PyProject/CenterNet/img/1/{0}.jpg"
for i in range(1, 20):
    print(path.format(i))
    image = Image.open(path.format(i))
    image = centernet.detect_image(image)
    # image.show()
