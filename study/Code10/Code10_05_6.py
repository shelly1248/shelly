import numpy as np
ary = np.arange(1, 17)
ary = ary.reshape(4, 4)
print(ary[:,1])
print(ary[0:4,1])
# print(ary[,1]) # 오류