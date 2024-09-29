#! python3

import os
import argparse
import cv2
import dlib
import numpy as np

# Initialize Dlib's face detector and facial landmark predictor
base_path = "/Users/jhirleyfonte/Documents/Classwork/2024 Fall/CAI2840C-2247-12439- Introduction to Computer Visio/code/open-cv-projects/jf_1_faceswap/"
model_path = f"{base_path}models/opencv_face_detector_uint8.pb"
config_path = f"{base_path}models/opencv_face_detector.pbtxt"
detector = dlib.get_frontal_face_detector()
predictor_path = f"{base_path}models/shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(predictor_path)

def detect_landmarks(image):
    # Detect faces in the image
    dets = detector(image, 1)
    if len(dets) == 0:
        return []

    # Get the landmarks for the first detected face
    shape = predictor(image, dets[0])
    landmarks = [(p.x, p.y) for p in shape.parts()]
    return landmarks

def swap_faces(source_image, destination_image):
    source_img = cv2.imread(source_image)
    destination_img = cv2.imread(destination_image)

    
    source_gray = cv2.cvtColor(source_img, cv2.COLOR_BGR2GRAY)
    destination_gray = cv2.cvtColor(destination_img, cv2.COLOR_BGR2GRAY)
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    source_faces = face_cascade.detectMultiScale(source_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    destination_faces = face_cascade.detectMultiScale(destination_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(source_faces) == 0 or len(destination_faces) == 0:
        print("No faces detected in one or both images.")
        return None

    source_x, source_y, source_w, source_h = source_faces[0]
    destination_x, destination_y, destination_w, destination_h = destination_faces[0]

    source_roi = source_img[source_y:source_y + source_h, source_x:source_x + source_w]
    destination_roi = destination_img[destination_y:destination_y + destination_h, destination_x:destination_x + destination_w]

    # Placeholder for landmark detection
    source_points = detect_landmarks(source_roi)
    destination_points = detect_landmarks(destination_roi)


    # Check if model files exist
    if not os.path.exists(model_path):
        print(f"Error: The model file {model_path} does not exist.")
        return None
    if not os.path.exists(config_path):
        print(f"Error: The config file {config_path} does not exist.")
        return None


    net = cv2.dnn.readNetFromTensorflow(model_path, config_path)
    blob = cv2.dnn.blobFromImage(destination_roi, 1.0, (300, 300), [104, 117, 123], False)

    net.setInput(blob)
    landmarks = net.forward()

    destination_points = []
    for i in range(68):
        x = int(landmarks[0, 0, i, 0] * destination_w) + destination_x
        y = int(landmarks[0, 0, i, 1] * destination_h) + destination_y
        destination_points.append((x, y))

    
    # Debugging information
    print(f"Destination points shape: {np.array(destination_points).shape}")
    print(f"Source faces shape: {np.array(source_faces).shape}")
    print(f"Destination points: {destination_points}")
    print(f"Source faces: {source_faces}")

    # Ensure both arrays have the same number of points
    if len(destination_points) != len(source_faces):
        raise ValueError("The number of destination points and source faces do not match.")

    hull_points = cv2.convexHull(np.array(destination_points), returnPoints=True)

    mask = np.zeros(source_img.shape[:2], dtype=np.uint8)
    cv2.fillPoly(mask, [np.array(destination_points)], 255)

    transformation_matrix, _ = cv2.estimateAffinePartial2D(np.array(destination_points), np.array(source_faces)[:,:2])

    source_face_warped = cv2.warpAffine(source_roi, transformation_matrix, (destination_w, destination_h))

    destination_face_masked = cv2.bitwise_and(destination_roi, destination_roi, mask=mask)

    swapped_face = cv2.add(destination_face_masked, source_face_warped)

    destination_img[destination_y:destination_y + destination_h, destination_x:destination_x + destination_w] = swapped_face

    return destination_img

def confirm_file_exists(file_path):
    try:
        with open(file_path) as f:
            return True
    except FileNotFoundError:
        return False



def startup():
    pass



def main():
    # Add your code here
    pass


# The following resources were used to create this code: aka the goat rodeo.
# https://medium.com/@ccpvyn/creating-a-face-swapping-tool-with-opencv-and-python-4d64fc332de3
# https://pysource.com/2019/05/28/face-swapping-explained-in-8-steps-opencv-with-python/
# https://github.com/guipleite/CV2-Face-Swap
# https://daehnhardt.com/blog/2024/03/18/ai-face-swaps-open-cv-face-detection/
# https://snyk.io/advisor/python/dlib/functions/dlib.cnn_face_detection_model_v1
# https://github.com/spmallick/learnopencv/blob/daaa99deaf31a1d50a7c5645092ed34e664b3c5e/FaceDetectionComparison/run-all.py#L31
# https://www.freepik.com/free-photo/young-woman-wearing-striped-shirt-eyeglasses_10228277.htm#query=sample%20people&position=20&from_view=keyword&track=ais_hybrid&uuid=0a2e465b-527c-4b42-a48c-af98ffdaf1ec#page=1&query=s&from_query=undefined&position=1&from_view=keyword&track=ais_hybrid&uuid=0a2e465b-527c-4b42-a48c-af98ffdaf1ec


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FaceSwap needs two images: source from and source two images.") 
    # Add any command-line arguments here
    parser.add_argument('-i', '--input_file', type=str, required=True, help='Path to the input file')
    parser.add_argument('-o', '--output_file', type=str, required=True, help='Path to the output file')

    args = parser.parse_args()
    
    # print(f"Input file: {args.input_file}")
    # print(f"Output file: {args.output_file}")

    #check if the input file exists
    if not confirm_file_exists(args.input_file):
        print(f"Error: The input file {args.input_file} does not exist.")
    
    #check if the output file exists
    if confirm_file_exists(args.output_file):
        print(f"Warning: The output file {args.output_file} already exists and will be overwritten.")

    #if both files exist then we can move on to face swap
    if confirm_file_exists(args.input_file) and confirm_file_exists(args.output_file):
        print(f"ready to move on to face swap.")
        swapped_image = swap_faces(args.input_file, args.output_file)

    print(args)
