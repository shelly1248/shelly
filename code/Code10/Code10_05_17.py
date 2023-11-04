import numpy as np

ary = np.random.randint(0, 255, size=10)
print(ary)

print(np.sort(ary))
print(np.sort(ary)[::-1]) # 내림차순
