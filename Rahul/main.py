# importing opencv module
import cv2 

# reading the base image
img=cv2.imread("wheres_waldo.jpg")

# converting base image to grayscale and saving it
grey=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imwrite('Wheres_waldo_grayscale.jpg',grey)

# reading the template converting it to grayscale and getting its height and width
temp=cv2.imread("template .jpg")
temp=cv2.cvtColor(temp,cv2.COLOR_RGB2GRAY)
h,w =temp.shape

# making a copy of the base image
final=img.copy()

# matching template with the base image
res=cv2.matchTemplate(grey,temp,cv2.TM_CCOEFF_NORMED)

# getting location of template in base image
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
vertex=max_loc

# making a rectangle around the template that was found in base image
cv2.rectangle(final,vertex,(vertex[0]+w,vertex[1]+h),(0,255,0),2)

# saving the image with the location of template and displaying it on a seperate window
cv2.imwrite('WALDO_FOUND.jpg',final)
cv2.imshow('FOUND',final)

# waiting for a key press to destroy the window created by imshow
cv2.waitKey(0)
cv2.destroyAllWindows()


###################DEFINITIONS###############################

# imread= to read images
# imwrite= to save image
# imshow= to display the img in a seprate window
# cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)= to convert a color img to grayscale
# temp.shape= to find width height and channels (like 3 for rgb) in the format (h,w,channels)
# img.copy()= to make a duplicate of an img 
# cv2.matchTemplate(grey,temp,cv2.TM_CCOEFF_NORMED)= to match two images (cv2.TM_CCOEFF_NORMED is the method used)
# cv2.minMaxLoc()= it gives the vertex values of template in main img
# cv2.rectangle()= is used to make a rectangle taking inputs in form (image,pt1,pt2,color,thickness)
# cv2.waitkey()= waiting for a key press
# cv2.destroyAllWindows()= to destroy the window created by imshow