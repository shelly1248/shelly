import numpy as np
ary1 = np.random.randint(0, 255, size=(3, 3))
print(ary1)

ary2 = np.random.randint(0, 255, size=(3, 3))
print(ary2)

print(np.maximum(ary1, ary2))