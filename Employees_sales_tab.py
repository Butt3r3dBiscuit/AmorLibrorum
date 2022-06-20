import tkinter as tk
from tkinter import ttk
import Start_window
# import Admin_inventory_window
# import Admin_employee_window
# import Admin_finance_window
# from AdminClass import Admin, add_to_Price_exceptions
# from datetime import date
# from tkinter import OptionMenu, messagebox
from book_search import book_search

emp_id = None
db = None

class Employee_sales_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        rel_width = 0.1
        rel_height = 0.05
        row_height = 20
        button_height = 45
        text_height = 20
        title_height = 30
        button_font = "Helvetica 18 bold"

        Search = tk.Button(self, text="Search", command=self.search)
        Search.place(relx=0.4, rely=0.35, relwidth=rel_width, height=45, anchor="e")

        Sell = tk.Button(self, text="Sell")
        Sell.place(relx=1, rely=0.9, relwidth=rel_width, height=45, anchor="e")

        Log_out = tk.Button(self, text="Log out", command=lambda: self.log_out(controller))
        Log_out.place(relx=0, rely=0, relwidth=rel_width, height=45, anchor="nw")


        Book_label = tk.Label(self, text="Book ID", width="15")
        Book_label.place(relx=0.2, rely=0.25, relwidth=rel_width, relheight=rel_height, anchor="e")
        # Book_label.pack()

        self.Book_text = tk.Entry(self, borderwidth=1, relief="groove")
        self.Book_text.place(relx=0.3, rely=0.35, relwidth=0.2, height=45, anchor="e")
        # self.enter_your_book_id_here_pls.pack()


        Book_search = tk.Label(self, text="Book search: ", font=button_font)
        Found = tk.Label(self, text="Found: ", font=button_font)


        Book_search.place(relx=0.25, rely=0.1, relwidth=rel_width*2, relheight=rel_height, anchor="e")
        Found.place(relx=0.2, rely=0.5, relwidth=rel_width*2, relheight=rel_height, anchor="e")
        

        self.search_results = ttk.Treeview(self)
        # rest = "Title", "Author", "Surname", "Edition", "Comment", "Language", "Publisher", "Year", "Pages", "Book Type", "Location", "Section", "Genre", "Translator", "Original Title", "Original Title", "Origin"
        self.search_results['columns'] = ("ISBN", "Comment", "Title [Original title]", "Author [Translator]",
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
        self.search_results.heading("ISBN", text="ISBN", anchor="center")
        self.search_results.heading("Comment", text="Comment", anchor="center")
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

        self.search_results.place(relx=0.025, rely=0.55, relwidth=0.95, relheight=0.25)


    def search(self):
        try:
            self.error_label.destroy()
        except AttributeError:
            pass
        for record in self.search_results.get_children():
            self.search_results.delete(record)
        Book_ID_input = self.Book_text.get()
        b = book_search(book_id=Book_ID_input,db=db)
        print(b)
        if b == []:
            self.error_label = tk.Label(
                self, text="Book not found", width="15", fg="red")
            self.error_label.place(relx=0.4, rely=0.335)

        m = len(b)
        count = 0
        parent = ''
        for i in range(m):
            n = len(b[i])
            values = []
            for j in range(n):
                if j == 2 or j == 8:
                    if b[i][j + 1] != None:
                        values.append(f"{b[i][j]} [{b[i][j + 1]}]")
                    else:
                        values.append(b[i][j])
                elif j == 4:
                    if b[i][j + 2] != None:
                        values.append(f"{b[i][j]} {b[i][j + 1]} [{b[i][j + 2]}]")
                    else:
                        values.append(f"{b[i][j]} {b[i][j + 1]}")
                elif j == 15:
                    values.append(f"{b[i][j]}-{b[i][j + 1]}")
                elif j not in (3, 5, 6, 9, 16):
                    if b[i][j] != None:
                        values.append(b[i][j])
                    else:
                        values.append('')
            self.search_results.insert(parent=parent, index='end', iid=str(count), values=values)
            count += 1

    def log_out(self, controller):
        controller.show_frame(Start_window.Start_window)
        try:
            self.error_label.destroy()
        except AttributeError:
            pass