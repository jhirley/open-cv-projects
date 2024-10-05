import cv2 as cv
import numpy as np
import os

# Get the directory of the script
script_dir = os.path.dirname(__file__)

# Move one level up
parent_dir = os.path.dirname(script_dir)

img = cv.imread(os.path.join(parent_dir,'opencv-course/Resources/Photos/park.jpg'))
# cv.imshow('Park', img)

# create blank image
blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1) # -1 fills the shape

circle = cv.circle(blank.copy(), (200,200), 200, 255, -1) # -1 fills the shape

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)


# bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
# cv.imshow('Bitwise AND', bitwise_and)

# bitwise OR
bitwise_or = cv.bitwise_or(rectangle, circle)
# cv.imshow('Bitwise OR', bitwise_or)

# bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# bitwise NOT
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise NOT', bitwise_not)

cv.imshow('Not Circle', cv.bitwise_not(circle))

cv.waitKey(0)