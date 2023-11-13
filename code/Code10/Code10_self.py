import numpy as np

SIZE = np.random.choice([8, 12, 16 ,20])
nSIZE = int(SIZE/2)
num,num2 = int(SIZE/2), int(SIZE/2)
ary = np.arange(1, 1+(SIZE*SIZE),1)
ary = ary.reshape(SIZE,SIZE)


for i in range(SIZE) :
    for k in range(SIZE) :
        print("%3d" % ary[i][k], end=' ')
    print()
print()


ary2 = ary[num:num+nSIZE, num2: num2+nSIZE].copy()

for i in range(nSIZE) :
    for k in range(nSIZE) :
        print("%3d" % ary2[i][k], end=' ')
    print()
print()

