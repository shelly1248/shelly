from tkinter import *
window = Tk()

photo = PhotoImage(file="C:/sqlite/mysql/GIF/dog.gif")
label1 = Label(window, image=photo)

label1.pack()
window.mainloop()