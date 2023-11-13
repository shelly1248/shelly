import numpy as np
ary = np.arange(10)
print(ary)
ary_sub2 = ary[3:7].copy() # d.c(깊은복사) s.c(얕은복사)
print(ary_sub2)

ary_sub2[:] = 88
print(ary_sub2)
print(ary)