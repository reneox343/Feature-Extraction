# from skimage.io import imread, imshow
from skimage.filters import prewitt_h,prewitt_v
import cv2
import pandas as pdskimage
import numpy as np
import matplotlib.pyplot as plt

"""by rene Avila,Luis Robledo and Diego iñigez"""

#read image with color
image = cv2.imread('./Graffiti/Graffiti_1.png')

def getFeaturesFromImage(image):
    #BGR order channel
    blue = 0
    green = 0
    red = 0
    grayScale = 0
    size = image.shape[0]*image.shape[1]
    for i in range(0,image.shape[0]):
        for j in range(0,image.shape[1]):
            blue += image[i,j,0]
            green += image[i,j,1]
            red += image[i,j,2]
            grayScale += (blue + red + green)/3
    blue /= size
    green /= size
    red /= size
    grayScale /= size
    #HSV
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hue = 0
    saturation = 0
    value = 0
    for i in range(0,image.shape[0]):
        for j in range(0,image.shape[1]):
            hue += hsv_img[i,j,0]
            saturation += hsv_img[i,j,1]
            value += hsv_img[i,j,2]
    hue /= size
    saturation /= size
    value /= size
    return red,green,blue,grayScale,hue,saturation,value

getFeaturesFromImage(image)