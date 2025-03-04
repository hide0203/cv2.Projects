import cv2

cap = cv2.VideoCapture()

ret, frame = cap.read()
if not ret:
    print("can't grab frame")


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
print(cv2.data.haarcascades)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
