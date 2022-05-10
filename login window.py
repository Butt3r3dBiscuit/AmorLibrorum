from tkinter import *

root = Tk()
root.geometry('300x150')
root.title('Log in')
root.resizable(False, False)

login_button = Button(root, text="Log in", height=2, width=11)
login_button.pack()
login_button.place(x=200, y=95)

email_label = Label(root, text="Email Adress", width = "15")
email_label.pack()
email_text = Text(root, height=1, width=30)
email_text.pack()

password_label = Label(root, text="Password", width = "15")
password_label.pack()
password_text = Text(root, height=1, width=30)
password_text.pack()

root.mainloop()