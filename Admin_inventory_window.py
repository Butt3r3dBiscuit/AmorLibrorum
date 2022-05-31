from tkinter import *

rel_width = 0.1
rel_height = 0.05

# Window
window = Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.title("Inventory Window")

# text
Add_book = Label(window, text="Add Book: ", font='Helvetica 18 bold')
Search_book = Label(window, text="Search Book: ", font='Helvetica 18 bold')
Found_book = Label(window, text="Books Found: ", font='Helvetica 18 bold')
Set_sellprice = Label(window, text="Set Sellprice: ", font='Helvetica 18 bold')

Title = Label(window, text="Title")
Author = Label(window, text="Author")
Edition = Label(window, text="Edition")
Version = Label(window, text="Version")
Buy_price = Label(window, text="BuyPrice")
Sell_price = Label(window, text="SellPrice")
In_store = Label(window, text="InStore")

# text place
Found_book.place(relx=0.2, rely=0.25, relwidth=rel_width, relheight=rel_height, anchor=E)
Title.place(relx=0.2, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor=E)
Author.place(relx=0.3, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor=E)
Edition.place(relx=0.4, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor=E)
Version.place(relx=0.5, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor=E)
Buy_price.place(relx=0.6, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor=E)
Sell_price.place(relx=0.7, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor=E)
In_store.place(relx=0.8, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor=E)
Set_sellprice.place(relx=0.2, rely=0.45, relwidth=rel_width, relheight=rel_height, anchor=E)

#button functions

def yes_button():
    Translated_label.pack()
    Translator_text.pack()
    Untranslated_label.pack()
    Untranslated_text.pack()
    Origin_text.pack()
    Origin_label.pack()


def no_button():
    Translated_label.pack_forget()
    Translator_text.pack_forget()
    Untranslated_label.pack_forget()
    Untranslated_text.pack_forget()
    Origin_text.pack_forget()
    Origin_label.pack_forget()

def open_employee_window():
    #window.destroy()
    import employee_window
    print("test")

# Buttons
Employee = Button(window, text="Employee", command=open_employee_window)
Finance = Button(window, text="Finance")
Inventory = Button(window, text="Inventory")
Save = Button(window, text="Save")
Undo = Button(window, text="Undo")
Add = Button(window, text="Add")
Search = Button(window, text="Search")
Search_all = Button(window, text="Search All")
Set = Button(window, text="Set")

# place label
Add_book.place(relx=0.2, rely=0.6, relwidth=rel_width, relheight=rel_height, anchor=E)
Search_book.place(relx=0.2, rely=0.1, relwidth=rel_width, relheight=rel_height, anchor=E)

# Place Buttons
Employee.place(relx=1, relwidth=rel_width, relheight=rel_height, anchor=NE)
Finance.place(relx=0.9, relwidth=rel_width, relheight=rel_height, anchor=NE)
Inventory.place(relx=0.8, relwidth=rel_width, relheight=rel_height, anchor=NE)
Save.place(relx=1, rely=0.975, relwidth=rel_width, relheight=rel_height, anchor=E)
Undo.place(relx=0.9, rely=0.975, relwidth=rel_width, relheight=rel_height, anchor=E)

# text and labels
Sell_Price_label = Label(window, text="Sell Price", width="15")
Sell_Price_label.pack()
Sell_Price_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Sell_Price_text.pack()

Isbn_label3 = Label(window, text="ISBN", width="15")
Isbn_label3.pack()
Isbn_text3 = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Isbn_text3.pack()

Isbn_label2 = Label(window, text="ISBN", width="15")
Isbn_label2.pack()
Isbn_text2 = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Isbn_text2.pack()

Isbn_label = Label(window, text="ISBN", width="15")
Isbn_label.pack()
Isbn_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Isbn_text.pack()

Title_label = Label(window, text="Title", width="15")
Title_label.pack()
Title_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Title_text.pack()

Author_label = Label(window, text="Author", width="15")
Author_label.pack()
Author_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Author_text.pack()

Surname_label = Label(window, text="Surname", width="15")
Surname_label.pack()
Surname_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Surname_text.pack()

Edition_label = Label(window, text="Edition", width="15")
Edition_label.pack()
Edition_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Edition_text.pack()

Version_label = Label(window, text="Version", width="15")
Version_label.pack()
Version_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Version_text.pack()

Language_label = Label(window, text="Language", width="15")
Language_label.pack()
Language_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Language_text.pack()

Buy_label = Label(window, text="Buy Price", width="15")
Buy_label.pack()
Buy_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Buy_text.pack()

Instore_label = Label(window, text="InStore", width="15")
Instore_label.pack()
Instore_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Instore_text.pack()

Publisher_label = Label(window, text="Publisher", width="15")
Publisher_label.pack()
Publisher_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Publisher_text.pack()

Year_label = Label(window, text="Year", width="15")
Year_label.pack()
Year_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Year_text.pack()

Pages_label = Label(window, text="Pages", width="15")
Pages_label.pack()
Pages_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Pages_text.pack()

Booktype_label = Label(window, text="Book Type", width="15")
Booktype_label.pack()
Booktype_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Booktype_text.pack()

Location_label = Label(window, text="Location", width="15")
Location_label.pack()
Location_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Location_text.pack()

Section_label = Label(window, text="Section", width="15")
Section_label.pack()
Section_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Section_text.pack()

Genre_label = Label(window, text="Genre", width="15")
Genre_label.pack()
Genre_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Genre_text.pack()

# Buttons show hide
Translated_label = Label(window, text="Is it translated?", width="15", font='Helvetica 18 bold')
Yes = Button(window, text='Yes', command=yes_button)
Yes.pack(pady=20)
No = Button(window, text='No', command=no_button)
No.pack()

