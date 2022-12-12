#BİTTİİ FULL BİTİRDİİİM


# import cv2
# img = cv2.imread("nresim1.png",0)

# filtre = [[1,0,-1],[1,0,-1],[1,0,-1]]

# satir, sutun = img.shape
# print(satir)
# print(sutun)

# for i in range(1,satir):
#     for j in range(1,sutun):
#         print(j)



# print(img)
# cv2.imshow("img",img)

# cv2.waitKey(0)

# [1, 2, 3,19,20,34], [-6,-48,-48,-138]
# [4, 5, 6,21,22,98], [-6,-45,45,-141]
# [7, 8, 9,23,24,67], [-6,-42,-42]
# [10,11,12,25,26,45], [-6, -39, -39]
# [13,14,15,27,28], [-27,-27,-27]
# [16,17,18,29,30]
#[31,32,33,34,35]
import numpy as np
import math

# satır sayısı 4'ün katı olacak şekilde çözülebiliyor
a = [[1, 2, 74,19,20,34,43,20,34,43], [4, 5, 53,21,22,98,73,20,34,43],[7, 8, 67,23,24,67,83,20,34,43],[10,11,12,25,26,45,5,20,34,43],[13,14,15,27,28,34,3,28,34,3],[16,17,18,29,30,90,9,28,34,3], [31,32,33,34,35,76,6,30,90,9]]
bir,uc,dort,alti,yedi,dokuz = 0,0,0,0,0,0
toplam = 0
toplamDizi=[]
a = np.array(a)
satir0, sutun0 = a.shape
print(a.reshape(satir0,sutun0))
f = []
for i in range(1,satir0-1):
    for j in range(1,sutun0-1):
            bir = a[i-1][j-1]
            uc = a[i-1][j+1]
            dort = a[i][j-1]
            alti = a[i][j+1]
            yedi = a[i+1][j-1]
            dokuz = a[i+1][j+1]
            toplam = bir - uc + dort - alti + yedi - dokuz
            toplamDizi.append(toplam)
            # print(toplam)
            # print(bir,iki,uc)
            # print(dort, bes)
            # print(alti, yedi ,sekiz)
            toplam=0
tp = toplamDizi.copy()
toplamDizi.sort()
print('--',toplamDizi)
f = np.array(tp)
print(f'f dizisinin bolunmeden önceki hali {f}')
a = f.reshape(satir0-2,sutun0-2)
print(a, ' toplamlar dizisi')
# for i in a:
#     for j in i[0::2]:
#         print(j)
satir,sutun = a.shape
print(f'satır: {satir}  sutun {sutun}')

# temp = []
# for i in range(0,satir,2):# her dörtlü dizinin 0. elemanı
#     for t in range(i,i+2):
#         for j in range(2):
#             print(a[i][j], end=' ')
#     print( )

#4 ün katı sütun olunca çalıştı
# k = []
# sonDizi = []
# for i in range(0,satir,2):
#     for j in range(0,sutun,2):
#         f = []
#         for l in range(2):
#             for m in range(2):
#                 if i+l < satir:
#                     k.append(a[i+l][j+m]) # tüm diziyi görmek için
#                     f.append(a[i+l][j+m])
#                     f.sort()
#                     if len(f)==4:
#                         sonDizi.append(f[0])
# print(k)
# print(sonDizi)

#çalışmıyor
# for i in range(0,satir,2):
#     for j in range(0,sutun,2):
#         for k in range(2):  
#             if sutun%2==0:
#                 for l in range(2):
#                     print(a[i+k][j+l],end=' ')
#             else:
#                 for l in range(2):
#                     if l == sutun:
#                         print(a[i+k][j],end=' ')
#                     else:
#                         print(a[i+k][j+l],end=' ')
                        
#         print()

k = []
sonDizi = []
for i in range(0,satir,2):
    for j in range(0,sutun,2):
        f = []
        for l in range(2):
            for m in range(2):
                #if i+l < satir:
                    #print(f' {j} + {m} = {j + m}')
                    if (i + l) >= satir:
                        l -= 1
                    if (j + m) >= sutun:
                        m -= 1
                    #    print(f' m:> {m}')
                    #print(f' tekrar toplayacak olursak {j} + {m} = {j + m}')

                    k.append(a[i+l][j+m]) # tüm diziyi görmek için
                    f.append(a[i+l][j+m])
                    f.sort()
                    if len(f)==4:
                        sonDizi.append(f[-1])

print(f' ful dizi (üstteki dizinin tek boyutlu hali) : {k}')
print('son Hal: ',sonDizi)
mtrx = np.array(sonDizi) 
if satir%2!=0:
    satir+=1
if sutun%2!=0:
    sutun+=1
k1, k2 =int((satir/2)),int((sutun/2))
print(k1,k2)
eNsoN = mtrx.reshape(k1,k2)
print(eNsoN)
# i=0
# k = 2
# while(i<k):
#     j=0
#     while(j<k):
#         print(a[i][j],end=' ')
#         j+=1
#     print()
#     i+=1