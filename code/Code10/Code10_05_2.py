import numpy as np
ary1 = np.arange(1, 26, 1)
ary2 = ary1.reshape(5, 5)
ary3 = ary2.reshape(25)
print(ary3)