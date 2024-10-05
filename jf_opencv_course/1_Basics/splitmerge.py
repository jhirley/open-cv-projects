import cv2 as cv
import numpy as np
import os

# Get the directory of the script
script_dir = os.path.dirname(__file__)

# Move one level up
parent_dir = os.path.dirname(script_dir)

img = cv.imread(os.path.join(parent_dir,'opencv-course/Resources/Photos/park.jpg'))
cv.imshow('Park', img)

# split the image into its channels
b,g,r = cv.split(img)

# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)

# merge the back together
merged = cv.merge([b,g,r])
# cv.imshow('Merged', merged)

# blank image
blank = np.zeros(img.shape[:2], dtype='uint8')

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)


cv.waitKey(0)