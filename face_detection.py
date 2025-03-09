import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    # .CascadeClassifier: an OpenCV function that loads the haarcascade model.
    # cv2.data.haarcascades: a path to the haarcascades folder in the OpenCV library.
    # haarcascade_frontalface_default.xml: name of the file that contains the haarcascade model for face detection.

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("can't grab frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  #Detect faces
    # .detectMultiScale: it searches for faces in in the grayscale image.
    # Gray because face detection works better in grayscale images.
    # 1.3 is scale value, it tells the algorithm to increase the size of the face by 30% each time it is not found.
    # 5 is the minimum numbers of conditions that should be satisfied for the rectangle to be considered as a face.


    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) #Draw rectangle around the faces
    # .rectangle: a OpenCV function draws a rectangle around the face.
    # (x+y) is the top-left corner of the rectangle.
    # (x+w, y+h) is the bottom-right corner of the rectangle.
    # (255, 0, 0) is the color of the rectangle in BGR format.
    # 2 is the thickness of the rectangle.

    cv2.imshow("Face Detection", frame) #Display the frame

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()