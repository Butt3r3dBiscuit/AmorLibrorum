import tkinter as tk
import Start_window

class login_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        # root = tk.Tk

        # width = root.winfo_screenwidth()
        # height = root.winfo_screenheight()
        # root.geometry("%dx%d" % (width, height))
        # root.title("Employee Window")

        # root.geometry('300x150')
        # root.title('Log in')
        # root.resizable(False, False)

        login_button = tk.Button(self, text="Log in", height=2, width=11)
        login_button.pack()
        login_button.place(x=200, y=95)

        email_label = tk.Label(self, text="Email Adress", width = "15")
        email_label.pack()
        email_text = tk.Text(self, height=1, width=30)
        email_text.pack()

        password_label = tk.Label(self, text="Password", width = "15")
        password_label.pack()
        password_text = tk.Text(self, height=1, width=30)
        password_text.pack()

        '''
         except Exception as e:
                if e.errno==1045:
                    #this error catches if user exists
        '''