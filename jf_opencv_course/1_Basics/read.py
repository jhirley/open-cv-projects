# https://www.youtube.com/watch?v=oXlwWbU8l2o
# https://github.com/jasmcaus/opencv-course/tree/master/Resources/Photos
# https://github.com/jasmcaus/caer

import cv2 as cv
import os

# Get the directory of the script
script_dir = os.path.dirname(__file__)

# Move one level up
parent_dir = os.path.dirname(script_dir)

# Construct the relative path from the parent directory
relative_path = 'opencv-course/Resources/Photos/cat.jpg'
img_path = os.path.join(parent_dir, relative_path)

print(f"Script directory: {script_dir}")
print(f"Parent directory: {parent_dir}")
print(f"Image path: {img_path}")


# img_path = 'jf_opencv_course/opencv-course/Resources/Photos/cat.jpg'
# img_path = '../jf_opencv_course/opencv-course/Resources/Photos/cat_large.jpg'
img = cv.imread(img_path)

# Check if the image was loaded successfully
if img is None:
    print(f"Error: Unable to load image at {img_path}. Please check the file path and ensure the file exists.")

cv.imshow('Cat', img)

cv.waitKey(0)