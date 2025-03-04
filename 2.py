import cv2

cap = cv2.VideoCapture(0)
if not cap:
    print("Can't access camera.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("can't grab frame")
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   
    #To learn it:cv2.cvtColor(convert color)
    #frame(convert color of frame)
    #cv2.COLOR_BGR2GRAY(color from blue green red to(2) gray)
    cv2.imshow("grayscale webcam" ,gray_frame)  

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break