# show hide text and labels
Translator_label = Label(window, text="Translator", width="15")
Translator_label.pack()
Translator_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Translator_text.pack()

Untranslated_label = Label(window, text="Original Title", width="15")
Untranslated_label.pack()
Untranslated_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Untranslated_text.pack()

Origin_label = Label(window, text="Origin", width="15")
Origin_label.pack()
Origin_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Origin_text.pack()

# label and text place 1
Isbn_text.place(relx=0.2, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor=E)
Isbn_label.place(relx=0.2, rely=0.65, relwidth=rel_width, relheight=rel_height, anchor=E)
Title_text.place(relx=0.3, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor=E)
Title_label.place(relx=0.3, rely=0.65, relwidth=rel_width, relheight=rel_height, anchor=E)
Author_text.place(relx=0.4, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor=E)
Author_label.place(relx=0.4, rely=0.65, relwidth=rel_width, relheight=rel_height, anchor=E)
Surname_text.place(relx=0.5, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor=E)
Surname_label.place(relx=0.5, rely=0.65, relwidth=rel_width, relheight=rel_height, anchor=E)
Edition_text.place(relx=0.6, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor=E)
Edition_label.place(relx=0.6, rely=0.65, relwidth=rel_width, relheight=rel_height, anchor=E)
Version_text.place(relx=0.7, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor=E)
Version_label.place(relx=0.7, rely=0.65, relwidth=rel_width, relheight=rel_height, anchor=E)
Language_text.place(relx=0.8, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor=E)
Language_label.place(relx=0.8, rely=0.65, relwidth=rel_width, relheight=rel_height, anchor=E)
Buy_text.place(relx=0.9, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor=E)
Buy_label.place(relx=0.9, rely=0.65, relwidth=rel_width, relheight=rel_height, anchor=E)

# label and text place 2
Instore_text.place(relx=0.2, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor=E)
Instore_label.place(relx=0.2, rely=0.75, relwidth=rel_width, relheight=rel_height, anchor=E)
Publisher_text.place(relx=0.3, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor=E)
Publisher_label.place(relx=0.3, rely=0.75, relwidth=rel_width, relheight=rel_height, anchor=E)
Year_text.place(relx=0.4, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor=E)
Year_label.place(relx=0.4, rely=0.75, relwidth=rel_width, relheight=rel_height, anchor=E)
Pages_text.place(relx=0.5, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor=E)
Pages_label.place(relx=0.5, rely=0.75, relwidth=rel_width, relheight=rel_height, anchor=E)
Booktype_text.place(relx=0.6, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor=E)
Booktype_label.place(relx=0.6, rely=0.75, relwidth=rel_width, relheight=rel_height, anchor=E)
Location_text.place(relx=0.7, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor=E)
Location_label.place(relx=0.7, rely=0.75, relwidth=rel_width, relheight=rel_height, anchor=E)
Section_text.place(relx=0.8, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor=E)
Section_label.place(relx=0.8, rely=0.75, relwidth=rel_width, relheight=rel_height, anchor=E)
Genre_text.place(relx=0.9, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor=E)
Genre_label.place(relx=0.9, rely=0.75, relwidth=rel_width, relheight=rel_height, anchor=E)

# label and text place 3
Translator_text.place(relx=0.2, rely=0.9, relwidth=rel_width, relheight=rel_height, anchor=E)
Translator_label.place(relx=0.2, rely=0.85, relwidth=rel_width, relheight=rel_height, anchor=E)
Untranslated_text.place(relx=0.3, rely=0.9, relwidth=rel_width, relheight=rel_height, anchor=E)
Untranslated_label.place(relx=0.3, rely=0.85, relwidth=rel_width, relheight=rel_height, anchor=E)
Origin_text.place(relx=0.4, rely=0.9, relwidth=rel_width, relheight=rel_height, anchor=E)
Origin_label.place(relx=0.4, rely=0.85, relwidth=rel_width, relheight=rel_height, anchor=E)
Translated_label.place(relx=0.65, rely=0.85, relwidth=rel_width, relheight=rel_height, anchor=E)
Yes.place(relx=0.6, rely=0.9, relwidth=rel_width, relheight=rel_height, anchor=E)
No.place(relx=0.7, rely=0.9, relwidth=rel_width, relheight=rel_height, anchor=E)
Add.place(relx=0.9, rely=0.9, relwidth=rel_width, relheight=rel_height, anchor=E)

# label and text place 4
Isbn_text2.place(relx=0.2, rely=0.2, relwidth=rel_width, relheight=rel_height, anchor=E)
Isbn_label2.place(relx=0.2, rely=0.15, relwidth=rel_width, relheight=rel_height, anchor=E)
Search.place(relx=0.8, rely=0.2, relwidth=rel_width, relheight=rel_height, anchor=E)
Search_all.place(relx=0.9, rely=0.2, relwidth=rel_width, relheight=rel_height, anchor=E)

# label and text place 5
Set.place(relx=0.9, rely=0.55, relwidth=rel_width, relheight=rel_height, anchor=E)
Isbn_text3.place(relx=0.2, rely=0.55, relwidth=rel_width, relheight=rel_height, anchor=E)
Isbn_label3.place(relx=0.2, rely=0.5, relwidth=rel_width, relheight=rel_height, anchor=E)
Sell_Price_text.place(relx=0.3, rely=0.55, relwidth=rel_width, relheight=rel_height, anchor=E)
Sell_Price_label.place(relx=0.3, rely=0.5, relwidth=rel_width, relheight=rel_height, anchor=E)



window.mainloop()
