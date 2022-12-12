import cv2
from random import randrange
import keyboard

trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
webcam = cv2.VideoCapture(0)

while True:
    successful_frame_read, frame = webcam.read()

    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    #draw rectangles round the faces
    for x,y,w,h in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(256,256,256),2)
    cv2.imshow("me", frame)
    if cv2.waitKey(20) & keyboard.is_pressed('q'):
        break
webcam.release()

# q

# #Detect faces
# face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
# print(face_coordinates)
# #draw rectangles round the faces
# for x,y,w,h in face_coordinates:
#     cv2.rectangle(webcam,(x,y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),2)
# print(face_coordinates)
# cv2.imshow("resim", webcam)

cv2.waitKey(1)