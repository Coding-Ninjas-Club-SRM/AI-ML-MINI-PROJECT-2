import cv2 #OpenCv Imported
import numpy as np #Numpy Imported
from matplotlib import pyplot as plt #MatplotLib Imported

rgb = cv2.imread('D:\GIT\CN\AI-ML-MINI-PROJECT-2\Astitva\wheres_waldo.jpg') #Main Image Is Read By Program
gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY) #Image Converted into Black And White (Greyscale) and Saved As gray
template = cv2.imread('D:\GIT\CN\AI-ML-MINI-PROJECT-2\Astitva\Template.jpg',0) #Template Image Is Read By The Program
w, h = template.shape[::-1] # saves the width and height of the template into 'w' and 'h'
a = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED) #Sliding The Template Image Over Main Image And Checking If The Pixles of Template Image and Main Image Matches.
threshold = 0.8#Thershold is the Match Precision (How Much The Main Image Pixel Matches With Template Image) in the Main Image
loc = np.where( a >= threshold) # finding the values where it exceeds the threshold
for pt in zip(*loc[::-1]): #for the points which have values greater than threshold.
    cv2.rectangle(rgb, pt, (pt[0] + w, pt[1] + h), (0,225,0), 2) #draw rectangle on places where it exceeds threshold
    print(pt) #for Printing The Points in the terminal where Rectangle Is Drawn
cv2.imwrite('Waldo Output.png',rgb) #Output Image Is Saved As Waldo Output.png
cv2.imwrite('Grey Scene.png',gray) #GreyScale Image Is Saved As Grey Scene.png
cv2.imshow('Waldo Output.png',rgb) #Showing Output Image
cv2.imshow('Grey Scene.png',gray) #Showing Gray Scale Image
cv2.waitKey(0) #Program Will wait till Other Key is Pressed
cv2.destroyAllWindows() #Program will kill all Windows When A Key Is Pressed