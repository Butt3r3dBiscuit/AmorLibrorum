import tkinter as tk
import Start_window

# to be added - other windows

class Admin_inventory_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        rel_width = 0.1
        rel_height = 0.05

        # Window
        # window = Tk()
        # width = window.winfo_screenwidth()
        # height = window.winfo_screenheight()
        # window.geometry("%dx%d" % (width, height))
        # window.title("Inventory Window")
        #test push

        # text
        Add_book = tk.Label(self, text="Add Book: ", font='Helvetica 18 bold')
        Search_book = tk.Label(self, text="Search Book: ", font='Helvetica 18 bold')
        Found_book = tk.Label(self, text="Books Found: ", font='Helvetica 18 bold')
        Set_sellprice = tk.Label(self, text="Set Sellprice: ", font='Helvetica 18 bold')

        Title = tk.Label(self, text="Title")
        Author = tk.Label(self, text="Author")
        Edition = tk.Label(self, text="Edition")
        Version = tk.Label(self, text="Version")
        Buy_price = tk.Label(self, text="BuyPrice")
        Sell_price = tk.Label(self, text="SellPrice")
        In_store = tk.Label(self, text="InStore")

        # text place
        Found_book.place(relx=0.2, rely=0.25, relwidth=rel_width, relheight=rel_height, anchor="e")
        Title.place(relx=0.2, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor="e")
        Author.place(relx=0.3, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor="e")
        Edition.place(relx=0.4, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor="e")
        Version.place(relx=0.5, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor="e")
        Buy_price.place(relx=0.6, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor="e")
        Sell_price.place(relx=0.7, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor="e")
        In_store.place(relx=0.8, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor="e")
        Set_sellprice.place(relx=0.2, rely=0.45, relwidth=rel_width, relheight=rel_height, anchor="e")

        # Buttons
        Employee = tk.Button(self, text="Employee", command=self.open_employee_window)
        Finance = tk.Button(self, text="Finance")
        Inventory = tk.Button(self, text="Inventory")
        Save = tk.Button(self, text="Save")
        Undo = tk.Button(self, text="Undo")
        Add = tk.Button(self, text="Add")
        Search = tk.Button(self, text="Search")
        Search_all = tk.Button(self, text="Search All")
        Set = tk.Button(self, text="Set")
        Log_out = tk.Button(self, text="Log out", command=lambda: controller.show_frame(Start_window.Start_window))

        # place label
        Add_book.place(relx=0.2, rely=0.6, relwidth=rel_width, relheight=rel_height, anchor="e")
        Search_book.place(relx=0.2, rely=0.1, relwidth=rel_width, relheight=rel_height, anchor="e")

        # Place Buttons
        Employee.place(relx=1, relwidth=rel_width, relheight=rel_height, anchor="ne")
        Finance.place(relx=0.9, relwidth=rel_width, relheight=rel_height, anchor="ne")
        Inventory.place(relx=0.8, relwidth=rel_width, relheight=rel_height, anchor="ne")
        Save.place(relx=1, rely=0.975, relwidth=rel_width, relheight=rel_height, anchor="e")
        Undo.place(relx=0.9, rely=0.975, relwidth=rel_width, relheight=rel_height, anchor="e")
        Log_out.place(relx=0,rely=0,relwidth=rel_width, relheight=rel_height, anchor="nw")

        # text and labels
        Sell_Price_label = tk.Label(self, text="Sell Price", width="15")
        Sell_Price_label.pack()
        Sell_Price_text = tk.Text(self, height=0.5, width=30, borderwidth=1, relief="groove")
        Sell_Price_text.pack()

        Isbn_label3 = tk.Label(self, text="ISBN", width="15")
        Isbn_label3.pack()
        Isbn_text3 = tk.Text(self, height=0.5, width=30, borderwidth=1, relief="groove")
        Isbn_text3.pack()

        Isbn_label2 = tk.Label(self, text="ISBN", width="15")
        Isbn_label2.pack()
        Isbn_text2 = tk.Text(self, height=0.5, width=30, borderwidth=1, relief="groove")
        Isbn_text2.pack()

        Isbn_label = tk.Label(self, text="ISBN", width="15")
        Isbn_label.pack()
        Isbn_text = tk.Text(self, height=0.5, width=30, borderwidth=1, relief="groove")
        Isbn_text.pack()

        Title_label = tk.Label(self, text="Title", width="15")
        Title_label.pack()
        Title_text = tk.Text(self, height=0.5, width=30, borderwidth=1, relief="groove")
        Title_text.pack()

        Author_label = tk.Label(self, text="Author", width="15")
        Author_label.pack()
        Author_text = tk.Text(self, height=0.5, width=30, borderwidth=1, relief="groove")
        Author_text.pack()

        Surname_label = tk.Label(self, text="Surname", width="15")
        Surname_label.pack()
        Surname_text = tk.Text(self, height=0.5, width=30, borderwidth=1, relief="groove")
        Surname_text.pack()

        Edition_label = tk.Label(self, text="Edition", width="15")
        Edition_label.pack()
        Edition_text = tk.Text(self, height=0.5, width=30, borderwidth=1, relief="groove")
        Edition_text.pack()

        Version_label = tk.Label(self, text="Version", width="15")
        Version_label.pack()
        Version_text = tk.Text(self, height=0.5, width=30, borderwidth=1, relief="groove")
        Version_text.pack()

        Language_label = tk.Label(self, text="Language", width="15")
        Language_label.pack()
        Language_text = tk.Text(self, height=0.5, width=30, borderwidth=1, relief="groove")
        Language_text.pack()

        Buy_label = tk.Label(self, text="Buy Price", width="15")
        Buy_label.pack()
        Buy_text = tk.Text(self, height=0.5, width=30, borderwidth=1, relief="groove")
        Buy_text.pack()

        Instore_label = tk.Label(self, text="InStore", width="15")
        Instore_label.pack()
        Instore_text = tk.Text(self, height=0.5, width=30, borderwidth=1, relief="groove")
        Instore_text.pack()

        Publisher_label = tk.Label(self, text="Publisher", width="15")
        Publisher_label.pack()
        Publisher_text = tk.Text(self, height=0.5, width=30, borderwidth=1, relief="groove")
        Publisher_text.pack()

        Year_label = tk.Label(self, text="Year", width="15")
        Year_label.pack()
        Year_text = tk.Text(self, height=0.5, width=30, borderwidth=1, relief="groove")
        Year_text.pack()

        Pages_label = tk.Label(self, text="Pages", width="15")
        Pages_label.pack()
        Pages_text = tk.Text(self, height=0.5, width=30, borderwidth=1, relief="groove")
        Pages_text.pack()

        Booktype_label = tk.Label(self, text="Book Type", width="15")
        Booktype_label.pack()
        Booktype_text = tk.Text(self, height=0.5, width=30, borderwidth=1, relief="groove")
        Booktype_text.pack()

        Location_label = tk.Label(self, text="Location", width="15")
        Location_label.pack()
        Location_text = tk.Text(self, height=0.5, width=30, borderwidth=1, relief="groove")
        Location_text.pack()

        Section_label = tk.Label(self, text="Section", width="15")
        Section_label.pack()
        Section_text = tk.Text(self, height=0.5, width=30, borderwidth=1, relief="groove")
        Section_text.pack()

        Genre_label = tk.Label(self, text="Genre", width="15")
        Genre_label.pack()
        Genre_text = tk.Text(self, height=0.5, width=30, borderwidth=1, relief="groove")
        Genre_text.pack()

        # Buttons show hide
        self.Translated_label = tk.Label(self, text="Is it translated?", width="15", font='Helvetica 18 bold')
        Yes = tk.Button(self, text='Yes', command=self.yes_button)
        Yes.pack(pady=20)
        No = tk.Button(self, text='No', command=self.no_button)
        No.pack()

        # show hide text and labels
        Translator_label = tk.Label(self, text="Translator", width="15")
        Translator_label.pack()
        self.Translator_text = tk.Text(self, height=0.5, width=30, borderwidth=1, relief="groove")
        self.Translator_text.pack()

        self.Untranslated_label = tk.Label(self, text="Original Title", width="15")
        self.Untranslated_label.pack()
        self.Untranslated_text = tk.Text(self, height=0.5, width=30, borderwidth=1, relief="groove")
        self.Untranslated_text.pack()

        self.Origin_label = tk.Label(self, text="Origin", width="15")
        self.Origin_label.pack()
        self.Origin_text = tk.Text(self, height=0.5, width=30, borderwidth=1, relief="groove")
        self.Origin_text.pack()

        # label and text place 1
        Isbn_text.place(relx=0.2, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor="e")
        Isbn_label.place(relx=0.2, rely=0.65, relwidth=rel_width, relheight=rel_height, anchor="e")
        Title_text.place(relx=0.3, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor="e")
        Title_label.place(relx=0.3, rely=0.65, relwidth=rel_width, relheight=rel_height, anchor="e")
        Author_text.place(relx=0.4, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor="e")
        Author_label.place(relx=0.4, rely=0.65, relwidth=rel_width, relheight=rel_height, anchor="e")
        Surname_text.place(relx=0.5, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor="e")
        Surname_label.place(relx=0.5, rely=0.65, relwidth=rel_width, relheight=rel_height, anchor="e")
        Edition_text.place(relx=0.6, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor="e")
        Edition_label.place(relx=0.6, rely=0.65, relwidth=rel_width, relheight=rel_height, anchor="e")
        Version_text.place(relx=0.7, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor="e")
        Version_label.place(relx=0.7, rely=0.65, relwidth=rel_width, relheight=rel_height, anchor="e")
        Language_text.place(relx=0.8, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor="e")
        Language_label.place(relx=0.8, rely=0.65, relwidth=rel_width, relheight=rel_height, anchor="e")
        Buy_text.place(relx=0.9, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor="e")
        Buy_label.place(relx=0.9, rely=0.65, relwidth=rel_width, relheight=rel_height, anchor="e")

        # label and text place 2
        Instore_text.place(relx=0.2, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")
        Instore_label.place(relx=0.2, rely=0.75, relwidth=rel_width, relheight=rel_height, anchor="e")
        Publisher_text.place(relx=0.3, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")
        Publisher_label.place(relx=0.3, rely=0.75, relwidth=rel_width, relheight=rel_height, anchor="e")
        Year_text.place(relx=0.4, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")
        Year_label.place(relx=0.4, rely=0.75, relwidth=rel_width, relheight=rel_height, anchor="e")
        Pages_text.place(relx=0.5, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")
        Pages_label.place(relx=0.5, rely=0.75, relwidth=rel_width, relheight=rel_height, anchor="e")
        Booktype_text.place(relx=0.6, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")
        Booktype_label.place(relx=0.6, rely=0.75, relwidth=rel_width, relheight=rel_height, anchor="e")
        Location_text.place(relx=0.7, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")
        Location_label.place(relx=0.7, rely=0.75, relwidth=rel_width, relheight=rel_height, anchor="e")
        Section_text.place(relx=0.8, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")
        Section_label.place(relx=0.8, rely=0.75, relwidth=rel_width, relheight=rel_height, anchor="e")
        Genre_text.place(relx=0.9, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")
        Genre_label.place(relx=0.9, rely=0.75, relwidth=rel_width, relheight=rel_height, anchor="e")

        # label and text place 3
        self.Translator_text.place(relx=0.2, rely=0.9, relwidth=rel_width, relheight=rel_height, anchor="e")
        Translator_label.place(relx=0.2, rely=0.85, relwidth=rel_width, relheight=rel_height, anchor="e")
        self.Untranslated_text.place(relx=0.3, rely=0.9, relwidth=rel_width, relheight=rel_height, anchor="e")
        self.Untranslated_label.place(relx=0.3, rely=0.85, relwidth=rel_width, relheight=rel_height, anchor="e")
        self.Origin_text.place(relx=0.4, rely=0.9, relwidth=rel_width, relheight=rel_height, anchor="e")
        self.Origin_label.place(relx=0.4, rely=0.85, relwidth=rel_width, relheight=rel_height, anchor="e")
        self.Translated_label.place(relx=0.65, rely=0.85, relwidth=rel_width, relheight=rel_height, anchor="e")
        Yes.place(relx=0.6, rely=0.9, relwidth=rel_width, relheight=rel_height, anchor="e")
        No.place(relx=0.7, rely=0.9, relwidth=rel_width, relheight=rel_height, anchor="e")
        Add.place(relx=0.9, rely=0.9, relwidth=rel_width, relheight=rel_height, anchor="e")

        # label and text place 4
        Isbn_text2.place(relx=0.2, rely=0.2, relwidth=rel_width, relheight=rel_height, anchor="e")
        Isbn_label2.place(relx=0.2, rely=0.15, relwidth=rel_width, relheight=rel_height, anchor="e")
        Search.place(relx=0.8, rely=0.2, relwidth=rel_width, relheight=rel_height, anchor="e")
        Search_all.place(relx=0.9, rely=0.2, relwidth=rel_width, relheight=rel_height, anchor="e")

        # label and text place 5
        Set.place(relx=0.9, rely=0.55, relwidth=rel_width, relheight=rel_height, anchor="e")
        Isbn_text3.place(relx=0.2, rely=0.55, relwidth=rel_width, relheight=rel_height, anchor="e")
        Isbn_label3.place(relx=0.2, rely=0.5, relwidth=rel_width, relheight=rel_height, anchor="e")
        Sell_Price_text.place(relx=0.3, rely=0.55, relwidth=rel_width, relheight=rel_height, anchor="e")
        Sell_Price_label.place(relx=0.3, rely=0.5, relwidth=rel_width, relheight=rel_height, anchor="e")

    # button functions

    def yes_button(self):
        self.Translated_label.pack()
        self.Translator_text.pack()
        self.Untranslated_label.pack()
        self.Untranslated_text.pack()
        self.Origin_text.pack()
        self.Origin_label.pack()

    def no_button(self):
        self.Translated_label.pack_forget()
        self.Translator_text.pack_forget()
        self.Untranslated_label.pack_forget()
        self.Untranslated_text.pack_forget()
        self.Origin_text.pack_forget()
        self.Origin_label.pack_forget()

    def open_employee_window(self):
        print("to be added")