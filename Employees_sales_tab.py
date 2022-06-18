import tkinter as tk
import Start_window
from tkinter import ttk

emp_id = None

class Employee_sales_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        rel_width = 0.1
        rel_height = 0.05

# window = Tk()
# window.geometry("800x400")
# window.title("Employee sales tab")

        Search = tk.Button(self, text="Search")
        Search.place(relx=0.4, rely=0.35, relwidth=rel_width, relheight=0.1, anchor="e")

        Sell = tk.Button(self, text="Sell")
        Sell.place(relx=1, rely=0.9, relwidth=rel_width, relheight=0.1, anchor="e")

        Log_out = tk.Button(self, text="Log out",
                            command=lambda: controller.show_frame(Start_window.Start_window))
        Log_out.place(relx=1, rely=0, relwidth=rel_width,relheight=0.1, anchor="ne")

        Book_label = tk.Label(self, text="Book ID", width = "15")
        Book_label.pack()
        Book_text = tk.Text(self, borderwidth=1, relief="groove")
        Book_text.pack()
        Book_text.place(relx=0.3, rely=0.35, relwidth=0.2, relheight=0.1, anchor="e")
        Book_label.place(relx=0.2, rely=0.25, relwidth=rel_width, relheight=rel_height, anchor="e")


        Book_search = tk.Label(self, text="Book search: ", font='Helvetica 18 bold')
        Found = tk.Label(self, text="Found: ", font='Helvetica 18 bold')
        # Title = tk.Label(self, text="Title")
        # Author = tk.Label(self, text="Author")
        # Edition = tk.Label(self, text="Edition")
        # Version = tk.Label(self, text="Version")
        # Location = tk.Label(self, text="Location")
        # Section = tk.Label(self, text="Section")
        # Language = tk.Label(self, text="Language")
        # Sell_price = tk.Label(self, text="SellPrice")
        # In_store = tk.Label(self, text="InStore")


        Book_search.place(relx=0.25, rely=0.1, relwidth=0.2, relheight=rel_height, anchor="e")
        Found.place(relx=0.2, rely=0.5, relwidth=0.2, relheight=rel_height, anchor="e")
        # Title.place(relx=0.1, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor="e")
        # Author.place(relx=0.2, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor="e")
        # Edition.place(relx=0.3, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor="e")
        # Version.place(relx=0.4, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor="e")
        # Location.place(relx=0.5, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor="e")
        # Section.place(relx=0.6, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor="e")
        # Language.place(relx=0.7, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor="e")
        # Sell_price.place(relx=0.8, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor="e")
        # In_store.place(relx=0.9, rely=0.7, relwidth=rel_width, relheight=rel_height, anchor="e")

        search_results = ttk.Treeview(self)
        # rest = "Title", "Author", "Surname", "Edition", "Comment", "Language", "Publisher", "Year", "Pages", "Book Type", "Location", "Section", "Genre", "Translator", "Original Title", "Original Title", "Origin"
        search_results['columns'] = ("ISBN", "Comment", "Title [Original title]", "Author [Translator]",
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

        self.search_results.insert(parent='', index='end', iid=0,
                              values=("9780593334833", "Book overview", "Book Lovers", "Emily Henry",
                                      "NULL", "English",
                                      "Sisters Fiction, Romantic Comedy", "Berkley",
                                      "paperback",
                                      "2022", "400", "17-18",
                                      "1479", "2"))
        self.search_results.insert(parent='0', index='end', iid=1,
                              values=("9780593334833", "Discount due to damaged cover", "Book Lovers", "Emily Henry",
                                      "NULL", "English",
                                      "Sisters Fiction, Romantic Comedy", "Berkley",
                                      "paperback",
                                      "2022", "400", "17-18",
                                      "1479", "1"))
        self.search_results.insert(parent='0', index='end', iid=2,
                              values=("9780593334833", "No comment", "Book Lovers", "Emily Henry",
                                      "NULL", "English",
                                      "Sisters Fiction, Romantic Comedy", "Berkley",
                                      "paperback",
                                      "2022", "400", "17-18",
                                      "1479", "1"))

        # window.mainloop()

