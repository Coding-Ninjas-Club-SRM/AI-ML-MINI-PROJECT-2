#This project uses the Template Matching technique for object detection.
#This project involves detection of template image over base image

#Importing opencv
import cv2

#Loading base image and template image using imread()
#Simultaneously converting the loaded images into grayscale
img = cv2.imread("findhere.jpg", 0)
template = cv2.imread("waldo.png", 0)

#Resizing the base image, img, to fit the screen
#cv2.INTER_AREA is to shrink an image
resized_img = cv2.resize(img, (1000, 650), interpolation = cv2.INTER_AREA)

#Displaying the resized base image, resized_img
cv2.imshow('FindWaldo', resized_img)

#Getting the height and width of the template image
#Since the template is in grayscale, it is a 2D array having no channels.
h, w = template.shape

#Making a copy of resized_img on which a rectangle would be drawn around Waldo indicating its position
img2 = resized_img.copy()

#Performing convolution and getting a 2D array in result
#The resulting 2D array tells about how close is the match in each region of our image
#The 2D array is of the size (W-w+1, H-h+1)
result = cv2.matchTemplate(img2, template, cv2.TM_CCOEFF_NORMED)

#Finding the min and max values and locations to figure out where those areas actually are in the base image
min_val, max_val, min_location, max_location = cv2.minMaxLoc(result)

#Since we only want the location of maximum value, we can store that in another variable
location = max_location

#Getting the bottom right coordinates of the rectangle which is to be drawn around the match
#The rectangle must be of the template size
bottom_right = (location[0]+w, location[1]+h)

#Forming a black rectangle around the match
cv2.rectangle(img2, location, bottom_right, 0, 2)

#Displaying the output
cv2.imshow("Match", img2)

#Writing the GrayScale of the base image into a file
cv2.imwrite("GrayScale Base Image.png", resized_img)

#Writing the result into a file
cv2.imwrite("Found Waldo.png", img2)

#Waiting till another key is pressed
cv2.waitKey(0)

#Destroying all windows whenever any key is pressed
cv2.destroyAllWindows()