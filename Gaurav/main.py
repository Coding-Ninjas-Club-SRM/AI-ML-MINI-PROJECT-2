from cv2 import cv2

img = cv2.imread('pics/wheres_waldo.jpeg', 0)
img2 = cv2.imread('pics/wheres_waldo.jpeg', 1)
template = cv2.imread('pics/Waldo.png', 0)
h, w = template.shape

result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
location = max_loc
bottom_right = (location[0] + w, location[1] + h)

cv2.rectangle(img2, location, bottom_right, 255, 2)
cv2.imshow('Match', img2)
cv2.imwrite('found.png', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
