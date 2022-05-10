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
Financial = Button(window, text="Financial")
Add_book = Button(window, text="Add Book")
Sell = Button(window, text="Sell")
Add_employee = Button(window, text="Add Employee")


#Text
Book_search = Label(window, text="Book Search")
Title = LabelFrame(window, text="Title")
Author = LabelFrame(window, text="Author")
Editor = LabelFrame(window, text="Editor")
Version = LabelFrame(window, text="Version")
Language = LabelFrame(window, text="Language")
All = LabelFrame(window, text="All")


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

window.mainloop()
