import cv2

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

# https://github.com/opencv
faceDet = cv2.CascadeClassifier('OpenCV\haarcascade_frontalface_default.xml')
eyeDet = cv2.CascadeClassifier('OpenCV\haarcascade_eye.xml')

while True:
    retV, frame = cam.read()
    color = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = faceDet.detectMultiScale(color, 1.3, 5)
    eye = eyeDet.detectMultiScale(color, 1.3, 5)
    for (x, y, w, h) in face:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    for (x, y, w, h) in eye:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('webcame', frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break

print("process finish")
cam.release()
cv2.destroyAllWindows()
