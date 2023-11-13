from tkinter import *
from tkinter import messagebox


window = Tk()
window.geometry("400x400")
window.title("애완동물 선택 하기")

# 함수 정의 부분
def myFunc():
    if var.get() == 1:
        labelImage.configure(image=photo1)
        messagebox.showinfo("강아지 버튼", "강아지")
    elif var.get() == 2:
        labelImage.configure(image=photo2)
        messagebox.showinfo("강아지 버튼", "고양이")
    elif var.get() == 4:
        labelImage.configure(image=photo4)
        messagebox.showinfo("강아지 버튼", "제주")
    else:
        labelImage.configure(image=photo3)
        messagebox.showinfo("강아지 버튼", "토끼")

# 메인 코드 부분
labelText = Label(window, text="좋아하는 동물 투표", fg="blue",font=("궁서체",20))

var = IntVar() 
rb1 = Radiobutton(window, text="강아지", variable=var, value=1)
rb2 = Radiobutton(window, text="고양이", variable=var, value=2)
rb3 = Radiobutton(window, text="토끼", variable=var, value=3)
rb4 = Radiobutton(window, text="제주", variable=var, value=4)
button0k = Button(window, text="사진 보기", command=myFunc)


photo0 = PhotoImage(file="C:\\sqlite\\mysql\\GIF\\lollipop.gif")
photo1 = PhotoImage(file="C:\\sqlite\\mysql\\GIF\\dog4.gif")
photo2 = PhotoImage(file="C:\\sqlite\\mysql\\GIF\\cat.gif")
photo3 = PhotoImage(file="C:\\sqlite\\mysql\\GIF\\rabbit.gif")
photo4 = PhotoImage(file="C:\\sqlite\\mysql\\GIF\\jeju1.gif")

button1 = Button(window, image=photo1, command=myFunc)
button2 = Button(window, image=photo2, command=myFunc)
button3 = Button(window, image=photo3, command=myFunc)
button4 = Button(window, image=photo4, command=myFunc)



labelImage = Label(window, width=200, height=200, bg="gray", image=photo0)


labelText.pack(padx=5, pady=5)
rb1.pack(padx=5, pady=5)
rb2.pack(padx=5, pady=5)
rb3.pack(padx=5, pady=5)
rb4.pack(padx=5, pady=5)
button0k.pack(padx=5, pady=5)
labelImage.pack(padx=5, pady=5)
window.mainloop()
