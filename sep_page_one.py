import tkinter as tk
# from now_make_it_separate_files import StartPage

LARGE_FONT = ("Verdana", 12)

class PageOne(tk.Frame):
    def __init__(self, parent, controller, StartPage):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Page One!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
