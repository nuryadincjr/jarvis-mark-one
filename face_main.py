import cv2


cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

# https://github.com/opencv
faceDet = cv2.CascadeClassifier('OpenCV\haarcascade_frontalface_default.xml')
eyeDet = cv2.CascadeClassifier('OpenCV\haarcascade_eye.xml')
faceRecognition = cv2.face.LBPHFaceRecognizer_create()
faceDir = 'face_databases'
faceRecognition.read(faceDir + '/learning.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

faceID = 0
name_list = ['unknown', 'Abugray']

minWidth = 0.1 * cam.get(3)
minHeight = 0.1 * cam.get(4)

while True:
    retV, frame = cam.read()
    frame = cv2.flip(frame, 1)

    color = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = faceDet.detectMultiScale(color, 1.2, 5, minSize=(round(minWidth), round(minHeight)))
    eye = eyeDet.detectMultiScale(color, 1.2, 5)
    for (x, y, w, h) in face:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        faceID, confidence = faceRecognition.predict(color[y: y + h, x: x + w])
        if confidence <= 52:
            nameID = name_list[faceID]
            confidenceTxt = " {0}%".format(round(100 - confidence))
        else:
            nameID = name_list[0]
            confidenceTxt = " {0}%".format(round(100 - confidence))

        cv2.putText(frame, str(nameID), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(frame, str(confidenceTxt), (x + 5, y + h - 5), font, 1, (255, 255, 255), 1)

    for (x, y, w, h) in eye:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('webcame', frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break

print("process finish")
cam.release()
cv2.destroyAllWindows()
