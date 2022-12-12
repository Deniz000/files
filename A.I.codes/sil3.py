import cv2
import numpy as np

resim = np.zeros((300,300,3), dtype='uint8')

cv2.line(resim,(0,0),(150,150),(0,23,235),6)
cv2.circle(resim,(150,150),55,(0,234,23),5 )

cv2.putText(resim,"Hi Bro!",(150,150),cv2.FONT_HERSHEY_COMPLEX,1,(34,35,234),3)

cv2.imshow("goster",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()