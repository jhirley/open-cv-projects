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

# draw a bird house
# draw a rectangle
cv.rectangle(blank, (100,100), (400,400), (0,0,255), thickness=cv.FILLED)

# draw a triangle
cv.line(blank, (50,100), (250,50), (255,255,255), thickness=2)

cv.line(blank, (250,50), (450,100), (255,255,255), thickness=2)

cv.line(blank, (50,100), (450,100), (255,255,255), thickness=2)

cv.line(blank, (100,100), (100,400), (255,255,255), thickness=2)

cv.line(blank, (100,400), (400,400), (255,255,255), thickness=2)

cv.line(blank, (400,100), (400,400), (255,255,255), thickness=2)

# draw a circle

cv.circle(blank, (250,250), 50, (255,255,255), thickness=cv.FILLED)

# write text
cv.putText(blank, 'Bird House', (150,450), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)



cv.imshow('Green with red square', blank)

cv.waitKey(0)
