#imports the required libraries: opencv, numpy and matplotlib
import cv2
import numpy
from matplotlib import pyplot
#reads the image as an input from the user
img = cv2.imread(r'C:\Users\AK_Sprinkles\Desktop\wheres_waldo.jpg')
#converts the rgb image into a grayscale image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#reads the template as an input from the user
template = cv2.imread(r'C:\Users\AK_Sprinkles\Desktop\waldo.jpg',0)
#saves the width and height of the template into 'w' and 'h'
w, h = template.shape[::-1]
#matches the pixels from the given template with the image
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.6
#finds the values where it exceed the threshold
loc = numpy.where( res >= threshold)
for pt in zip(*loc[::-1]):
    #draws rectangle on places where it exceed threshold
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
#creates the output image forming a rectangle around the match
cv2.imwrite('found waldo.jpg',img)
#shows the output image forming a rectangle around the match
cv2.imshow('found waldo.jpg',img)
#creates the grayscale image
cv2.imwrite('gray image.jpg',img_gray)
#shows the grayscale image
cv2.imshow('gray image.jpg',img_gray)
#waits until any key is pressed
cv2.waitKey(0)
#destroys all windows whenever any key is pressed
cv2.destroyAllWindows()