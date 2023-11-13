from tkinter import *
import random

# 변수 선언 부분
btnList = [None] * 9

fnameList = ["eclair.gif", "froyo.gif", "gingerbread.gif", "honeycomb.gif","icecream.gif","jellybean.gif", "kitkat.gif", "lollipop.gif", "marshmallow.gif"]
random.shuffle(fnameList)

photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

# 메인 코드 부분
window = Tk()
window.geometry("210x210")

for i in range(0, 9):
    photoList[i] = PhotoImage(file="C:\\sqlite\\mysql\\GIF\\" + fnameList[i])
    btnList[i] = Button(window, image=photoList[i])

for i in range(0, 3): # 0 ~ 2 까지
    for k in range(0, 3): # 0 ~ 2 까지
        btnList[num].place(x = xPos, y = yPos) # btnList인덱스 0번은 위치가 (0, 0)
        num += 1 # 인덱스 증가
        xPos += 70 # x축 값 증가
    xPos = 0 # 안에 for문 3번 돌리고 나서 x축 초기화
    yPos += 70 # y축 증가 시켜서 다음줄로 넘어가기

window.mainloop()