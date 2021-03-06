import tkinter as tk
from tkinter import ttk
import login_window
import guest_class as gc


class Start_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        rel_width = 0.1
        row_height = 20
        button_height = 45
        button_font = "Helvetica 18 bold"

        self.search_results = ttk.Treeview(self)
        self.search_results['columns'] = ("Title [Original title]", "Author [Translator]",
                                     "Edition", "Language","Genre", "Publisher",
                                     "Book Type","Year", "Pages", "Place",
                                     "Price", "Amount")

        self.search_results.column("#0", width=20, stretch=False)
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

        self.search_results.place(relx=0.025, rely=0.45, relwidth=0.95, relheight=0.5)


        Login = tk.Button(self, text="Log in", height=25, width=45, command=lambda: controller.show_frame(login_window.login_window))
        Login.place(relx=1, relwidth=rel_width, height=button_height, anchor='ne')

        Book_search = tk.Label(self, text="Book search: ", font=button_font)
        Book_search.place(relx=0.2, rely=0.2, relwidth=0.2, height=row_height, anchor="e")

        self.Book_text = tk.Entry(self, width=300, borderwidth=1, relief="groove")
        self.Book_text.pack()
        self.Book_text.place(relx=0.2, rely=0.3, relwidth=0.1, height=row_height, anchor="e")


        Search = tk.Button(self, text="Search", command=self.search)
        Search.pack()
        Search.place(relx=0.3, rely=0.3, relwidth=rel_width, height=row_height, anchor="e")



    def search(self):
        for record in self.search_results.get_children():
            self.search_results.delete(record)
        search_input = self.Book_text.get()
        Booksearch = gc.Guest()
        b = Booksearch.search(search=search_input)
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