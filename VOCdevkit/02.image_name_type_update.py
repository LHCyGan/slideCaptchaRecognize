# -*- coding: utf-8 -*-

import os
import cv2 as cv
import numpy as np


def _image_name_type_update():
	rootdir = 'VOC2012/JPEGImages'
	lists = os.listdir(rootdir)
	for idx, _list in enumerate(lists):
		path = os.path.join(rootdir, _list)
		print(path)
		if os.path.isfile(path):
			img = cv.imdecode(np.fromfile(path, dtype=np.uint8), -1)
			cv.imwrite('VOC2012/JPEGImages/{}.jpg'.format(('000000' + str(idx + 1))[-6:]), img)


if __name__ == '__main__':
	_image_name_type_update()
