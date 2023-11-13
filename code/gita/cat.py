from tkinter import *
window = Tk()
window.title('cat')

photo1 = PhotoImage(file="C:/sqlite/mysql/GIF/cat.gif")
label1 = Label(window, image=photo1)

photo2 = PhotoImage(file="C:/sqlite/mysql/GIF/cat2.gif")
label2 = Label(window, image=photo2)


label1.pack(side=LEFT)
label2.pack(side=LEFT)
window.mainloop()