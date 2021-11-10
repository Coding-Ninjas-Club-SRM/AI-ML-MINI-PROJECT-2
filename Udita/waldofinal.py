import cv2
import numpy as np
img=cv2.imread('waldo.jpg')
template=cv2.imread('waldotemp.jpg',0)
grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
result=cv2.matchTemplate(grey_img,template,cv2.TM_CCOEFF_NORMED)
width,height=template.shape[:: -1]
limit = 0.9
location=np.where(result>=limit)
print(location)
for point in zip(*location[::-1]):
    cv2.rectangle(img,point,(point[0]+width,point[1]+height),(0,0,275),4)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows