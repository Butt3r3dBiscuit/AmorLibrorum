from tkinter import *


class Child():
    def __init__(self, master):
        new_window = Tk()
        new_window.title("Other one")
        new_window.geometry("400x400")

        self.myButton = Button(new_window, text="No", command=lambda: self.clicker(master, new_window))
        self.myButton.pack(pady=20)

    def clicker(self, master, new_window):
        new_window.destroy()
        from tkinter_main import Elder
        print(1)
        Elder(master)


print("Ok")
