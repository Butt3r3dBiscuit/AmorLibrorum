from tkinter import *

rel_width = 0.1
rel_height = 0.05

window = Tk()
window.geometry("800x400")
window.title("Employee sales tab")

Search = Button(window, text="Search")
Search.place(relx=0.4, rely=0.35, relwidth=rel_width, relheight=0.1, anchor=E)

Sell = Button(window, text="Sell")
Sell.place(relx=1, rely=0.9, relwidth=rel_width, relheight=0.1, anchor=E)

Book_label = Label(window, text="Book ID", width = "15")
Book_label.pack()
Book_text = Text(window, borderwidth=1, relief="groove")
Book_text.pack()
Book_text.place(relx=0.3, rely=0.35, relwidth=0.2, relheight=0.1, anchor=E)
Book_label.place(relx=0.2, rely=0.25, relwidth=rel_width, relheight=rel_height, anchor=E)


Book_search = Label(window, text="Book search: ", font='Helvetica 18 bold')
Found = Label(window, text="Found: ", font='Helvetica 18 bold')
Title = Label(window, text="Title")
Author = Label(window, text="Author")
Edition = Label(window, text="Edition")
Version = Label(window, text="Version")
Location = Label(window, text="Location")
Section = Label(window, text="Section")
Language = Label(window, text="Language")
Sell_price = Label(window, text="SellPrice")
In_store = Label(window, text="InStore")


Book_search.place(relx=0.25, rely=0.1, relwidth=0.2, relheight=rel_height, anchor=E)
Found.place(relx=0.2, rely=0.5, relwidth=0.2, relheight=rel_height, anchor=E)
Title.place(relx=0.1, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor=E)
Author.place(relx=0.2, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor=E)
Edition.place(relx=0.3, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor=E)
Version.place(relx=0.4, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor=E)
Location.place(relx=0.5, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor=E)
Section.place(relx=0.6, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor=E)
Language.place(relx=0.7, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor=E)
Sell_price.place(relx=0.8, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor=E)
In_store.place(relx=0.9, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor=E)





window.mainloop()

