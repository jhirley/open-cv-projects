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

# simple thresholding
threshold_value = 150
threshold, simple = cv.threshold(grey, threshold_value, 255, cv.THRESH_BINARY) # <-- image has to be grey scale
#- change the threshold value, 150, to see the effect

threshold, simple_inv = cv.threshold(grey, threshold_value, 255, cv.THRESH_BINARY_INV) # <-- image has to be grey scale
#- change the threshold value, 150, to see the effect
cv.imshow('Simple Inverse Thresholded Image', simple_inv)
cv.imshow('Simple Thresholded Image', simple)

# Adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(grey, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

adaptive_thresh_gaussian = cv.adaptiveThreshold(grey, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow('Adaptive Thresholding Gaussian', adaptive_thresh_gaussian)

cv.waitKey(0)

# 2:19:00