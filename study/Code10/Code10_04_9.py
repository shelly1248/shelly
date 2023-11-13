import numpy as np
ary = np.arange(10)
ary[0] = 100
print(ary)

sry_sub1 = ary[3:7]
print(sry_sub1)


sry_sub1[:] = 77
print(sry_sub1)
print(ary)
