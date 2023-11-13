from tkinter import *

window = Tk()
window.title("4번째 시간")
window.geometry("300x200+100+100")
window.resizable(False, False)

def Calcuate():
    label.configure(text = "결과 값 = " + str(eval(entry.get())))

entry = Entry(window)
entry.pack()

# entry = Entry(window)
# entry.pack()

# entry = Entry(window)
# entry.pack()

# entry = Entry(window)
# entry.pack()

# entry = Entry(window)
# entry.pack()

button = Button(window, text = "클릭", command=Calcuate)
button.pack()

label = Label(window)
label.pack()

window.mainloop()