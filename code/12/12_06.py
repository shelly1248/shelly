from tkinter import *
from tkinter import messagebox

# 함수 정의 부분
def myFunc():
    messagebox.showinfo("강아지 버튼", "강아지")

# 메인 코드 부분
window = Tk()

photo = PhotoImage(file="C:\\sqlite\\mysql\\GIF\\dog2.gif")
button1 = Button(window, image=photo, command=myFunc)

button1.pack()

window.mainloop()