from tkinter import *

rel_width = 0.1
rel_height = 0.2

start_window = Tk()
start_window.geometry("800x400")
start_window.title("this is start_window.py")


Login = Button(start_window, text="Log in", height=25, width=45)
Login.place(relx=1, relwidth=rel_width, relheight=rel_height, anchor=NE)

Book_search = Label(start_window, text="Book search: ", font='Helvetica 18 bold')
Found = Label(start_window, text="Found: ", font='Helvetica 18 bold')
Title = Label(start_window, text="Title")
Author = Label(start_window, text="Author")
Edition = Label(start_window, text="Edition")
Version = Label(start_window, text="Version")
Location = Label(start_window, text="Location")
Section = Label(start_window, text="Section")
Language = Label(start_window, text="Language")
Sell_price = Label(start_window, text="SellPrice")
In_store = Label(start_window, text="InStore")


Book_search.place(relx=0.2, rely=0.2, relwidth=0.2, relheight=rel_height, anchor=E)
Found.place(relx=0.2, rely=0.6, relwidth=0.2, relheight=rel_height, anchor=E)
Title.place(relx=0.1, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor=E)
Author.place(relx=0.2, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor=E)
Edition.place(relx=0.3, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor=E)
Version.place(relx=0.4, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor=E)
Location.place(relx=0.5, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor=E)
Section.place(relx=0.6, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor=E)
Language.place(relx=0.7, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor=E)
Sell_price.place(relx=0.8, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor=E)
In_store.place(relx=0.9, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor=E)

Book_text = Text(start_window, height=1, width=300, borderwidth=1, relief="groove")
Book_text.pack()
Book_text.place(relx=0.5, rely=0.4, relwidth=0.4, relheight=0.1, anchor=E)

Search = Button(start_window, text="Search")
Search.place(relx=0.8, rely=0.4, relwidth=rel_width, relheight=0.1, anchor=E)

start_window.mainloop()

