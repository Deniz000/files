import cv2
import numpy as np
import math

def horizontal(girisGoruntusu, imgSatir, imgSutun):
    bir,iki,uc,yedi,sekiz,dokuz = 0,0,0,0,0,0
    toplam = 0
    tekBoyutluCikarim=[]
    for i in range(1,imgSatir-1): 
        for j in range(1,imgSutun-1): 
            bir = girisGoruntusu[i-1][j-1]  
            iki = girisGoruntusu[i-1][j]
            uc = girisGoruntusu[i-1][j+1]
            yedi = girisGoruntusu[i+1][j-1]
            sekiz = girisGoruntusu[i+1][j]
            dokuz = girisGoruntusu[i+1][j+1]
            toplam = (bir + iki + uc) - (yedi + sekiz + dokuz)
            tekBoyutluCikarim.append(toplam)
            toplam=0
    tempArray = np.array(tekBoyutluCikarim)
    yeniGoruntu = tempArray.reshape(imgSatir-2,imgSatir-2)
    print(yeniGoruntu, ' -----------------------toplamlar dizisi')

    # seçilen indisin etrafındaki sayıları toplayıp yeni oluşturduğumuz görüntü 
    return yeniGoruntu  


#son sütundan bir önceki sütuna kadar çalışması gerektiği için imgSütun -1 'de duracak
# son satırdan bir önceki satıra kadar çalışması gerektiği için imgSatir -1 'de duracak
# tek bopyutlu girisGoruntusuyi çok boyutluya çevirebilmek için numpy'ı kullanıyoruz

#veritical filtre uygulama
def vertical(GirisGoruntusu, imgSatir, imgSutun):
    bir,uc,dort,alti,yedi,dokuz = 0,0,0,0,0,0
    toplam = 0
    tekBoyutluCikarim=[]
    for i in range(1,imgSatir-1): 
        for j in range(1,imgSutun-1): 

            bir = GirisGoruntusu[i-1][j-1]  
            uc = GirisGoruntusu[i-1][j+1]
            dort = GirisGoruntusu[i][j-1]
            alti = GirisGoruntusu[i][j+1]
            yedi = GirisGoruntusu[i+1][j-1]
            dokuz = GirisGoruntusu[i+1][j+1]
            toplam = bir - uc + dort - alti + yedi - dokuz
            tekBoyutluCikarim.append(toplam)

            toplam=0 
    tempArray = np.array(tekBoyutluCikarim)  
    yeniGoruntu = tempArray.reshape(imgSatir-2,imgSatir-2)
    print(yeniGoruntu, ' -----------------------toplamlar GirisGoruntususi')

    # seçilen indisin etrafındaki sayıları toplayıp yeni oluşturduğumuz GirisGoruntusu: 
    return yeniGoruntu  

#max elemanı bulma
def maxHavuzlama(filtre):
    geturnGirisGoruntusu = []
    for i in range(0,(imgSatir-2),2):
        for j in range(0,(imgSutun-2),2):
            secilenDortEleman = []
            for l in range(2):
                for m in range(2):
                    if (i + l) >= (imgSatir-2):
                        l -= 1
                    if (j + m) >= (imgSutun -2):
                        m -= 1
                        
                    secilenDortEleman.append(filtre[i+l][j+m])
                    secilenDortEleman.sort()
                    if len(secilenDortEleman)==4:
                        geturnGirisGoruntusu.append(secilenDortEleman[-1])
    return geturnGirisGoruntusu


lena = cv2.imread("lena.png",0)
lenaForVertical = cv2.imread("lena.png",0)
lenaForHorizontal = cv2.imread("lena.png",0)
imgSatir, imgSutun = lena.shape
goruntu = lena

#metotları çağırıyoruz
filtre = vertical(goruntu, imgSatir, imgSutun)
horizontalFiltre = horizontal(goruntu,imgSatir,imgSutun)

#havuzlama işleminden geçiriyoruz
maxVertical = maxHavuzlama(filtre)
maxHorizontal = maxHavuzlama(horizontalFiltre)

#tek boyutlu gelen array'i yine iki boyutluya çevirebilmek için numpy 
#kütüphanesini kullanıyoruz 
verticalArray = np.array(maxVertical) 
horizontalArray = np.array(maxHorizontal) 

#satır ve sütun değerleri çift değilse çift yapıyoruz
#çünkü oluşacak olan son girisGoruntusumiz yani max değerlerin
#seçildiği yeni girisGoruntusu için satır ve süun değerleri yarıya iniyor
#bölebilmemiz için çift olmalı
if imgSatir%2!=0:
    imgSatir+=1
if imgSutun%2!=0:
    imgSutun+=1

#(-2) dememizin nedenini yukarıda açıklamıştık. 
#yeni kenar değerleri için bölme uyguluyoruz. 
k1,k2 = int(((imgSatir-2)/2)),int(((imgSutun-2)/2))

#yeni array 
verticalImage = verticalArray.reshape(k1,k2)
horizontalImage = horizontalArray.reshape(k1,k2)

#girisGoruntusumizi resmimize atıyoruz
lenaForVertical = verticalImage
lenaForHorizontal = horizontalImage

cv2.imshow('ilk',lena)
cv2.imshow('vertical filtre',verticalImage)
cv2.imshow('horizontal filtre',horizontalImage)
cv2.waitKey(0)


