import tkinter as tk
import Start_window
from connect import connect_admin, connect_employee

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
        back_button = tk.Button(self, text="Return home",height=2, width=11,
                                command= lambda: controller.show_frame(Start_window.Start_window))
        back_button.pack()
        back_button.place(x=0,y=0)


        login_button = tk.Button(self, text="Log in", height=2, width=11, command= self.log_in)
        login_button.pack()
        login_button.place(x=200, y=95)

        email_label = tk.Label(self, text="Email Adress", width = "15")
        email_label.pack()
        self.email_text = tk.Text(self, height=1, width=30)
        self.email_text.pack()

        password_label = tk.Label(self, text="Password", width = "15")
        password_label.pack()
        self.password_text = tk.Text(self, height=1, width=30)
        self.password_text.pack()

    def log_in(self):
        email = self.email_text.get("1.0","end-1c")
        print(email)
        if email=="margje@amorlibrorum.boek":
            print(True)
        else:
            print([email])
        password = self.password_text.get("1.0","end-1c ")
        print(password)
        db = connect_employee(email,password)
        if db == 1045:
            error_label = tk.Label(self, text="User not found!", width = "15", fg="red")
            error_label.pack()
        else:
            my_cursor = db.cursor()






        '''
         except Exception as e:
                if e.errno==1045:
                    #this error catches if user exists
        '''