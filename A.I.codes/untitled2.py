import cv2

image = cv2.imread("C:\deneme\ForSpyder\\farkiBul.jpg",0)

thresh = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                             cv2.THRESH_BINARY,11,2)
thresh2 = cv2.adaptiveThreshold(image,150,cv2.ADAPTIVE_THRESH_MEAN_C,\
                             cv2.THRESH_BINARY,11,2)

cv2.imshow("baslık",image)
cv2.imshow("thresh",thresh)
cv2.imshow("thresh2",thresh2)

cv2.waitKey(0)  