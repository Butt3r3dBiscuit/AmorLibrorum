import tkinter as tk
import sep_page_one
LARGE_FONT = ("Verdana", 12)


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(sep_page_one.PageOne))
        button1.pack()