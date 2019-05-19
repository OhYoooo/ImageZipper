import cv2
from re import match
from re import I as flag
from os import listdir

def resize(image, width=1200):
	power = width * 1.0 / image.shape[1]
	dim = (width, int(image.shape[0] * power))
	out = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
	return out

def zip(filepath):
	targetWidth = 1366
	image = cv2.imread(filepath)
	if image.shape[0] > targetWidth:
		image = resize(image=image, width = targetWidth)
	cv2.imwrite("{}.jpg".format(filepath), image)

for filename in listdir(dirpath):
	ans = match("^(.*)[.]((png)|(bmp)|(jpg)|(jpeg))$", filename, flag)
	if ans is not None:
		print (filename)
		zip("{}/{}".format(".", filename))