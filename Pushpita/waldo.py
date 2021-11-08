import cv2
import numpy as np
from matplotlib import pyplot as plt

#image input from user
image = cv2.imread('wheres_waldo.jpg')

#cv2.imshow('Original',image)[to display original image]

#converting image to grayscale
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#storing grayscale image 
cv2.imwrite('Grayscale.png',grayscale)
cv2.imshow('Grayscale', grayscale)


#template input from user for matching object
template = cv2.imread('mini_waldo.jpg',0)

#saves the width and height of the template into 'w' and 'h'
w, h = template.shape[::-1]

#using cv2.TM_CCOEFF_NORMED function to match pixels
res = cv2.matchTemplate(grayscale,template,cv2.TM_CCOEFF_NORMED)

threshold = 0.6
# finding the values where it exceeds the threshold
loc = np.where( res >= threshold)
#for pt in zip(*loc[::-1]): is for the points which have values greater than threshold.
# zip is a container of all such points and it will iterate to all such points and draw rectangle around this closed entity
for pt in zip(*loc[::-1]):
    #draw rectangle on places where it exceeds threshold
    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
cv2.imwrite('found_waldo.png',image)
cv2.imshow('found_waldo', image)
#to wait until any key is pressed
cv2.waitKey(0)
#Destroy all windows whenever any key is pressed
cv2.destroyAllWindows()