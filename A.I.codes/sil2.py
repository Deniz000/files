import numpy as np 
import cv2


kamera = cv2.VideoCapture(0)

while True:
    ret,goruntu = kamera.read()
    
    cv2.imshow("me",goruntu)

    if cv2.waitKey(30) & 0xFF == ('q'):
        break
kamera.release()


cv2.destroyAllWindows()