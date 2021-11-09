# Object Dection Project Using OpenCV 
<div align="center">
  <img alt="Where's Waldo!" src="images/wheres-waldo-logo.jpg" height="56" />
</div>
> Importing OpenCV
```
import cv2 as cv
```

```

img = cv.imread(r'D:\projects\AI-ML-MINI-PROJECT-2\Pratham\images\wheres_waldo.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
template = cv.imread(r'D:\projects\AI-ML-MINI-PROJECT-2\Pratham\images\temp.jpg',0)
h ,w = template.shape

match = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.99

min_val, max_val, min_location, max_location = cv.minMaxLoc(match)
location = max_location
font = cv.FONT_HERSHEY_PLAIN
cv.rectangle(img, location, (location[0] + w, location[1] + h), (0,0,255), 2)
cv.putText(img,"Waldo Spotted.", (location[0]-40,location[1]-5),font , 1, (0,0,0),2)

cv.imwrite('AI-ML-MINI-PROJECT-2\Pratham\grayscale.jpg',img_gray)
cv.imshow('grayscale.jpg',img_gray)
cv.imwrite('AI-ML-MINI-PROJECT-2\Pratham\Results.jpg',img)
cv.imshow('Results.jpg',img)

cv.waitKey(0)
cv.destroyAllWindows()

```

