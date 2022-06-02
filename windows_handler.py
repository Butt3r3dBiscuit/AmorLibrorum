import tkinter as tk
#here we will put names of files
from Start_window import Start_window
from login_window import login_window

class Handler(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        width = tk.Tk.winfo_screenwidth(self)
        height = tk.Tk.winfo_screenheight(self)
        tk.Tk.geometry(self,f"{width}x{height}")

        container.pack(side="top", fill="both", expand= True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

#here we will put names of classes in respective files

        for F in (Start_window, login_window):
            print("here", F)
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0,column=0, sticky="nsew")

        self.show_frame(Start_window)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()




if __name__=='__main__':
    LARGE_FONT = ("Verdana", 12)


    app = Handler()
    app.mainloop()
