import cv2 as cv
import numpy as np
import os

# Get the directory of the script
script_dir = os.path.dirname(__file__)

# Move one level up
parent_dir = os.path.dirname(script_dir)

people = []
DIR = os.path.join(parent_dir, 'opencv-course/Resources/Faces/train/')

for i in os.listdir(DIR):
    people.append(i)

# create haar cascade 
haar_cascade_face = cv.CascadeClassifier(os.path.join(script_dir, 'haarcascade/haarcascade_frontalface_default.xml'))
features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yaml')

# List of image paths
image_paths = [
    'opencv-course/Resources/Faces/val/ben_afflek/1.jpg',
    'opencv-course/Resources/Faces/val/elton_john/1.jpg',
    'opencv-course/Resources/Faces/val/jerry_seinfeld/1.jpg',
    'opencv-course/Resources/Faces/val/madonna/2.jpg',
    'opencv-course/Resources/Faces/val/mindy_kaling/1.jpg'
]

# Load images
img = [cv.imread(os.path.join(parent_dir, path)) for path in image_paths]

# Check if images are loaded correctly
for i, image in enumerate(img):
    if image is None:
        print(f"Error: Unable to load image at {image_paths[i]}. Please check the file path and ensure the file exists.")
        exit(1)

# Convert images to grayscale
grey = [cv.cvtColor(image, cv.COLOR_BGR2GRAY) for image in img]

# Display the first grayscale image
cv.imshow('Person', grey[0])

# Detect the face in the images
for i in range(len(img)):
    # Detect the face in the image
    face_rect = haar_cascade_face.detectMultiScale(grey[i], scaleFactor=1.1, minNeighbors=4)
    for (x, y, w, h) in face_rect:
        face_roi = grey[i][y:y+h, x:x+w]

        # Predict the face
        label, confidence = face_recognizer.predict(face_roi)
        print(f'Label = {people[label]} with a confidence of {confidence}')

        cv.putText(img[i], f'{str(people[label])} {confidence}', (20, 20), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), thickness=2)
        cv.rectangle(img[i], (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

# Display the results
for i in range(len(img)):
    cv.imshow(f'Person {i}', img[i])

cv.waitKey(0)
cv.destroyAllWindows()