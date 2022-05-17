from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Python Guides')
window.geometry('300x200')


def msg1():
   messagebox.askquestion('Ask Question', 'Do you want to continue?')


Button(window, text='Click Me', command=msg1).pack(pady=50)
window.mainloop()