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
threshold_value = 225
threshold, simple = cv.threshold(grey, threshold_value, 255, cv.THRESH_BINARY) # <-- image has to be grey scale
#- change the threshold value, 150, to see the effect


cv.imshow('Simple Thresholded Image', simple)


cv.waitKey(0)