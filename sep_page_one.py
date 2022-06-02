import tkinter as tk
# from now_make_it_separate_files import StartPage
import sep_start_page


LARGE_FONT = ("Verdana", 12)

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Page One!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(sep_start_page.StartPage))
        button1.pack()
