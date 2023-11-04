bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0] 
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]  
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0] 
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9] 

import matplotlib.pyplot as plt
# ==================================== 알고리즘===============================
plt.scatter(bream_length, bream_weight) # 도미 길이, 무게
plt.scatter(smelt_length, smelt_weight) # 빙어 길이, 무게
plt.scatter(30, 600, marker='^') # marker 30,600 을 세모표시



# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show() # 2차원 그래프
# ========================================= 데이터 정리 ===============================

length = bream_length + smelt_length
weight = bream_weight + smelt_weight
fishdata = [[l, w]for l, w in zip(length, weight)] # zip 함수로 길이와무게를 리스트 제작
# print(fishdata)
# print(len(bream_length))
# print(len(smelt_weight))
fishtaget = [1]*35 + [0]*14 # [1]도미35, [0]빙어14
# print(fishtaget)


#========================================= 대상 찾기=====================================
from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier() # 포인트 하나 최근접 이웃으로 찾아 예측
# 어떤 데이터에 대한 답을 구할 때 주위의 다른 데이터를 보고 다수를 차지하는 것을 정답으로 판단
# print(kn)
kn.fit(fishdata, fishtaget) # 데이터알고리즘 훈련
# print(kn.fit(fishdata, fishtaget))
# print(kn.score(fishdata, fishtaget)) # 1 맞추다 0 틀리다 

# print(kn.predict([[30, 600]])) # 데이터의 정답 예측 <- 2차원 그래프 보고 데이터 입력

# print(kn._fit_X)
# print(kn._y)

kn49 = KNeighborsClassifier(n_neighbors=49) # 가장 가까운 데이터 49개 참고

# kn49.fit(fishdata, fishtaget)
# kn49.score(fishdata, fishtaget)

# print(35/ 49)

kn = KNeighborsClassifier()
kn.fit(fishdata, fishtaget)
num = 0
for n in range(5, 50):
    kn.n_neighbors = n
    score = kn.score(fishdata, fishtaget)
    print(n)
    if score < 1:
        print(n, score)
        break
    

        

