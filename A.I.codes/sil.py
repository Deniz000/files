from pprint import pprint
import cv2 

resim1 = cv2.imread("bir.png")
resim4 = cv2.imread("ikii.png")
resim5  = cv2.addWeighted(resim1,0.3,resim4,0.7,0)
resim6 = cv2.pyrUp(resim5)
cv2.imshow("resim 5",resim6)

resim2 = cv2.pyrUp(resim1)
resim3 = cv2.pyrDown(resim1)


# cv2.imshow("resim 1",resim1)
# cv2.imshow("resim 2",resim2)
# cv2.imshow("resim 3",resim3)

print(resim1.shape)
print(resim2.shape)
print(resim3.shape)

# sayac = 0
# for i in resim1:
#     for j in resim1[i]:
#         for k in range(3):
#             print(resim1[i][j][k])
#             sayac += 1
#             print(sayac)

cv2.waitKey(0)
cv2.destroyAllWindows()
