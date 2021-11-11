import cv2
import numpy as np
img_rgb = cv2.imread('wheres_waldo.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('waldo.png',0)

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.6
w, h = template.shape[::-1]
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
cv2.imwrite('found_waldo.png',img_rgb)

import cv2
import numpy as np
from matplotlib import pyplot as plt
img_rgb = cv2.imread('find_waldo.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('waldo.png',0)

w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.6

loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
cv2.imwrite('found_waldo.png',img_rgb)