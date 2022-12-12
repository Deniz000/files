from random import randrange
import cv2
import keyboard

car_cascade_src = 'cars.xml'
pedestrian_cascade_src = 'haarcascade_fullbody.xml'

car_cascade = cv2.CascadeClassifier(car_cascade_src)
pedestrian_cascade = cv2.CascadeClassifier(pedestrian_cascade_src)


video = cv2.VideoCapture('video.mp4')

while True:
        successful_frame_read, frame = video.read()

        gray_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray_video,1.1,1)
        pedestrians = pedestrian_cascade.detectMultiScale(gray_video,1.1,1)
        for x,y,w,h in cars:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(256,256,256),2)
        
        for x,y,w,h in pedestrians:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,256,0),2)
        cv2.imshow('video', frame)
        if cv2.waitKey(10) & keyboard.is_pressed('q'):
            break
video.release()


#RESİMDE ARABA BULMA
# img = cv2.imread("cars.jpg")
# grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cars = car_cascade.detectMultiScale(grayscaled_img)
# print(cars)
# for x,y,w,h in cars:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),2)
# #Detect faces
# #draw rectangles round the faces
# print(cars)
# cv2.imshow("resim", img)

# cv2.waitKey(0)