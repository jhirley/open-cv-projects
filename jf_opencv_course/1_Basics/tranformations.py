import cv2 as cv
import numpy as np
import os

# Get the directory of the script
script_dir = os.path.dirname(__file__)

# Move one level up
parent_dir = os.path.dirname(script_dir)

img = cv.imread(os.path.join(parent_dir,'opencv-course/Resources/Photos/park.jpg'))
cv.imshow('Park', img)

#translation
def translate (img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions) 
# -x --> left , +x --> right
# -y --> up , +y --> downlilinll

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

# rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

# -angle --> clockwise, +angle --> counter clockwise
rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)
cv.imshow('Rotated 90', rotate(img, -90))


rotated_rotated = rotate(rotated, -45)
cv.imshow('Rotated Rotated', rotated_rotated)

# resizing
factor = 0.5                                                                                                                                                                  
resized = cv.resize(img, (int(img.shape[1]*factor) ,int(img.shape[0]*factor)), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#flipping
flip = cv.flip(img, 0)
# 0 --> flip vertically, 1 --> flip horizontally, -1 --> flip both vertically and horizontally
cv.imshow('Flip', flip)

#cropping
cropped = flip[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)