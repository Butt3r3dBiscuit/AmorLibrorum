import tkinter as tk
import login_window
import guest_class as gc


class Start_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        rel_width = 0.1
        row_height = 20


        Login = tk.Button(self, text="Log in", height=2, width=11, command=lambda: controller.show_frame(
            login_window.login_window))
        Login.place(relx=1, anchor='ne')

        button_font = "Helvetica 18 bold"

        Book_search = tk.Label(self, text="Book search: ", font=button_font)
        Found = tk.Label(self, text="Found: ", font=button_font)
        Title = tk.Label(self, text="Title")
        Author = tk.Label(self, text="Author")
        Edition = tk.Label(self, text="Edition")
        Version = tk.Label(self, text="Version")
        Location = tk.Label(self, text="Location")
        Section = tk.Label(self, text="Section")
        Language = tk.Label(self, text="Language")
        Sell_price = tk.Label(self, text="SellPrice")
        In_store = tk.Label(self, text="InStore")


        Book_search.place(relx=0.2, rely=0.2, relwidth=0.2, height=row_height, anchor="e")
        Found.place(relx=0.2, rely=0.6, relwidth=0.2, height=row_height, anchor="e")
        Title.place(relx=0.1, rely=0.8, relwidth=rel_width, height=row_height, anchor="e")
        Author.place(relx=0.2, rely=0.8, relwidth=rel_width, height=row_height, anchor="e")
        Edition.place(relx=0.3, rely=0.8, relwidth=rel_width, height=row_height, anchor="e")
        Version.place(relx=0.4, rely=0.8, relwidth=rel_width, height=row_height, anchor="e")
        Location.place(relx=0.5, rely=0.8, relwidth=rel_width, height=row_height, anchor="e")
        Section.place(relx=0.6, rely=0.8, relwidth=rel_width, height=row_height, anchor="e")
        Language.place(relx=0.7, rely=0.8, relwidth=rel_width, height=row_height, anchor="e")
        Sell_price.place(relx=0.8, rely=0.8, relwidth=rel_width, height=row_height, anchor="e")
        In_store.place(relx=0.9, rely=0.8, relwidth=rel_width, height=row_height, anchor="e")

        self.Book_text = tk.Entry(self, width=300, borderwidth=1, relief="groove")
        self.Book_text.pack()
        self.Book_text.place(relx=0.5, rely=0.4, relwidth=0.4, height=20, anchor="e")

        books = []
        books_var = tk.StringVar(value=books)
        self.Books_found = tk.Listbox(self, listvariable=books_var, selectmode="extended")
        self.Books_found.place(relx=0.03, rely=0.45, relwidth=0.85, height=500)

        Search = tk.Button(self, text="Search", command=self.search)
        Search.place(relx=0.8, rely=0.2, relwidth=rel_width, height=50, anchor="e")

    def search(self):
        a = self.Book_text.get()
        print(f"({a})")
        Booksearch = gc.Guest()
        b = Booksearch.search(a)
        print(b)
        m = len(b)
        books = []
        for i in range(m):
            books.append(str(b[i]))
        print(books)
        books_var = tk.StringVar(value=books)
        self.Books_found.config(listvariable=books_var)



# h.place(relx=0.8, rely=0.4, relwidth=rel_width, height=0.1, anchor="e")

        # Search = tk.Button(self, text="Search") #todo
        # Search.place(relx=0.8, rely=0.4, relwidth=rel_width, height=row_height, anchor="e") #todo