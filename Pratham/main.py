import cv2

img = cv2.imread(r'D:\projects\AI-ML-MINI-PROJECT-2\Pratham\images\wheres_waldo.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread(r'D:\projects\AI-ML-MINI-PROJECT-2\Pratham\images\temp.jpg',0)
h ,w = template.shape

match = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.99

min_val, max_val, min_location, max_location = cv2.minMaxLoc(match)
location = max_location
font = cv2.FONT_HERSHEY_PLAIN
cv2.rectangle(img, location, (location[0] + w, location[1] + h), (0,0,255), 2)
cv2.putText(img,"Waldo Spotted.", (location[0]-40,location[1]-5),font , 1, (0,0,0),2)

cv2.imwrite('AI-ML-MINI-PROJECT-2\Pratham\grayscale.jpg',img_gray)
cv2.imshow('grayscale.jpg',img_gray)
cv2.imwrite('AI-ML-MINI-PROJECT-2\Pratham\Results.jpg',img)
cv2.imshow('Results.jpg',img)

cv2.waitKey(0)
cv2.destroyAllWindows()