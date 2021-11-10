# -*- coding: utf-8 -*-
"""Waldo_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/148gGJXWrLbgBlm0v2WGBHgFthix8THTL
"""

# Commented out IPython magic to ensure Python compatibility.
#import the required libraries
import cv2
import matplotlib.pyplot
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
# %matplotlib inline
from cv2 import matchTemplate
from cv2 import minMaxLoc

from google.colab.patches import cv2_imshow

#Opening and converting to grayscale
src = cv2.imread("/content/wheres_waldo.jpg")
src = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
Temp = cv2.imread("/content/waldo.png") 
temp = cv2.cvtColor(Temp, cv2.COLOR_RGB2GRAY) 
plt.imshow(src, cmap='gray')

#As we can note the grayscale image possess a 2D Array
print(src)

plt.imshow(temp, cmap='gray')

#Assigning height width variables to source image
height, width =src.shape
height, width

#Assigning height width variables to walo's Template image
H, W = temp.shape
H, W

methods = [cv2.TM_CCOEFF_NORMED]

for method in methods:
    src2 = src.copy()
    result = cv2.matchTemplate(src2, temp, method)#matches the pixels from the given template with the image
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)#assigning and printing out image threshs
    print(min_loc, max_loc)
    bottom_right = (location[0] + W, location[1] + H)
    cv2.rectangle(src2, location,bottom_right, 255, 5)
    cv2_imshow(src2)#shows the output image forming a rectangle around the match
    cv2.waitKey(0)
    cv2.destroyAllWindows()

