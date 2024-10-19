import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

# Get the directory of the script
script_dir = os.path.dirname(__file__)

# Move one level up
parent_dir = os.path.dirname(script_dir)

img_path = os.path.join(parent_dir, 'opencv-course/Resources/Photos/group 1.jpg')
img = cv.imread(img_path)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

if img is None:
    print(f"Error: Unable to load image at {img_path}. Please check the file path and ensure the file exists.")
else:
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Load Haar cascade classifiers from the haarcascade subfolder
    haar_cascade_body = cv.CascadeClassifier(os.path.join(script_dir, 'haarcascade/haarcascade_fullbody.xml'))
    haar_cascade_upper_body = cv.CascadeClassifier(os.path.join(script_dir, 'haarcascade/haarcascade_upperbody.xml'))
    haar_cascade_face = cv.CascadeClassifier(os.path.join(script_dir, 'haarcascade/haarcascade_frontalface_default.xml'))
    lbp_cascade_face = cv.CascadeClassifier(os.path.join(script_dir, 'lbpcascade/lbpcascade_frontalface_improved.xml'))

    # Check if the classifiers are loaded properly
    if haar_cascade_body.empty() or haar_cascade_upper_body.empty() or haar_cascade_face.empty() or lbp_cascade_face.empty():
        print("Error: One or more Haar cascade files could not be loaded. Please check the file paths.")
    else:
        # Detect bodies and faces
        body_rect = haar_cascade_body.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
        upper_body_rect = haar_cascade_upper_body.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)
        faces_rect = haar_cascade_face.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)
        faces_rect2 = lbp_cascade_face.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

        print(f'Number of bodies found = {len(body_rect)}')
        print(f'Number of upper bodies found = {len(upper_body_rect)}')
        print(f'Number of faces found = {len(faces_rect)}')
        print(f'Number of faces found = {len(faces_rect2)}')

        # Optionally, draw rectangles around detected bodies and faces
        for (x, y, w, h) in body_rect:
            cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        for (x, y, w, h) in upper_body_rect:
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        for (x, y, w, h) in faces_rect:
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        for (x, y, w, h) in faces_rect2:
            cv.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

        # Display the result
        cv.imshow('Detected Bodies and Faces', img)
        cv.waitKey(0)
        cv.destroyAllWindows()