import cv2
import os
import numpy as np
from PIL import Image

# https://github.com/opencv
faceDet = cv2.CascadeClassifier('OpenCV\haarcascade_frontalface_default.xml')
eyeDet = cv2.CascadeClassifier('OpenCV\haarcascade_eye.xml')
faceRecognition = cv2.face.LBPHFaceRecognizer_create()
dirFile = 'face_databases'


def getFace_database(path):
    imgPaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    faceIDs = []

    for imgPath in imgPaths:
        PILImg = Image.open(imgPath).convert('L')
        imgNum = np.array(PILImg, 'uint8')
        faceID = int(os.path.split(imgPath)[-1].split(".")[1])
        faces = faceDet.detectMultiScale(imgNum)
        for (x, y, w, h) in faces:
            faceSamples.append(imgNum[y:y + h, x:x + w])
            faceIDs.append(faceID)
        return faceSamples, faceIDs


print("Scanning..")
faces, IDs = getFace_database(dirFile)
faceRecognition.train(faces, np.array(IDs))
faceRecognition.write(dirFile + '/learning.xml')
print('Saving as learning.xml to ID ', format(len(np.unique(IDs))))
