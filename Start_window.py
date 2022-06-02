import tkinter as tk
import login_window

class Start_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        rel_width = 0.1
        rel_height = 0.2

        # tk.title("Book search")

        # window = Tk()
        # window.geometry("800x400")
        # window.title("start Window")







        Login = tk.Button(self, text="Log in", height=25, width=45, command=lambda: controller.show_frame(login_window.login_window))
        Login.place(relx=1, relwidth=rel_width, relheight=rel_height, anchor='ne')

        Book_search = tk.Label(self, text="Book search: ", font='Helvetica 18 bold')
        Found = tk.Label(self, text="Found: ", font='Helvetica 18 bold')
        Title = tk.Label(self, text="Title")
        Author = tk.Label(self, text="Author")
        Edition = tk.Label(self, text="Edition")
        Version = tk.Label(self, text="Version")
        Location = tk.Label(self, text="Location")
        Section = tk.Label(self, text="Section")
        Language = tk.Label(self, text="Language")
        Sell_price = tk.Label(self, text="SellPrice")
        In_store = tk.Label(self, text="InStore")


        Book_search.place(relx=0.2, rely=0.2, relwidth=0.2, relheight=rel_height, anchor="e")
        Found.place(relx=0.2, rely=0.6, relwidth=0.2, relheight=rel_height, anchor="e")
        Title.place(relx=0.1, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")
        Author.place(relx=0.2, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")
        Edition.place(relx=0.3, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")
        Version.place(relx=0.4, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")
        Location.place(relx=0.5, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")
        Section.place(relx=0.6, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")
        Language.place(relx=0.7, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")
        Sell_price.place(relx=0.8, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")
        In_store.place(relx=0.9, rely=0.8, relwidth=rel_width, relheight=rel_height, anchor="e")

        Book_text = tk.Text(self, height=1, width=300, borderwidth=1, relief="groove")
        Book_text.pack()
        Book_text.place(relx=0.5, rely=0.4, relwidth=0.4, relheight=0.1, anchor="e")

        Search = tk.Button(self, text="Search")
        Search.place(relx=0.8, rely=0.4, relwidth=rel_width, relheight=0.1, anchor="e")

