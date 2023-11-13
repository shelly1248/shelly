import numpy as np
## 넘파이 2차원 배열 생성

SIZE = 3
numpyAry = np.random.randint(0, 255, size=(SIZE, SIZE))

#배열출력
print(numpyAry)
print()

# 배열을 2배 증가후 평균값
numpyArys = numpyAry *2
result = np.sum(numpyArys)
print(round(result / len(numpyArys),2))
