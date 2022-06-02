import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, *args, **kwargs)

        lb = tk.Label(self, ...)
        ...
        button_main = tk.Button(self, ...)
        ...
        button = tk.Button(self, ...)
        ...

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    # app is a frame, so add it to root. Since it's the
    # only widget in root, pack is the simplest method
    # to add it to the root window
    app.pack(fill="both", expand=True)