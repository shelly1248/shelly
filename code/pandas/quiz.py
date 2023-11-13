# 1. 1,2,3,4,5 의 모든 값을 두 배씩 증가시킨 값을 지닌 for loop

# import numpy as np
# list = []
# for num in range(1,6):
#     list.append(num *2)
# print(list)
# # 리스트 컴프리헨션
# r1 = [1, 2, 3, 4, 5]
# r2 = [x * 2 for x in r1]
# print(r2)

# r1 = [1, 2, 3, 4, 5]
# r2 = [x + 10 for x in r1]
# # print(r2)

# # 홀수 * 2 출력
# r3 = [x * 2 for x in r1 if x % 2 == 1]
# print(r3)

# r1 = ['bleack', 'white']
# r2 = ['red', 'Blue', 'Green']
# r3 = []

# for i in r1:
#     for j in r2:
#         r3.append(i + j)
# print(r3)

# r3 = [ i + j for i in r1 for j in r2]
# print(r3)

# r4 = [f'{i}X{j} = {i * j}'  for i in range(2, 10) for j in range(1, 10)]
# print(r4,end=' ')