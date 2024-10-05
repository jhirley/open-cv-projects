import cv2 as cv
import numpy as np
import os

# Get the directory of the script
script_dir = os.path.dirname(__file__)

# Move one level up
parent_dir = os.path.dirname(script_dir)

img = cv.imread(os.path.join(parent_dir,'opencv-course/Resources/Photos/park.jpg'))
cv.imshow('Park', img)

# averaging
average = cv.blur(img, (7,7))

# Gaussian blur
gauss = cv.GaussianBlur(img, (7,7), 0)

# median blur
median = cv.medianBlur(img, 7)

# bilateral blur
bilateral = cv.bilateralFilter(img, 10, 35, 25)

# show the images
cv.imshow('Average Blur', average)
cv.imshow('Gaussian Blur', gauss)
cv.imshow('Median Blur', median)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)