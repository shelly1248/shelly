import numpy as np
ary1 = np.random.randint(0, 255, size=(3, 3))
# print(ary1)
ary2 = np.random.randint(0, 255, size=(3, 3))
# print(ary2)

condAry = np.random.choice([True, False], size=(3, 3))
print(condAry)

print(np.where(condAry, ary1, ary2))

# np.where(조건, 참, 거짓)