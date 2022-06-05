import tkinter as tk
# here we will put names of files
from sep_page_one import PageOne
from sep_start_page import StartPage


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        tk.Tk.geometry(self, "1000x500")

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # here we will put names of classes in respective files

        for F in (StartPage, PageOne):
            print("here", F)
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


if __name__ == '__main__':
    LARGE_FONT = ("Verdana", 12)

    app = SeaofBTCapp()
    app.mainloop()
