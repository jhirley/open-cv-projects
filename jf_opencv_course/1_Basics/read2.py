# https://www.youtube.com/watch?v=oXlwWbU8l2o
# https://github.com/jasmcaus/opencv-course/tree/master/Resources/Photos
# https://github.com/jasmcaus/caer

import cv2 as cv
import os

def get_available_cameras():
    """
    https://medium.com/@saicoumar/how-to-use-a-smartphone-as-a-webcam-with-opencv-b68773db9ddd
    get_available_cameras() -> List
    """
    available_cameras = []
    # Check for 5 cameras 
    for i in range(5):
        cap = cv.VideoCapture(i)
        if cap.isOpened():
            available_cameras.append(i)
            cap.release()
    return available_cameras

cameras = get_available_cameras()
if cameras:
    print("Available Cameras:", cameras)
else:
    print("No cameras found.")

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

# img_path = 'jf_opencv_course/opencv-course/Resources/Photos/cat_large.jpg'
img = cv.imread(img_path)


path = os.path.join(parent_dir,'opencv-course/Resources/Videos/dog.mp4')


get_available_cameras()

# capture = cv.VideoCapture(path)
capture = cv.VideoCapture(0) # <- This is for the first camera
# capture = cv.VideoCapture(1) # <- This is for the second camera
# capture = cv.VideoCapture(2) # <- This is for the iphone camera
# capture = cv.VideoCapture('https://10.4.4.238:4747/video')


# Check if the image was loaded successfully
if capture is None:
    print(f"Error: Unable to load image at {path}. Please check the file path and ensure the file exists.")


while True:
    isTrue, frame = capture.read()

    blur = cv.GaussianBlur(frame, (15,15), cv.BORDER_DEFAULT)
    # cv.imshow('Video', frame)
    cv.imshow('Video', blur)

    canny = cv.Canny(frame, 125, 175)
    cv.imshow('Canny', canny)

    grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('Grey', grey)

    # thesholding
    ret, thresh = cv.threshold(grey, 125, 255, cv.THRESH_BINARY)
    cv.imshow('Thresh', thresh)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
