from tkinter import *


rel_width = 0.1
rel_height = 0.2

window = Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.title("Book search")

# window = Tk()
# window.geometry("800x400")
# window.title("start Window")

def open_login_window():
    window.destroy()
    import login_window





Login = Button(window, text="Log in", height=25, width=45, command=open_login_window)
Login.place(relx=1, relwidth=rel_width, relheight=rel_height, anchor=NE)

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

Book_text = Text(window, height=1, width=300, borderwidth=1, relief="groove")
Book_text.pack()
Book_text.place(relx=0.5, rely=0.4, relwidth=0.4, relheight=0.1, anchor=E)

Search = Button(window, text="Search")
Search.place(relx=0.8, rely=0.4, relwidth=rel_width, relheight=0.1, anchor=E)

window.mainloop()

