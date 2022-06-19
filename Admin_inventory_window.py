import tkinter as tk
from tkinter import ttk
import Start_window
# import Admin_inventory_window
import Admin_employee_window
import Admin_finance_window
from AdminClass import Admin, add_to_Price_exceptions
from datetime import date
from tkinter import OptionMenu, messagebox
# from book_search import book_search

emp_id = None
db = None

class Admin_inventory_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        rel_width = 0.1
        # rel_height = 0.05
        row_height = 20
        rel_width = 0.1
        rel_height = 0.05
        button_height = 45
        text_height = 20
        title_height = 30
        button_font = "Helvetica 18 bold"



        # Tabs
        Log_out = tk.Button(self, text="Log out", command=lambda: controller.show_frame(Start_window.Start_window))

        Employee = tk.Button(self, text="Employee", command=lambda: controller.show_frame(Admin_employee_window.Admin_employee_window))
        Finance = tk.Button(self, text="Finance", command= lambda: controller.show_frame(Admin_finance_window.Admin_finance_window))
        Inventory = tk.Button(self, text="Inventory", relief="sunken", state="disabled")


        # text
        Add_book = tk.Label(self, text="Add Book: ", font=button_font)
        Search_book = tk.Label(self, text="Search Book: ", font=button_font)
        Found_book = tk.Label(self, text="Results: ", font=button_font)
        Set_sellprice = tk.Label(self, text="Set new sell price: ", font=button_font)

        self.search_results = ttk.Treeview(self)
        # rest = "Title", "Author", "Surname", "Edition", "Comment", "Language", "Publisher", "Year", "Pages", "Book Type", "Location", "Section", "Genre", "Translator", "Original Title", "Original Title", "Origin"
        self.search_results['columns'] = ("ISBN","Comment", "Title [Original title]", "Author [Translator]",
                                     "Edition", "Language", "Genre", "Publisher",
                                     "Book Type", "Year", "Pages", "Place",

                                     # "Translator","Original Title", "Origin",
                                     "Price", "Amount")

        self.search_results.column("#0", width=20, stretch=False)
        self.search_results.column("ISBN", anchor="w", width=110, minwidth=50)
        self.search_results.column("Comment", anchor="w", width=100, minwidth=50)
        self.search_results.column("Title [Original title]", anchor="w", width=200, minwidth=100)
        self.search_results.column("Author [Translator]", anchor="w", width=100, minwidth=50)
        self.search_results.column("Edition", anchor="w", width=100, minwidth=50)
        # self.search_results.column("Comment", anchor="w", width=100)
        self.search_results.column("Language", anchor="w", width=100, minwidth=50)
        self.search_results.column("Genre", anchor="w", width=100, minwidth=50)
        self.search_results.column("Publisher", anchor="w", width=100, minwidth=50)
        self.search_results.column("Book Type", anchor="w", width=100, minwidth=50)
        self.search_results.column("Year", anchor="center", width=50, minwidth=25, stretch=False)
        self.search_results.column("Pages", anchor="center", width=50, minwidth=25, stretch=False)
        self.search_results.column("Place", anchor="center", width=50, minwidth=25, stretch=False)
        # self.search_results.column("Section", anchor="center", width=100)
        # self.search_results.column("Translator", anchor="center", width=100)
        # self.search_results.column("Original Title", anchor="center", width=100)
        # self.search_results.column("Origin", anchor="center", width=100)
        self.search_results.column("Price", anchor="center", width=50, minwidth=25, stretch=False)
        self.search_results.column("Amount", anchor="center", width=50, minwidth=25, stretch=False)

        self.search_results.heading("#0", text="", anchor="center")
        self.search_results.heading("ISBN",text="ISBN",  anchor="center")
        self.search_results.heading("Comment",text="Comment",  anchor="center")
        self.search_results.heading("Title [Original title]", text="Title [Original title]", anchor="center")
        self.search_results.heading("Author [Translator]", text="Author [Translator]", anchor="center")
        self.search_results.heading("Edition", text="Edition", anchor="center")
        # self.search_results.heading("Comment",text="Comment",  anchor="center")
        self.search_results.heading("Language", text="Language", anchor="center")
        self.search_results.heading("Genre", text="Genre", anchor="center")
        self.search_results.heading("Publisher", text="Publisher", anchor="center")
        self.search_results.heading("Book Type", text="Book Type", anchor="center")
        self.search_results.heading("Year", text="Year", anchor="center")
        self.search_results.heading("Pages", text="Pages", anchor="center")
        self.search_results.heading("Place", text="Place", anchor="center")
        # self.search_results.heading("Section",text="Section",  anchor="center")
        # self.search_results.heading("Translator",text="Translator",  anchor="center")
        # self.search_results.heading("Original Title", text="Original Title",  anchor="center")
        # self.search_results.heading("Origin", text="Origin",  anchor="center")
        self.search_results.heading("Price", text="Price", anchor="center")
        self.search_results.heading("Amount", text="Amount", anchor="center")

        self.search_results.place(relx=0.025, rely=0.25, relwidth=0.95, relheight=0.15)


        Set_sellprice.place(relx=0.2, rely=0.45, relwidth=rel_width, height=row_height, anchor="e")

                
        Save = tk.Button(self, text="Save", command=self.commit_save)
        Undo = tk.Button(self, text="Undo", command=self.rollback_undo)
        Add = tk.Button(self, text="Add", command=self.add_book) # for adding
        Set = tk.Button(self, text="Set", command=self.set_price_exception)
        Log_out = tk.Button(self, text="Log out", command=lambda: controller.show_frame(Start_window.Start_window))

        # place label
        Add_book.place(relx=0.2, rely=0.6, relwidth=rel_width, height=row_height, anchor="e")
        Search_book.place(relx=0.2, rely=0.1, relwidth=rel_width, height=row_height, anchor="e")

        # Place Buttons
        Employee.place(relx=1, relwidth=rel_width, height=button_height, anchor="ne")
        Finance.place(relx=0.9, relwidth=rel_width, height=button_height, anchor="ne")
        Inventory.place(relx=0.8, relwidth=rel_width, height=button_height, anchor="ne")
        Log_out.place(relx=0, rely=0, relwidth=rel_width, height=button_height, anchor="nw")
        
        Save.place(relx=1, rely=0.975, relwidth=rel_width, height=row_height, anchor="e")
        Undo.place(relx=0.9, rely=0.975, relwidth=rel_width, height=row_height, anchor="e")

        # text and labels
        Isbn_label2 = tk.Label(self, text="ISBN", width="15")
        Isbn_label2.pack()
        Isbn_text2 = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        Isbn_text2.pack()

        Isbn_label3 = tk.Label(self, text="ISBN", width="15")
        Isbn_label3.pack()
        self.Isbn_text3 = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Isbn_text3.pack()

        BookID_label3 = tk.Label(self, text="Book ID", width="15")
        BookID_label3.pack()
        self.BookID_entry3 = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.BookID_entry3.pack()

        Comment_Price_Exc = tk.Label(self, text="Comment", width="15")
        BookID_label3.pack()
        self.Comment_price_exc_entry = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Comment_price_exc_entry.pack()



        Sell_Price_label = tk.Label(self, text="Sell Price", width="15")
        Sell_Price_label.pack()
        self.Sell_Price_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Sell_Price_text.pack()

        Isbn_label = tk.Label(self, text="ISBN", width="15") #for add book
        Isbn_label.pack()
        self.Isbn_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        # Isbn_text.pack()

        Title_label = tk.Label(self, text="Title", width="15")
        Title_label.pack()
        self.Title_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Title_text.pack()

        Author_label = tk.Label(self, text="Author", width="15")
        Author_label.pack()
        self.Author_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Author_text.pack()

        Surname_label = tk.Label(self, text="Surname", width="15")
        Surname_label.pack()
        self.Surname_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Surname_text.pack()

        Edition_label = tk.Label(self, text="Edition", width="15")
        Edition_label.pack()
        self.Edition_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Edition_text.pack()

        Comment_label = tk.Label(self, text="Comment", width="15")
        Comment_label.pack()
        self.Comment_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Comment_text.pack()

        Language_label = tk.Label(self, text="Language", width="15")
        Language_label.pack()
        self.Language_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Language_text.pack()

        Buy_label = tk.Label(self, text="Buy Price", width="15")
        Buy_label.pack()
        self.Buy_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Buy_text.pack()

        Amount_label = tk.Label(self, text="Amount", width="15")
        Amount_label.pack()
        self.Amount_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Amount_text.pack()

        Publisher_label = tk.Label(self, text="Publisher", width="15")
        Publisher_label.pack()
        self.Publisher_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Publisher_text.pack()

        Year_label = tk.Label(self, text="Year", width="15")
        Year_label.pack()
        self.Year_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Year_text.pack()

        Pages_label = tk.Label(self, text="Pages", width="15")
        Pages_label.pack()
        self.Pages_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Pages_text.pack()

        Booktype_label = tk.Label(self, text="Book Type", width="15")
        Booktype_label.pack()
        
        clicked = tk.StringVar()
        clicked.set("Hardcopy")

        self.Booktype = tk.OptionMenu(self, self.clicked, "Hardcover", "Paperback")
        self.Booktype.pack()

        Location_label = tk.Label(self, text="Location", width="15")
        Location_label.pack()
        self.Location_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Location_text.pack()

        Section_label = tk.Label(self, text="Section", width="15")
        Section_label.pack()
        self.Section_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Section_text.pack()

        Genre_label = tk.Label(self, text="Genre", width="15")
        Genre_label.pack()
        self.Genre_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Genre_text.pack()

        # Buttons show hide
        self.Translated_label = tk.Label(self, text="Is it translated?", width="30", font=button_font)
        translated_yes = tk.Button(self, text='Yes', command=lambda: self.yes_button(rel_width, row_height))
        translated_yes.pack(pady=20)
        translated_no = tk.Button(self, text='No', command=self.no_button)
        translated_no.pack()

        # show hide text and labels
        self.Translator_label = tk.Label(self, text="Translator", width="15")
        self.Translator_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")

        self.Untranslated_label = tk.Label(self, text="Original Title", width="15")
        self.Untranslated_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")

        self.Origin_label = tk.Label(self, text="Origin", width="15")
        self.Origin_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")

        # label and text place 1
        self.Isbn_text.place(relx=0.2, rely=0.7, relwidth=rel_width, height=row_height, anchor="e")
        Isbn_label.place(relx=0.2, rely=0.65, relwidth=rel_width, height=row_height, anchor="e")
        self.Title_text.place(relx=0.3, rely=0.7, relwidth=rel_width, height=row_height, anchor="e")
        Title_label.place(relx=0.3, rely=0.65, relwidth=rel_width, height=row_height, anchor="e")
        self.Author_text.place(relx=0.4, rely=0.7, relwidth=rel_width, height=row_height, anchor="e")
        Author_label.place(relx=0.4, rely=0.65, relwidth=rel_width, height=row_height, anchor="e")
        self.Surname_text.place(relx=0.5, rely=0.7, relwidth=rel_width, height=row_height, anchor="e")
        Surname_label.place(relx=0.5, rely=0.65, relwidth=rel_width, height=row_height, anchor="e")
        self.Edition_text.place(relx=0.6, rely=0.7, relwidth=rel_width, height=row_height, anchor="e")
        Edition_label.place(relx=0.6, rely=0.65, relwidth=rel_width, height=row_height, anchor="e")
        self.Comment_text.place(relx=0.7, rely=0.7, relwidth=rel_width, height=row_height, anchor="e")
        Comment_label.place(relx=0.7, rely=0.65, relwidth=rel_width, height=row_height, anchor="e")
        self.Language_text.place(relx=0.8, rely=0.7, relwidth=rel_width, height=row_height, anchor="e")
        Language_label.place(relx=0.8, rely=0.65, relwidth=rel_width, height=row_height, anchor="e")
        self.Buy_text.place(relx=0.9, rely=0.7, relwidth=rel_width, height=row_height, anchor="e")
        Buy_label.place(relx=0.9, rely=0.65, relwidth=rel_width, height=row_height, anchor="e")

        # label and text place 2
        self.Amount_text.place(relx=0.2, rely=0.8, relwidth=rel_width, height=row_height, anchor="e")
        Amount_label.place(relx=0.2, rely=0.75, relwidth=rel_width, height=row_height, anchor="e")
        self.Publisher_text.place(relx=0.3, rely=0.8, relwidth=rel_width, height=row_height, anchor="e")
        Publisher_label.place(relx=0.3, rely=0.75, relwidth=rel_width, height=row_height, anchor="e")
        self.Year_text.place(relx=0.4, rely=0.8, relwidth=rel_width, height=row_height, anchor="e")
        Year_label.place(relx=0.4, rely=0.75, relwidth=rel_width, height=row_height, anchor="e")
        self.Pages_text.place(relx=0.5, rely=0.8, relwidth=rel_width, height=row_height, anchor="e")
        Pages_label.place(relx=0.5, rely=0.75, relwidth=rel_width, height=row_height, anchor="e")
        self.Booktype.place(relx=0.6, rely=0.8, relwidth=rel_width, height=row_height*0.85, anchor="e")
        Booktype_label.place(relx=0.6, rely=0.75, relwidth=rel_width, height=row_height, anchor="e")
        self.Location_text.place(relx=0.7, rely=0.8, relwidth=rel_width, height=row_height, anchor="e")
        Location_label.place(relx=0.7, rely=0.75, relwidth=rel_width, height=row_height, anchor="e")
        self.Section_text.place(relx=0.8, rely=0.8, relwidth=rel_width, height=row_height, anchor="e")
        Section_label.place(relx=0.8, rely=0.75, relwidth=rel_width, height=row_height, anchor="e")
        self.Genre_text.place(relx=0.9, rely=0.8, relwidth=rel_width, height=row_height, anchor="e")
        Genre_label.place(relx=0.9, rely=0.75, relwidth=rel_width, height=row_height, anchor="e")

        # label and text place 3
        self.Translated_label.place(relx=0.65, rely=0.85, relwidth=rel_width, height=row_height, anchor="e")
        translated_yes.place(relx=0.6, rely=0.9, relwidth=rel_width, height=row_height, anchor="e")
        translated_no.place(relx=0.7, rely=0.9, relwidth=rel_width, height=row_height, anchor="e")
        Add.place(relx=0.9, rely=0.9, relwidth=rel_width, height=row_height, anchor="e")

        # label and text place 4
        Isbn_text2.place(relx=0.2, rely=0.2, relwidth=rel_width, height=row_height, anchor="e")
        Isbn_label2.place(relx=0.2, rely=0.15, relwidth=rel_width, height=row_height, anchor="e")

        # label and text place 5
        Set.place(relx=0.9, rely=0.55, relwidth=rel_width, height=row_height, anchor="e")
        self.Isbn_text3.place(relx=0.2, rely=0.55, relwidth=rel_width, height=row_height, anchor="e")
        Isbn_label3.place(relx=0.2, rely=0.5, relwidth=rel_width, height=row_height, anchor="e")
        BookID_label3.place(relx=0.3, rely=0.5, relwidth=rel_width, height=row_height, anchor="e")
        self.BookID_entry3.place(relx=0.3, rely=0.55, relwidth=rel_width, height=row_height, anchor="e")
        Comment_Price_Exc.place(relx=0.4, rely=0.5, relwidth=rel_width, height=row_height, anchor="e")
        self.Comment_price_exc_entry.place(relx=0.4, rely=0.55, relwidth=rel_width, height=row_height, anchor="e")
        Sell_Price_label.place(relx=0.5, rely=0.5, relwidth=rel_width, height=row_height, anchor="e")
        self.Sell_Price_text.place(relx=0.5, rely=0.55, relwidth=rel_width, height=row_height, anchor="e")

    # button functions

    def yes_button(self, rel_width, row_height):
        try:
            self.Translator_text.destroy()
            self.Untranslated_label.destroy()
            self.Untranslated_text.destroy()
            self.Origin_text.destroy()
            self.Origin_label.destroy()
            self.Translator_label.destroy()
        except AttributeError:
            print("already exists")

        self.Translator_label = tk.Label(self, text="Translator", width="15")
        self.Translator_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Untranslated_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Untranslated_label = tk.Label(self, text="Original Title", width="15")
        self.Origin_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Origin_label = tk.Label(self, text="Origin", width="15")
        # self.Translated_label = tk.Label(self, text="Is it translated?", width="15", font=button_font)

        self.Translator_label.place(relx=0.2, rely=0.85, relwidth=rel_width, height=row_height, anchor="e")
        self.Translator_text.place(relx=0.2, rely=0.9, relwidth=rel_width, height=row_height, anchor="e")
        self.Untranslated_text.place(relx=0.3, rely=0.9, relwidth=rel_width, height=row_height, anchor="e")
        self.Untranslated_label.place(relx=0.3, rely=0.85, relwidth=rel_width, height=row_height, anchor="e")
        self.Origin_text.place(relx=0.4, rely=0.9, relwidth=rel_width, height=row_height, anchor="e")
        self.Origin_label.place(relx=0.4, rely=0.85, relwidth=rel_width, height=row_height, anchor="e")
        print("hello")
        print(emp_id)

    def no_button(self):
        self.Translator_text.destroy()
        self.Untranslated_label.destroy()
        self.Untranslated_text.destroy()
        self.Origin_text.destroy()
        self.Origin_label.destroy()
        self.Translator_label.destroy()

        self.Translator_label = tk.Label(self, text="Translator", width="15")
        self.Translator_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Untranslated_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Untranslated_label = tk.Label(self, text="Original Title", width="15")
        self.Origin_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Origin_label = tk.Label(self, text="Origin", width="15")

    def open_employee_window(self):
        print("to be added")

    def add_book(self):
        ISBN = self.Isbn_text.get()
        Title = self.Title_text.get()
        Author = self.Author_text.get()
        Surname = self.Surname_text.get()
        Edition = self.Edition_text.get()
        Comment = self.Comment_text.get()
        Language = self.Language_text.get()
        Buy_price = int(self.Buy_text.get())
        Amount = int(self.Amount_text.get()) #what is it for?
        Publisher = self.Publisher_text.get()
        Year = self.Year_text.get()
        Pages = self.Pages_text.get()
        Booktype = self.clicked.get()
        Location = self.Location_text.get()
        Section = self.Section_text.get()
        Genre = self.Genre_text.get()

        Date = date.today()

        Translator = self.Translator_text.get()
        if Translator == "":
            Translator = None
        Original_title = self.Untranslated_text.get()
        if Original_title == "":
            Original_title = None
        Origin = self.Origin_text.get()
        if Origin == "":
            Origin = None

        # Comment = "Bruh"


        resp = messagebox.askquestion('Confirmation', 'Are you sure you want to save this book?')
        messagebox.askquestion("Confirmation", "Are you sure?")
        mycursor = db.cursor()
        if resp == "yes":
            print(Translator, Original_title, Origin)
            Admin_object = Admin(db)
            try:
                Admin_object.add_book(ISBN, Title, Author, Surname, Publisher, Year, Pages, Language, Booktype,
                                      Location, Section, Genre, emp_id, Date, Buy_price, Comment, Translator,
                                      Original_title,
                                      Origin, Edition, Amount)
                self.Booktype_listbox.config(fg="black")
            except UnboundLocalError:
                print("Here")
                self.Booktype_listbox.config(fg="red")
            print(ISBN, Title, Author, Surname, Edition, Comment, Language, Buy_price)
            print(Publisher, Year, Pages, Booktype, Location, Section, Genre)
            print("Book has been added\nmake this a label that shows up.")
        else:
            print("Book has not been added.")
    def commit_save(self):
        resp = messagebox.askquestion('Confirmation', 'Are you sure you want to commit?')
        mycursor = db.cursor()
        if resp=="yes":
            mycursor.execute("commit")
        else:
            print("It doesn't commit")
    def rollback_undo(self):
        resp = messagebox.askquestion('Confirmation', 'This will rollback your transaction progress. Do you want to continue?')
        mycursor = db.cursor()
        if resp == "yes":
            mycursor.execute("rollback")
        else:
            print("It doesn't rollback")
    def set_price_exception(self):
        ISBN = self.Isbn_text3.get()
        if ISBN == "":
            ISBN = None
        Book_ID = self.BookID_entry3.get()
        if Book_ID == "":
            Book_ID = None
        else:
            Book_ID = int(Book_ID)

        New_price = int(self.Sell_Price_text.get())
        Comment = str(self.Comment_price_exc_entry.get())
        print(Book_ID,New_price, Comment)
        Admin_object = Admin(db)
        query = Admin_object.add_price_exception(newprice=New_price,ISBN=ISBN,book_id=Book_ID,comment=Comment)
        print(query)
        resp = messagebox.askquestion('Confirmation', f'Are you sure, you want to change price of this book to {New_price/100}€ ?')
        mycursor = db.cursor()
        if resp == "yes":
            mycursor.execute(query)
            print("Book has been added\nmake this a label that shows up.")
        else:
            print("Book hasn't been added")