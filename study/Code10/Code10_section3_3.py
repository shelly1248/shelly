import numpy as np
ary1 = np.random.randint(0, 255, size=(3, 3))
ary2 = np.random.randint(0, 255, size=(3, 3))
print(np.greater(ary1, ary2))