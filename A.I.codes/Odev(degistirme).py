import numpy as np
import cv2 

def benzerlik(resim1, resim2):
    ayniPixelSayisi, toplamPixel = 0,0
    p1 = 0
    for i in resim1:
        p2 = 0
        for j in resim1[i]:
            temp = []  
            toplamPixel += 1
            for k in range(3): # 3 kanal : R G B için 
                if resim1[p1][p2][k] == resim2[p1][p2][k]:
                    temp.append(resim1[p1][p2][k])
            rgb = np.array(temp)
            if rgb.size == 3:
                print(temp)
                ayniPixelSayisi+=1
            else: 
                pass
            p2 = p2 + 1
        p1 += 1
        
        
    print("Aynı olan pixel sayısı",ayniPixelSayisi)
    print("Toplam pixel sayısı",toplamPixel)
    print("Oran",ayniPixelSayisi/toplamPixel)
    print("Yüzde",(ayniPixelSayisi*100)/toplamPixel)


resim1 = cv2.imread("C:\deneme\\k1.png")
resim2 = cv2.imread("C:\deneme\\k2.png")
benzerlik(resim1,resim2)
