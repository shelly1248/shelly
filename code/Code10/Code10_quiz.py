import numpy as np
import random
# 1차원 배열을 생성 1번
# a = np.arange(10,51)

# print(a.dtype)  
# print(a.ndim)
# print(a.shape)

# 반전출력 2번
# print(a[::-1])

# 최대,최솟값 3번
# ary = np.random.randint(0, 255, size=(10,10))
# print(ary)
# print(np.min(ary))
# print(np.max(ary))

# 0-8범위의 값을 사용하여 3x3 배열 생성
# ary = np.arange(0, 9, 1)
# ary = ary.reshape(3, 3)
# print(ary)

# 문제 5 1에서24까지의 가지는4x6크기의 2차원 행렬 생성
# arr = np.arange(1, 25).reshape(4,6)
# # print(arr)
# # #문제 6 arr 배열에 슬라이싱을 적용하여 다음의 출력결과 쓰기
# # print(arr[1:3,1:5])

# # 문제7 위문제의 arr 배열에 슬라이싱 적용
# print(arr[2:,::-1])

# 문제8 arr 배열에서 10~20까지 값만 출력
# result = arr[(arr>=10)& (arr<=20)]

# 문제9 1 부터 20 까지 연속된 정수값을 가지는 1차원배열 작성
# 마지막 원소 : 20
# 모든원소의 합 210
# 모든원소의 평균: 10.5

# ary1 = np.arange(1, 21, 1)
# ary2 = ary1.reshape(4, 5)
# print(f"마지막원소: {ary2.max()}")
# print(f"모든 원소의 합:{ary2.sum()}")
# print(f"모든 원소의 평균: {ary2.mean()}")

# 문제10
# 학생들의 근로 장학금 1.5배 상승
# 출력결과 인상전 금액 200,150,180,200,250
# 인상된금액 300, 225, 270, 330, 375
# 평균금액 300.0
# 평균이상 원소 300, 330, 375
# 평균이상 원소 개수 3

# n1 = np.array([200,150,180,220,250])
# n2 = n1 * 1.5
# avg = sum(n2) / len(n2)
# avgnum = n2[n2 >= avg]
# print(n1) # 인상전 금액
# print(n2) # 인상후 금액
# print(avg)
# print(avgnum)
# print(len(avgnum))
