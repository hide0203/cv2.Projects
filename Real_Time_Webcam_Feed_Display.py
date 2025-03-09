import cv2

cap = cv2.VideoCapture(0)  #Access camera(but doesn't display it)
if not cap.isOpened:
    print("Error can't access camera.")

while True:
    ret, frame= cap.read()
    #ret= a boolean variable, True if frame is captured, False if frams isn't captured
    #frame= image from the camera 
    #cap.read()= returns the value of ret and frame
    if not ret:
        print("Failed to grab frame.")
        break

    cv2.imshow("webcam feed", frame)  #cv2.imshow = displays the image from camera
    
    if cv2.waitKey(1)== ord('q'):
    #.waitKey(1)= waits for 1 millisecond and returns the ASCII value if any key is pressed, and if no key is pressed it returns -1(meaning no key was detected).
    #ord('q') = ASCII value of q is 113 and ord('q') has the same value.(by pressing q you close the cv2 camera window).
        break

cap.release()  # camera access is revoked 
cv2.destroyAllWindows()   # closes any cv2 window 