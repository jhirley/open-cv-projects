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

# create a list of features and labels
features = []
labels = []

def create_train():

    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img = cv.imread(img_path)
            grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            # cv.imshow('Training on image...', img)
            # cv.waitKey(100)

            face_rect = haar_cascade_face.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in face_rect:
                face_roi = grey[y:y+h, x:x+w]
                features.append(face_roi)
                labels.append(label)

create_train()

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the recognizer on the features list and the labels list
features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer.train(features, labels)
print('Training done ---------------')

print(f'Length of features = {len(features)}')
print(f'Length of labels = {len(labels)}')

# Save the features as a numpy array
np.save( 'features.npy', features)
np.save( 'labels.npy', labels)

face_recognizer.save('face_trained.yml')
print('Training done ---------------')