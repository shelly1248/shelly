import numpy as np
ary1 = np.random.randint(0, 9, size=10)
print(ary1)

ary2 = np.random.randint(0, 9, size=10)
print(ary2)

print(np.intersect1d(ary1, ary2)) # 공통된 항목 추출