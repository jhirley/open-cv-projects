import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

# Get the directory of the script
script_dir = os.path.dirname(__file__)

# Move one level up
parent_dir = os.path.dirname(script_dir)

img = cv.imread(os.path.join(parent_dir,'opencv-course/Resources/Photos/cats.jpg'))
cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')  

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Grey', grey)

# grayscale histogram
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Mask', masked)

# histogram
# grey_hist = cv.calcHist([grey], [0], mask, [256], [0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
# plt.plot(img) # plot the histogram
plt.xlim([0,256])

#color histogram

colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])
plt.show()


cv.waitKey(0)