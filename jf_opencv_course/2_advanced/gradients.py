import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

# Get the directory of the script
script_dir = os.path.dirname(__file__)

# Move one level up
parent_dir = os.path.dirname(script_dir)

img = cv.imread(os.path.join(parent_dir,'opencv-course/Resources/Photos/cats.jpg'))
cv.imshow('cats', img)


grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', grey)

# Laplacian
lap = cv.Laplacian(grey, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# sobel gradient magnitude representation

sobelx = cv.Sobel(grey, cv.CV_64F, 1, 0)
sobely = cv.Sobel(grey, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(grey, 150, 175)
cv.imshow('Canny', canny)
cv.waitKey(0)

# 2:19:00