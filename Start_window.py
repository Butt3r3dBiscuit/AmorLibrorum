import tkinter as tk
from tkinter import ttk
import login_window
import guest_class as gc


class Start_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        rel_width = 0.1
        rel_height = 0.2

        # tk.title("Book search")

        # window = Tk()
        # window.geometry("800x400")
        # window.title("start Window")

        self.search_results = ttk.Treeview(self)
        # rest = "Title", "Author", "Surname", "Edition", "Comment", "Language", "Publisher", "Year", "Pages", "Book Type", "Location", "Section", "Genre", "Translator", "Original Title", "Original Title", "Origin"
        self.search_results['columns'] = ("Title [Original title]", "Author [Translator]",
                                     "Edition", "Language","Genre", "Publisher",
                                     "Book Type","Year", "Pages", "Place",

                                     # "Translator","Original Title", "Origin",
                                     "Price", "Amount")

        self.search_results.column("#0", width=20)
        # self.search_results.column("ISBN", anchor="center", width=120)
        self.search_results.column("Title [Original title]", anchor="w", width=200)
        self.search_results.column("Author [Translator]", anchor="w", width=100)
        self.search_results.column("Edition", anchor="w", width=100)
        # self.search_results.column("Comment", anchor="w", width=100)
        self.search_results.column("Language", anchor="w", width=100)
        self.search_results.column("Genre", anchor="w", width=100)
        self.search_results.column("Publisher", anchor="w", width=100)
        self.search_results.column("Book Type", anchor="w", width=100)
        self.search_results.column("Year", anchor="center", width=50)
        self.search_results.column("Pages", anchor="center", width=50)
        self.search_results.column("Place", anchor="center", width=50)
        # self.search_results.column("Section", anchor="center", width=100)
        # self.search_results.column("Translator", anchor="center", width=100)
        # self.search_results.column("Original Title", anchor="center", width=100)
        # self.search_results.column("Origin", anchor="center", width=100)
        self.search_results.column("Price", anchor="center", width=50)
        self.search_results.column("Amount", anchor="center", width=50)

        self.search_results.heading("#0", text="", anchor="center")
        # self.search_results.heading("ISBN",text="ISBN",  anchor="center")
        self.search_results.heading("Title [Original title]", text="Title [Original title]",  anchor="center")
        self.search_results.heading("Author [Translator]", text="Author [Translator]",  anchor="center")
        self.search_results.heading("Edition", text="Edition",  anchor="center")
        # self.search_results.heading("Comment",text="Comment",  anchor="center")
        self.search_results.heading("Language", text="Language",  anchor="center")
        self.search_results.heading("Genre", text="Genre",  anchor="center")
        self.search_results.heading("Publisher",text="Publisher",  anchor="center")
        self.search_results.heading("Book Type",text="Book Type",  anchor="center")
        self.search_results.heading("Year",text="Year",  anchor="center")
        self.search_results.heading("Pages",text="Pages",  anchor="center")
        self.search_results.heading("Place",text="Place",  anchor="center")
        # self.search_results.heading("Section",text="Section",  anchor="center")
        # self.search_results.heading("Translator",text="Translator",  anchor="center")
        # self.search_results.heading("Original Title", text="Original Title",  anchor="center")
        # self.search_results.heading("Origin", text="Origin",  anchor="center")
        self.search_results.heading("Price",text="Price",  anchor="center")
        self.search_results.heading("Amount",text="Amount",  anchor="center")

        self.search_results.place(relx=0.025, rely=0.45, relwidth=0.95, relheight=0.5)

        # self.search_results.insert(parent='', index='end', iid=0, values=["Book Lovers","Emily Henry",
        #                                                              "NULL", "English","Sisters Fiction, Romantic Comedy", "Berkley","paperback",
        #                                                              "2022", "400",  "17-18",
        #                                                              "1479", "2"])
        # self.search_results.insert(parent='0', index='end', iid=1, values=("Book Lovers","Emily Henry",
        #                                                              "NULL", "English","Sisters Fiction, Romantic Comedy", "Berkley","paperback",
        #                                                              "2022", "400",  "17-18",
        #                                                              "1479", "1"))
        # self.search_results.insert(parent='0', index='end', iid=2, values=("Book Lovers","Emily Henry",
        #                                                              "NULL", "English","Sisters Fiction, Romantic Comedy", "Berkley","paperback",
        #                                                              "2022", "400",  "17-18",
        #                                                              "1479", "1"))



        Login = tk.Button(self, text="Log in", height=25, width=45, command=lambda: controller.show_frame(login_window.login_window))
        Login.place(relx=1, relwidth=rel_width, relheight=rel_height, anchor='ne')

        # Found = tk.Label(self, text="Found: ", font='Helvetica 18 bold')
        Book_search = tk.Label(self, text="Book search: ", font='Helvetica 18 bold')
        # Title = tk.Label(self, text="Title")
        # Author = tk.Label(self, text="Author")
        # Edition = tk.Label(self, text="Edition")
        # Version = tk.Label(self, text="Version")
        # Location = tk.Label(self, text="Location")
        # Section = tk.Label(self, text="Section")
        # Language = tk.Label(self, text="Language")
        # Sell_price = tk.Label(self, text="SellPrice")
        # In_store = tk.Label(self, text="InStore")


        Book_search.place(relx=0.2, rely=0.2, relwidth=0.2, relheight=rel_height, anchor="e")
        # Found.place(relx=0.2, rely=0.6, relwidth=0.2, relheight=rel_height, anchor="e")
        # Title.place(relx=0.1, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")
        # Author.place(relx=0.2, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")
        # Edition.place(relx=0.3, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")
        # Version.place(relx=0.4, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")
        # Location.place(relx=0.5, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")
        # Section.place(relx=0.6, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")
        # Language.place(relx=0.7, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")
        # Sell_price.place(relx=0.8, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")
        # In_store.place(relx=0.9, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")

        self.Book_text = tk.Entry(self, width=300, borderwidth=1, relief="groove")
        self.Book_text.pack()
        self.Book_text.place(relx=0.5, rely=0.4, relwidth=0.4, relheight=0.1, anchor="e")

        books = []
        books_var = tk.StringVar(value=books)
        # self.Books_found = tk.Listbox(self, listvariable=books_var, selectmode="extended")
        # self.Books_found.place(relx=0.03, rely=0.45, relwidth=0.85, relheight=0.5)








        Search = tk.Button(self, text="Search", command=self.search)
        Search.place(relx=0.8, rely=0.2, relwidth=rel_width, relheight=0.1, anchor="e")





    def search(self):
        for record in self.search_results.get_children():
            self.search_results.delete(record)
        a = self.Book_text.get()
        Booksearch = gc.Guest()
        b = Booksearch.search(a)
        m = len(b)
        count=0
        parent_id=''
        for i in range(m):
            if i>0 and b[i-1][0] != b[i][0]:
                parent = ''
                parent_id = str(count)
            else:
                parent = parent_id
            n = len(b[i])
            values = []
            for j in range(n-1):
                if j == 0 or j == 6:
                    if b[i][j+2] != None:
                        values.append(f"{b[i][j+1]} [{b[i][j+2]}]")
                    else:
                        values.append(b[i][j + 1])
                elif j == 2:
                    if b[i][j+3] != None:
                        values.append(f"{b[i][j + 1]} {b[i][j + 2]} [{b[i][j+3]}]")
                    else:
                        values.append(f"{b[i][j + 1]} {b[i][j + 2]}")
                elif j == 13:
                    values.append(f"{b[i][j+1]}-{b[i][j+2]}")
                elif j not in (1,3,4,7,14):
                    if b[i][j+1] != None:
                        values.append(b[i][j+1])
                    else:
                        values.append('')
            self.search_results.insert(parent=parent, index='end', iid=str(count), values=values)
            count += 1

# h.place(relx=0.8, rely=0.4, relwidth=rel_width, relheight=0.1, anchor="e")
