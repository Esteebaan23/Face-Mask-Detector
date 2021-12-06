from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import os
import mediapipe as mp

faceNet = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils


ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", type=str,
	default="mask_detector.model",
	help="path to trained face mask detector model")
args = vars(ap.parse_args())




modelo = load_model(args["model"])
cap = cv2.VideoCapture(0)
with faceNet.FaceDetection(
     min_detection_confidence=0.5) as face_detection:

     while True:
        faces = []
        locs = []
        preds = []
        ret, frame = cap.read()
        if ret == False: break
        frame = cv2.flip(frame, 1)
        height, width, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(frame)
        if results.detections:
          for detection in results.detections:
            #mp_drawing.draw_detection(frame, detection)
            xmin = int(detection.location_data.relative_bounding_box.xmin * width)
            ymin = int(detection.location_data.relative_bounding_box.ymin * height)
            w = int(detection.location_data.relative_bounding_box.width * width)
            h = int(detection.location_data.relative_bounding_box.height * height)
            if(xmin>0 and ymin>0 and xmin<350 and ymin<350):
                face = frame[ymin : ymin + h, xmin : xmin + w]
                face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                face = cv2.resize(face, (224, 224))
                face = img_to_array(face)
                face = preprocess_input(face)
                face = np.expand_dims(face, axis=0)
                preds = modelo.predict(face)
                print(preds)
                print("\n \n \n")
                masked, unmasked = np.split(preds, 2, axis=1)
                label = "Con Mascarilla" if masked > unmasked else "Sin Mascarilla"
                color = (0, 255, 0) if label == "Con Mascarilla" else (0, 0, 255)
                label = "{}".format(label)
                cv2.putText(frame, label, (xmin, ymin - 15),
        			2, 0.45, color, 2)
                cv2.rectangle(frame, (xmin, ymin), (xmin+w, ymin+h), color, 2)
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
    
     cv2.destroyAllWindows()
     vs.stop()