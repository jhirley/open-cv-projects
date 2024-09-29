
# https://www.youtube.com/watch?v=oXlwWbU8l2o
# https://github.com/jasmcaus/opencv-course/tree/master/Resources/Photos
# https://github.com/jasmcaus/caer


import cv2 as cv
import os

# Get the directory of the script
script_dir = os.path.dirname(__file__)

# Move one level up
parent_dir = os.path.dirname(script_dir)




def rescale_frame(frame, scale=0.75):
    # Images, Videos, and Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # Only live videos
    capture.set(3, width)
    capture.set(4, height)


# image example

# Construct the relative path from the parent directory
relative_path = 'opencv-course/Resources/Photos/cat.jpg'
img_path = os.path.join(parent_dir, relative_path)

img = cv.imread(img_path)

resize_image = rescale_frame(img, scale=0.5)

cv.imshow('Cat', resize_image )

resize_image2 = rescale_frame(img, scale=.25)
                              
cv.imshow('Cat2', resize_image2)
                              



# video example
relative_path = 'opencv-course/Resources/Videos/dog.mp4'
path = os.path.join(parent_dir, relative_path)

capture = cv.VideoCapture(path)
# capture = cv.VideoCapture(0) # <- This is for the first camera
# capture = cv.VideoCapture(1) # <- This is for the second camera

# Check if the image was loaded successfully
if capture is None:
    print(f"Error: Unable to load image at {path}. Please check the file path and ensure the file exists.")


while True:
    isTrue, frame = capture.read()

    frame_resized = rescale_frame(frame, scale=0.75)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()