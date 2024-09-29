import cv2 as cv
import numpy as np
import os

# Get the directory of the script
script_dir = os.path.dirname(__file__)

# Move one level up
parent_dir = os.path.dirname(script_dir)



blank = np.zeros((500, 500,3), dtype='uint8')
# blank = np.zeros((500, 500), dtype='uint8')
# 
# cv.imshow('Blankety blank blank blank', blank)
# img = cv.imread(os.path.join(parent_dir,'opencv-course/Resources/Photos/cat.jpg'))
# cv.imshow('Cat', img)

# 1. paint the image a certain color
blank[:] = 0, 255, 0 # Blue, Green, Red

blank[200:300, 300:400] = 0, 0, 255 # add a red square
# draw a rectangle
# cv.rectangle(blank, (10,10), (250,250), (255,0,0), thickness=2) # thickness=cv.FILLED)

cv.rectangle(blank, (10,10), (blank.shape[1]//2,blank.shape[0]//2), (255,0,0), thickness=2) # thickness=cv.FILLED)

# draw a circle
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,255), thickness=3)
cv.circle(blank, (blank.shape[1]//3,blank.shape[0]//3), 20, (255,0,255), thickness=cv.FILLED)

# draw a line
cv.line(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (255,255,255), thickness=3)

# write text
cv.putText(blank, 'Hello, my name is J!', (35,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)

cv.imshow('Green with red square', blank)

cv.waitKey(0)
