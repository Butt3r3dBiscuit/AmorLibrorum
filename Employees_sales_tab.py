import tkinter as tk
from tkinter import ttk
import Start_window
from AdminClass import Admin
from book_search import book_search

emp_id = None
db = None

class Employee_sales_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        rel_width = 0.1
        rel_height = 0.05
        button_font = "Helvetica 18 bold"

        Search = tk.Button(self, text="Search", command=self.search)
        Search.place(relx=0.4, rely=0.35, relwidth=rel_width, height=45, anchor="e")

        Sell = tk.Button(self, text="Sell", command=self.sell)
        Sell.place(relx=1, rely=0.9, relwidth=rel_width, height=45, anchor="e")

        Log_out = tk.Button(self, text="Log out", command=lambda: self.log_out(controller))
        Log_out.place(relx=0, rely=0, relwidth=rel_width, height=45, anchor="nw")


        Book_label = tk.Label(self, text="Book ID", width="15")
        Book_label.place(relx=0.2, rely=0.25, relwidth=rel_width, relheight=rel_height, anchor="e")

        self.Book_text = tk.Entry(self, borderwidth=1, relief="groove")
        self.Book_text.place(relx=0.3, rely=0.35, relwidth=0.2, height=45, anchor="e")

        Book_search = tk.Label(self, text="Book search: ", font=button_font)
        Found = tk.Label(self, text="Found: ", font=button_font)

        Book_search.place(relx=0.25, rely=0.1, relwidth=rel_width*2, relheight=rel_height, anchor="e")
        Found.place(relx=0.2, rely=0.5, relwidth=rel_width*2, relheight=rel_height, anchor="e")
        
        self.search_results = ttk.Treeview(self)
        self.search_results['columns'] = ("ISBN", "Comment", "Title [Original title]", "Author [Translator]",
                                     "Edition", "Language", "Genre", "Publisher",
                                     "Book Type", "Year", "Pages", "Place",
                                     "Price", "Amount")

        self.search_results.column("#0", width=20, stretch=False)
        self.search_results.column("ISBN", anchor="w", width=110, minwidth=50)
        self.search_results.column("Comment", anchor="w", width=100, minwidth=50)
        self.search_results.column("Title [Original title]", anchor="w", width=200, minwidth=100)
        self.search_results.column("Author [Translator]", anchor="w", width=100, minwidth=50)
        self.search_results.column("Edition", anchor="w", width=100, minwidth=50)
        self.search_results.column("Language", anchor="w", width=100, minwidth=50)
        self.search_results.column("Genre", anchor="w", width=100, minwidth=50)
        self.search_results.column("Publisher", anchor="w", width=100, minwidth=50)
        self.search_results.column("Book Type", anchor="w", width=100, minwidth=50)
        self.search_results.column("Year", anchor="center", width=50, minwidth=25, stretch=False)
        self.search_results.column("Pages", anchor="center", width=50, minwidth=25, stretch=False)
        self.search_results.column("Place", anchor="center", width=50, minwidth=25, stretch=False)
        self.search_results.column("Price", anchor="center", width=50, minwidth=25, stretch=False)
        self.search_results.column("Amount", anchor="center", width=50, minwidth=25, stretch=False)

        self.search_results.heading("#0", text="", anchor="center")
        self.search_results.heading("ISBN", text="ISBN", anchor="center")
        self.search_results.heading("Comment", text="Comment", anchor="center")
        self.search_results.heading("Title [Original title]", text="Title [Original title]", anchor="center")
        self.search_results.heading("Author [Translator]", text="Author [Translator]", anchor="center")
        self.search_results.heading("Edition", text="Edition", anchor="center")
        self.search_results.heading("Language", text="Language", anchor="center")
        self.search_results.heading("Genre", text="Genre", anchor="center")
        self.search_results.heading("Publisher", text="Publisher", anchor="center")
        self.search_results.heading("Book Type", text="Book Type", anchor="center")
        self.search_results.heading("Year", text="Year", anchor="center")
        self.search_results.heading("Pages", text="Pages", anchor="center")
        self.search_results.heading("Place", text="Place", anchor="center")
        self.search_results.heading("Price", text="Price", anchor="center")
        self.search_results.heading("Amount", text="Amount", anchor="center")

        self.search_results.place(relx=0.025, rely=0.55, relwidth=0.95, relheight=0.25)


    def search(self):
        self.clean_up()
        for record in self.search_results.get_children():
            self.search_results.delete(record)
        Book_ID_input = self.Book_text.get()
        b = book_search(book_id=Book_ID_input,db=db)
        if b == [] or b == 1064:
            self.error_label = tk.Label(
                self, text="Book not found", width="15", fg="red")
            self.error_label.place(relx=0.4, rely=0.335)
        try:
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
        except TypeError:
            print("No input")

    def log_out(self, controller):
        controller.show_frame(Start_window.Start_window)
        self.clean_up()

    def clean_up(self):
        try:
            self.error_label.destroy()
        except AttributeError:
            pass
        try:
            self.error_label_sell_pos.destroy()
        except AttributeError:
            pass
        try:
            self.error_label_sell_neg.destroy()
        except AttributeError:
            pass

    def sell(self):
        book_id = self.Book_text.get()
        try:
            Admin_object = Admin(db)
            Admin_object.sell(book_id=book_id,employee_id=emp_id)
            self.error_label_sell_pos = tk.Label(
                self, text="Book sold", width="15", fg="green")
            self.error_label_sell_pos.place(relx=0.4, rely=0.335)
        except Exception as e:
            if e.errno==1644:
                self.error_label_sell_neg = tk.Label(
                    self, text="Book already sold", width="15", fg="red")
                self.error_label_sell_neg.place(relx=0.4, rely=0.335)
