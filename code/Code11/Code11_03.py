import numpy as np
import matplotlib.pyplot as plt

SIZE = 30
x_vlaue = np.random.rand(SIZE) # 데이터 30개
y_value = np.random.rand(SIZE)
sizeAry = (50 * np.random.randn(SIZE)) ** 2 # 사이즈 크기 랜덤
colorAry = np.random.rand(SIZE) # 색깔

plt.scatter(x_vlaue, y_value, s=sizeAry, c=colorAry, alpha= 0.5, cmap='spring') # alpha 투명도 cmap='spring' 산점도 분위기 예)글씨체
plt.colorbar()
plt.show()