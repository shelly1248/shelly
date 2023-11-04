import numpy as np
ary = np.arange(1, 17)
ary = ary.reshape(4, 4)
print(ary[2:])
print(ary[2:4,])
print(ary[2:4,:])