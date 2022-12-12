import numpy as np

arr = np.array([[[125,137,226],[125,137,226]],[[125,137,226],[125,137,226]]])

temp = [[12,231,124],[12,231,124],[12,231,124],[12,231,124],[12,231,124],[12,231,124],[12,231,124]]

sayac = 0
for i in temp:
    for i in temp[0]:
        sayac +=1
        print(sayac)


print(arr.ndim)