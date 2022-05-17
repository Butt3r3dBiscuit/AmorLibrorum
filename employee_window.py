from tkinter import *

rel_width = 0.1
rel_height = 0.05

#Window
window = Tk()
width= window.winfo_screenwidth()
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.title("Employee Window")


#Buttons
Employee = Button(window, text="Employee")
Finance = Button(window, text="Finance")
Inventory = Button(window, text="Inventory")
Add = Button(window, text="Add")
Search = Button(window, text="Search")
Search_all = Button(window, text="Search all")
Save = Button(window, text="Save")
Undo = Button(window, text="Undo")



#Text
Add_employee = Label(window, text="Add Employee: ", font='Helvetica 18 bold')
Search_employee = Label(window, text="Search Employee: ", font='Helvetica 18 bold')
Found = Label(window, text="Found: ", font='Helvetica 18 bold')



#Placement Buttons
Employee.place(relx=1, relwidth=rel_width, relheight=rel_height, anchor=NE)
Finance.place(relx=0.9, relwidth=rel_width, relheight=rel_height, anchor=NE)
Inventory.place(relx=0.8, relwidth=rel_width, relheight=rel_height, anchor=NE)
Add.place(relx=0.7, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor=E)
Add_employee.place(relx=0.2, rely=0.2, relwidth=rel_width, relheight=rel_height, anchor=E)
Search_employee.place(relx=0.2, rely=0.4, relwidth=rel_width, relheight=rel_height, anchor=E)
Search.place(relx=0.5, rely=0.5, relwidth=rel_width, relheight=rel_height, anchor=E)
Search_all.place(relx=0.6, rely=0.5, relwidth=rel_width, relheight=rel_height, anchor=E)
Found.place(relx=0.2, rely=0.6, relwidth=rel_width, relheight=rel_height, anchor=E)
Save.place(relx=1, rely=0.975, relwidth=rel_width, relheight=rel_height, anchor=E)
Undo.place(relx=0.9, rely=0.975, relwidth=rel_width, relheight=rel_height, anchor=E)

#Add employees text and labels
First_label = Label(window, text="First name", width = "15")
First_label.pack()
First_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
First_text.pack()
First_text.place(relx=0.2, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor=E)
First_label.place(relx=0.2, rely=0.25, relwidth=rel_width, relheight=rel_height, anchor=E)

Last_label = Label(window, text="Last name", width = "15")
Last_label.pack()
Last_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Last_text.pack()
Last_text.place(relx=0.3, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor=E)
Last_label.place(relx=0.3, rely=0.25, relwidth=rel_width, relheight=rel_height, anchor=E)

email_label = Label(window, text="Email Adress", width = "15")
email_label.pack()
email_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
email_text.pack()
email_text.place(relx=0.4, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor=E)
email_label.place(relx=0.4, rely=0.25, relwidth=rel_width, relheight=rel_height, anchor=E)

Pass_label = Label(window, text="Password", width = "15")
Pass_label.pack()
Pass_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Pass_text.pack()
Pass_text.place(relx=0.5, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor=E)
Pass_label.place(relx=0.5, rely=0.25, relwidth=rel_width, relheight=rel_height, anchor=E)

Position_label = Label(window, text="Postition", width = "15")
Position_label.pack()
Position_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Position_text.pack()
Position_text.place(relx=0.6, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor=E)
Position_label.place(relx=0.6, rely=0.25, relwidth=rel_width, relheight=rel_height, anchor=E)

#search employees labels and text
First_label = Label(window, text="First name", width = "15")
First_label.pack()
First_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
First_text.pack()
First_text.place(relx=0.2, rely=0.5, relwidth=rel_width, relheight=rel_height, anchor=E)
First_label.place(relx=0.2, rely=0.45, relwidth=rel_width, relheight=rel_height, anchor=E)

Last_label = Label(window, text="Last name", width = "15")
Last_label.pack()
Last_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Last_text.pack()
Last_text.place(relx=0.3, rely=0.5, relwidth=rel_width, relheight=rel_height, anchor=E)
Last_label.place(relx=0.3, rely=0.45, relwidth=rel_width, relheight=rel_height, anchor=E)

#found labels
First_label = Label(window, text="First name", width = "15")
First_label.pack()
First_label.place(relx=0.2, rely=0.65, relwidth=rel_width, relheight=rel_height, anchor=E)

Last_label = Label(window, text="Last name", width = "15")
Last_label.pack()
Last_label.place(relx=0.3, rely=0.65, relwidth=rel_width, relheight=rel_height, anchor=E)

email_label = Label(window, text="Email Adress", width = "15")
email_label.pack()
email_label.place(relx=0.4, rely=0.65, relwidth=rel_width, relheight=rel_height, anchor=E)

Pass_label = Label(window, text="Password", width = "15")
Pass_label.pack()
Pass_label.place(relx=0.5, rely=0.65, relwidth=rel_width, relheight=rel_height, anchor=E)

window.mainloop()

