import cv2 
import numpy as np
import pandas as pd


def sifirinciKareBEnzerliği(resim1,resim2):
    resimBir = resim1[0:200,0:200]
    resimIki = resim2[0:200,0:200]

    sayac = 0
    toplamPixel = 0
    sayac2 = 0
    for i in range(200): # 200 satır ( 200 iç dizi)
        for j in range(200):# 200 sütun ( her iç dizinin satır sayısı)
            temp = []  #rgb kontrolü -ya da rgb- için; r g b nin arı ayrı değerlerini alıp dizi ekleyecek, pixel karşılaştırması için
            toplamPixel += 1
            for k in range(3): # 3 kanal : R G B için 
                if resimBir[i][j][k] == resimIki[i][j][k]:
                    temp.append(resimBir[i][j][k])
                #else kısmını yazmaya gerek yok
                # else:
                #     print("DEEEEĞİİİİL", resimBir[i][j][k],resimIki[i][j][k])
            if temp !=[]:
                sayac+=1
            else: 
                sayac2 +=1
    print(sayac)
    print(toplamPixel)
    print(sayac2)
    
def birinciKareBenzerliği(resim1,resim2):
    resimBir = resim1[0:200,200:400]
    resimIki = resim2[0:200,200:400]
    sayac = 0
    toplamPixel = 0
    sayac2 = 0
    for i in range(200): # 200 satır ( 200 iç dizi)
        for j in range(200):# 200 sütun ( her iç dizinin satır sayısı)
            temp = []  #rgb kontrolü -ya da rgb- için; r g b nin arı ayrı değerlerini alıp dizi ekleyecek, pixel karşılaştırması için
            toplamPixel += 1
            for k in range(3): # 3 kanal : R G B için 
                if resimBir[i][j][k] == resimIki[i][j][k]:
                    temp.append(resimBir[i][j][k])
                #else kısmını yazmaya gerek yok
                # else:
                #     print("DEEEEĞİİİİL", resimBir[i][j][k],resimIki[i][j][k])
            if temp !=[]:
                sayac+=1
            else: 
                sayac2 +=1
    print(sayac)
    print(toplamPixel)
    print(sayac2)

def benzerlik(resim1, resim2):
    sayac, toplamPixel = 0,0
    for i in range(405): # 600 satır ( 600 iç dizi)
        for j in range(405):# 600 sütun ( her iç dizinin satır sayısı)
            temp = []  #rgb kontrolü -ya da rgb- için; r g b nin arı ayrı değerlerini alıp dizi ekleyecek, pixel karşılaştırması için
            toplamPixel += 1
            for k in range(3): # 3 kanal : R G B için 
                if resim1[i][j][k] == resim2[i][j][k]:
                    temp.append(resim1[i][j][k])
            rgb = np.array(temp)
            if rgb.size == 3:
                print(temp)
                sayac+=1
            else: 
                pass
    print("Aynı olan pixel sayısı",sayac)
    print("Toplam pixel sayısı",toplamPixel)
    print("Oran",sayac/toplamPixel)
    print("Yüzde",(sayac*100)/toplamPixel)


def red(resim1, resim2):
    resimBir = resim1[0:600, 0:600]
    resimIki = resim2[0:600,0:600]
    sayac = 0
    toplamPixel = 0
    sayac2 = 0
    for i in range(600): # 600 satır ( 600 iç dizi)
        for j in range(600):# 600 sütun ( her iç dizinin satır sayısı)
            temp = []  #rgb kontrolü -ya da rgb- için; r g b nin arı ayrı değerlerini alıp dizi ekleyecek, pixel karşılaştırması için
            toplamPixel += 1
            for k in range(1): # 3 kanal : R G B için 
                if resimBir[i][j][k] == resimIki[i][j][k]:
                    temp.append(resimBir[i][j][k])
            if temp != []:
                sayac+=1
            else: 
                sayac2 +=1
    print("R kanalı benzerlik sayısı",sayac)
    print("Toplam R kanalı sayısı",toplamPixel)
    print("Oran",sayac/toplamPixel)


def green(resim1, resim2):
    resimBir = resim1[0:600, 0:600]
    resimIki = resim2[0:600,0:600]
    sayac = 0
    toplamPixel = 0
    sayac2 = 0
    for i in range(600): # 600 satır ( 600 iç dizi)
        for j in range(600):# 600 sütun ( her iç dizinin satır sayısı)
            temp = []  #rgb kontrolü -ya da rgb- için; r g b nin arı ayrı değerlerini alıp dizi ekleyecek, pixel karşılaştırması için
            toplamPixel += 1
            for k in range(1,2): # 3 kanal : R G B için 
                if resimBir[i][j][k] == resimIki[i][j][k]:
                    temp.append(resimBir[i][j][k])
            if temp != []:
                sayac+=1
            else: 
                sayac2 +=1
    print("G kanalı benzerlik sayısı",sayac)
    print("Toplam G kanalı sayısı",toplamPixel)
    print("Oran",sayac/toplamPixel)


def blue(resim1, resim2):
    resimBir = resim1[0:600, 0:600]
    resimIki = resim2[0:600,0:600]
    sayac = 0
    toplamPixel = 0
    sayac2 = 0
    for i in range(600): # 600 satır ( 600 iç dizi)
        for j in range(600):# 600 sütun ( her iç dizinin satır sayısı)
            temp = []  #rgb kontrolü -ya da rgb- için; r g b nin arı ayrı değerlerini alıp dizi ekleyecek, pixel karşılaştırması için
            toplamPixel += 1
            for k in range(2,3): # 3 kanal : R G B için 
                if resimBir[i][j][k] == resimIki[i][j][k]:
                    temp.append(resimBir[i][j][k])
            if temp != []:
                sayac+=1
            else: 
                sayac2 +=1

    print("B kanalı benzerlik sayısı",sayac)
    print("Toplam B kanalı sayısı",toplamPixel)
    print("Oran",sayac/toplamPixel)


resim1 = cv2.imread("k1.png")
resim2 = cv2.imread("k2.png")

benzerlik(resim1,resim2)
# red(resim1, resim2)
# green(resim1, resim2)
# blue(resim1, resim2)

cv2.imshow("resim 1",resim1)
cv2.imshow("resim 2",resim2)
# kirmiListe = resim1[0:200,0:200]
# resimIkiListe = resim2[0:200,0:200]

# print("RESİM[0] ÇALIŞTI : >",resim1[1])
# print("RESİM[0][0:5] ÇALIŞTI : >",resim1[1][0:5])

# print(kirmiListe[0][0])
# print(resimIkiListe[0][0])

cv2.waitKey(0)
cv2.destroyAllWindows()
