from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("400x200")

def Click():
    messagebox.askquestion("askquestion", "Are you sure?")

button = Button(window,text = "Click Me", command = Click)
button.pack()

window.mainloop()
