import cv2
import numpy as np
from pynput.keyboard import Key, Controller

keyboard = Controller()

cap = cv2.VideoCapture(0)

# cascade source
# https://github.com/trane293/Palm-Fist-Gesture-Recognition
cascade = cv2.CascadeClassifier('fist.xml')

width = cap.get(3)
height = cap.get(4)

while(True):

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    match = cascade.detectMultiScale(gray, 1.5, 2)


    if len(match) > 0:
        for (x, y, w, h) in match:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if(x < int(width / 2)):
                cv2.putText(
                    img=frame, 
                    text="Steering left", 
                    org=(50, 50), 
                    fontScale=1, 
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    color=(255, 255, 0)
                )


            elif (x > int(width / 2)):
                cv2.putText(
                    img=frame, 
                    text="Steering Right", 
                    org=(int(width / 2), 50), 
                    fontScale=1, 
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    color=(255, 255, 0)
                )

    cv2.imshow('Driver_frame', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
