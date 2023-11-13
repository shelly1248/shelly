from tkinter import *

## 함수 선언 부
def makeEmptySheet(r, w):
    retList = []
    for i in range(0, r): # r = 0, 1, 2, 3
        tmpList = []
        for k in range(0, w): # w = 0, 1, 2
            ent = Entry(window, text = '', width=10) # 칸 설정
            ent.grid(row=i, column=k) 
            tmpList.append(ent)
        retList.append(tmpList)
    return retList

# 전역 변수부
csvList = [ [ '제목1', '제목2', '제목3'],
            [ 111, 222, 333],
            [ 444, 555, 666],
            [ 777, 888, 999]   ] 
rowNum, colNum = 4, 3 # r, w 칸 갯수
worksheet = []

## 메인 코드 부
window = Tk()
worksheet = makeEmptySheet(rowNum, colNum)

# 워크 시트에리스트 값  채우기( = 각 빈 셀에 값 넣기)
for i in range(0, rowNum): # 0은 첫재 위치부터 넣어라
    for k in range(0, colNum): # 0은 첫재 위치부터 넣어라
        worksheet[i][k].insert(0,csvList[i][k])

window.mainloop() # 위젯들이 사건 처리