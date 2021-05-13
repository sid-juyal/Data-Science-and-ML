# Read a Video Stream from camera (Frame by Frame)
import cv2

cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("C:/Users/SIDDHARTH/desktop/ML and Data Science/haarcascade_frontalface_default.xml")

while True:
    ret,frame=cap.read()
    grey_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if ret==False:
        continue

    faces=face_cascade.detectMultiScale(grey_frame,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("Video Frame",frame)
    #cv2.imshow("Gray Frame",gray_frame)

    # Wait for user input -q, then you will stop the loop
    key_pressed=cv2.waitKey(1)&0xFF
    if key_pressed==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
