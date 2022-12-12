import cv2
import numpy as np
import math

ilkResim = cv2.imread("lena.png",0)
img = cv2.imread("lena.png",0)
imgSatir, imgSutun = img.shape

dizi = img
bir,uc,dort,alti,yedi,dokuz = 0,0,0,0,0,0
toplam = 0
tekBoyutluToplamlarDizisi=[]
f = []
#print(dizi)
sayac = 0
for i in range(1,imgSatir-1):
    for j in range(1,imgSutun-1):
        bir = dizi[i-1][j-1]
        uc = dizi[i-1][j+1]
        dort = dizi[i][j-1]
        alti = dizi[i][j+1]
        yedi = dizi[i+1][j-1]
        dokuz = dizi[i+1][j+1]
        toplam = bir - uc + dort - alti + yedi - dokuz
        tekBoyutluToplamlarDizisi.append(toplam)
        # print(toplam)
        # print(bir,iki,uc)
        # print(dort, bes)
        # print(alti, yedi ,sekiz)
        toplam=0
#print('toplam Dizi: ', tekBoyutluToplamlarDizisi)
ikiBoyutluToplamDizisi = np.array(tekBoyutluToplamlarDizisi)
dongununYeniAnahtari = ikiBoyutluToplamDizisi.reshape(imgSatir-2,imgSatir-2)
print(dongununYeniAnahtari, ' -----------------------toplamlar dizisi')


k = []
sonDizi = []
for i in range(0,(imgSatir-2),2):
    for j in range(0,(imgSutun-2),2):
        f = []
        for l in range(2):
            for m in range(2):
                #if i+l < satir:
                    #print(f' {j} + {m} = {j + m}')
                    if (i + l) >= (imgSatir-2):
                        l -= 1
                    if (j + m) >= (imgSutun -2):
                        m -= 1
                    #    print(f' m:> {m}')
                    #print(f' tekrar toplayacak olursak {j} + {m} = {j + m}')

                    k.append(dongununYeniAnahtari[i+l][j+m]) # tüm diziyi görmek için
                    f.append(dongununYeniAnahtari[i+l][j+m])
                    f.sort()
                    if len(f)==4:
                        sonDizi.append(f[-1])

#print(f' ful dizi : {k}')
mtrx = np.array(sonDizi) 
if imgSatir%2!=0:
    imgSatir+=1
if imgSutun%2!=0:
    imgSutun+=1
k1,k2 = int(((imgSatir-2)/2)),int(((imgSutun-2)/2))
print(k1,k2)
eNsoN = mtrx.reshape(k1,k2)
print(eNsoN)
#print(sonDizi)


img = eNsoN

cv2.imshow('img',img)
cv2.imshow('ilk',ilkResim)

cv2.waitKey(0)
