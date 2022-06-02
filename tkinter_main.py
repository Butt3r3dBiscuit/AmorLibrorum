from tkinter import *


root = Tk()
root.title("test")
root.geometry("400x400")

class Elder:
    def __init__(self, master):
        root = Tk()
        root.title("test")
        root.geometry("400x400")
        myFrame = Frame(master)
        myFrame.pack()

        self.myButton = Button(master, text="Test", command= lambda: self.clicker(master))
        self.myButton.pack(pady=20)

    def clicker(self, master):
        from tkinter_child import  Child
        Child(master)
        root.destroy()




# class Child(Elder):
#     def __init__(self):
#         new_window = Tk()
#         new_window.title("Other one")
#         new_window.geometry("400x400")
#
#         self.myButton = Button(new_window, text="No", command=self.clicker)
#         self.myButton.pack(pady=20)

e = Elder(root)

root.mainloop()