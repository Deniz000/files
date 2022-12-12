import cv2 
import keyboard

kamera = cv2.VideoCapture(0)

while True:
    ret, goruntu = kamera.read()

    cv2.line(goruntu,(250,100), (250,400),(140,0,200),5)
    cv2.line(goruntu,(100,250), (400,250),(60,0,200),5)
    cv2.circle(goruntu,(250,250),100,(0,355,0),5)

    cv2.rectangle(goruntu,(100,100),(400,400),(255,0,0),5)


    cv2.imshow("Ben", goruntu)

    if cv2.waitKey(250) and keyboard.is_pressed('q'):
        break

kamera.release()

