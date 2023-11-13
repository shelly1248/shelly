from tkinter import *
from tkinter import messagebox
window = Tk()

# 함수 정의 부분
def myFunc():
    if chk.get() == 0 :
        messagebox.showinfo("", "체크버튼이 꺼졌어요.")
    else:
        messagebox.showinfo("", "체크버튼이 커졌어요.")

# 메인 코드 부분
chk = IntVar()
cb1 = Checkbutton(window, text="클릭하세요", variable=chk, command=myFunc)

cb1.pack()

window.mainloop()