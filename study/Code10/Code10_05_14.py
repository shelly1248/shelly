import numpy as np
ary2 = np.random.randint(0, 255, size=(3, 3))
print(ary2)

print(ary2.sum())
print(ary2.sum(axis=0)) # 세로의합
print(ary2.sum(axis=1)) # 가로의합

