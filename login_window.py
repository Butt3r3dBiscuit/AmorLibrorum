from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('300x150')
root.title('Log in')
root.resizable(False, False)
# root.attributes('-fullscreen',True)


login_button = Button(root, text="Log in", height=2, width=11)
login_button.pack()
login_button.place(x=200, y=95)

email_label = Label(root, text="Email Adress", width =150)
email_label.pack()
email_text = Entry(root, width=35) #Entry() is a single-line textbox to accept a value from the user
email_text.pack()

password_label = Label(root, text="Password", width =15)
password_label.pack()
password_text = Entry(root, width=35, show="*") #Entry allows to have password concealed
password_text.pack()


# warn = "Username can't be empty"
# warn = "Password can't be empty"
#
#     if (u == un and p == pd):
#         ws.destroy()
#         import app    
#     else:
#         messagebox.showerror('', 'Incorrect credentials')
# else:
#     messagebox.showerror('', warn)

root.mainloop()