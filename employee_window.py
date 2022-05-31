from tkinter import *

rel_width = 0.1
rel_height = 0.05

#employee_window
employee_window = Tk()
width= employee_window.winfo_screenwidth()
height= employee_window.winfo_screenheight()
employee_window.geometry("%dx%d" % (width, height))
employee_window.title("this is employee_window.py")
# employee_window.attributes('-fullscreen',True)

#Buttons
Financial = Button(employee_window, text="Financial")
Add_book = Button(employee_window, text="Add Book")
Sell = Button(employee_window, text="Sell")
Add_employee = Button(employee_window, text="Add Employee")


#Text
Book_search = Label(employee_window, text="Book Search")
Title = LabelFrame(employee_window, text="Title")
Author = LabelFrame(employee_window, text="Author")
Editor = LabelFrame(employee_window, text="Editor")
Version = LabelFrame(employee_window, text="Version")
Language = LabelFrame(employee_window, text="Language")
All = LabelFrame(employee_window, text="All")


#Placement Buttons
Financial.place(relx=1, relwidth=rel_width, relheight=rel_height, anchor=NE)
Add_book.place(relx=0.9, relwidth=rel_width, relheight=rel_height, anchor=NE)
Sell.place(relx=0.8, relwidth=rel_width, relheight=rel_height, anchor=NE)
Add_employee.place(relx=0.7, relwidth=rel_width, relheight=rel_height, anchor=NE)

#Placement Text
Book_search.place(relx=0.18, rely=0.15, relwidth=rel_width, relheight=rel_height, anchor=E)
Title.place(relx=0.2, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor=E)
Author.place(relx=0.35, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor=E)
Editor.place(relx=0.5, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor=E)
Version.place(relx=0.65, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor=E)
Language.place(relx=0.8, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor=E)
All.place(relx=0.95, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor=E)

employee_window.mainloop()
