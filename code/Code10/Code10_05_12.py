import numpy as np
ary = np.random.randint(-128, 127, size=(3, 3))
print(ary)

print(np.where(ary < 0, 0, ary))