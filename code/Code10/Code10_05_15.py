import numpy as np

ary2 = np.random.randint(0, 255, size=(3, 3))
print(ary2)

print((ary2 > 128).sum()) # 항목의 개수