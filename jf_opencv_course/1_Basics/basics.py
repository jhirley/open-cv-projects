import cv2 as cv
import os

# Get the directory of the script
script_dir = os.path.dirname(__file__)

# Move one level up
parent_dir = os.path.dirname(script_dir)

img = cv.imread(os.path.join(parent_dir,'opencv-course/Resources/Photos/cat.jpg'))
park = cv.imread(os.path.join(parent_dir,'opencv-course/Resources/Photos/park.jpg'))

# convert to grayscale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# blur an image
blur = cv.GaussianBlur(park, (7,7), cv.BORDER_DEFAULT)
blur2 = cv.GaussianBlur(park, (47,47), cv.BORDER_DEFAULT)

# edge cascade
canny = cv.Canny(park, 125, 175)
cv.imshow('Canny Edges', canny)

canny_blur = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges Blur', canny_blur)

# dialate the image
dilated = cv.dilate(canny_blur, (7,7), iterations=1)
cv.imshow('Dilated', dilated)

# erode
eroded = cv.erode(dilated, (7,7), iterations=1)
cv.imshow('Eroded', eroded)

#resize
resized = cv.resize(park, (2500,2500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# crop
cropped = park[50:200, 200:400]
cv.imshow('Cropped', cropped)
# save cropped image
cv.imwrite(os.path.join(parent_dir, 'cropped_park.jpg'), cropped) 


# cv.imshow('Cat', img)
# cv.imshow('Grey Cat', grey)
# cv.imshow('Park', park)
# cv.imshow('Blur Park', blur)
# cv.imshow('Blur Park 2u', blur2)

cv.waitKey(0)