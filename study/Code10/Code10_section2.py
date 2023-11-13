import numpy as np
ary1= np.zeros((2,2), dtype=np.int8)
ary2= np.ones((2, 2), dtype=np.int8)
print(ary1)
print(ary2)

print(np.concatenate((ary1, ary2), axis = 0))
print(np.concatenate((ary1, ary2), axis = 1))
