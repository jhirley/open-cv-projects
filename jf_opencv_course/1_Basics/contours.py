import cv2 as cv
import numpy as np
import os

# Get the directory of the script
script_dir = os.path.dirname(__file__)

# Move one level up
parent_dir = os.path.dirname(script_dir)

img = cv.imread(os.path.join(parent_dir,'opencv-course/Resources/Photos/park.jpg'))
# cv.imshow('Park', img)

# create a blank image
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# convert to grayscale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Grey Park', grey)

# blur an image
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)

# canny edge detection
canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)

# thesholding
ret, thresh = cv.threshold(grey, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

# find contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)