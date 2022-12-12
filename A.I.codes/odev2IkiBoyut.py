import numpy as np
dizi = [[1,2,23,4,5,6,2],[1,2,3,4,5,6,2],[1,6,23,4,5,6,2],[1,766,23,4,5,6,2]]
f = []
y = []
for i in range(4):
    for j in dizi[i]:
        y.append(j)
    f = np.array(y)

print(f.reshape(4,7))
