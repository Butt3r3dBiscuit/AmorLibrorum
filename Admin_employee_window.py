import tkinter as tk
from tkinter import ttk
import Start_window
import Admin_inventory_window
import Admin_finance_window

class Admin_employee_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        rel_width = 0.1
        row_height = 20
        
        
        
        #Window
        # window = Tk()
        # width= window.winfo_screenwidth()
        # height= window.winfo_screenheight()
        # window.geometry("%dx%d" % (width, height))
        # window.title("Employee Window")
        
        
        
        #Buttons
        Employee = tk.Button(self, text="Employee", state="disabled")
        Finance = tk.Button(self, text="Finance",command=lambda: controller.show_frame(Admin_finance_window.Admin_finance_window))
        Inventory = tk.Button(self, text="Inventory",
                              command=lambda: controller.show_frame(Admin_inventory_window.Admin_inventory_window))
        Log_out = tk.Button(self, text="Log out", command=lambda: controller.show_frame(Start_window.Start_window))


        button_font = "Helvetica 18 bold"

        Add_employee_label = tk.Label(self, text="Add Employee:", font=button_font)
        Search_employee_label = tk.Label(self, text="Search Employee:", font=button_font)

        Add_employee_label.place(relx=0.09, rely=0.15, relwidth=0.15, height=row_height, anchor="w")
        Search_employee_label.place(relx=0.1, rely=0.35, relwidth=0.15, height=row_height, anchor="w")

        
        #Text
        # Book_search = tk.Label(self, text="Book Search")
        # Title = tk.LabelFrame(self, text="Title")
        # Author = tk.LabelFrame(self, text="Author")
        # Editor = tk.LabelFrame(self, text="Editor")
        # Version = tk.LabelFrame(self, text="Version")
        # Language = tk.LabelFrame(self, text="Language")
        # All = tk.LabelFrame(self, text="All")
        #
        
        #Placement Buttons
        Employee.place(relx=1, relwidth=rel_width, height=row_height, anchor="ne")
        Finance.place(relx=0.9, relwidth=rel_width, height=row_height, anchor="ne")
        Inventory.place(relx=0.8, relwidth=rel_width, height=row_height, anchor="ne")
        Log_out.place(relx=0, rely=0, relwidth=rel_width, height=row_height, anchor="nw")


        #first row
        First_name_label3 = tk.Label(self, text="First name", width="15")
        First_name_label3.pack()
        self.First_name__text3 = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.First_name__text3.pack()

        Last_name_label3 = tk.Label(self, text="Last name", width="15")
        Last_name_label3.pack()
        self.Last_name_entry3 = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Last_name_entry3.pack()

        Email_label = tk.Label(self, text="Email", width="15")
        Last_name_label3.pack()
        self.Email_entry = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Email_entry.pack()

        Password_label = tk.Label(self, text="Password", width="15")
        Password_label.pack()
        self.Password_entry = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Password_entry.pack()

        self.First_name__text3.place(relx=0.215, rely=0.25, relwidth=rel_width, height=row_height, anchor="e")
        First_name_label3.place(relx=0.215, rely=0.2, relwidth=rel_width, height=row_height, anchor="e")
        Last_name_label3.place(relx=0.315, rely=0.2, relwidth=rel_width, height=row_height, anchor="e")
        self.Last_name_entry3.place(relx=0.315, rely=0.25, relwidth=rel_width, height=row_height, anchor="e")
        Email_label.place(relx=0.415, rely=0.2, relwidth=rel_width, height=row_height, anchor="e")
        self.Email_entry.place(relx=0.415, rely=0.25, relwidth=rel_width, height=row_height, anchor="e")
        Password_label.place(relx=0.515, rely=0.2, relwidth=rel_width, height=row_height, anchor="e")
        self.Password_entry.place(relx=0.515, rely=0.25, relwidth=rel_width, height=row_height, anchor="e")

        Add_employee_button = tk.Button(self, text="Add as STAFF")
        Add_manager_button = tk.Button(self, text="Add as MANAGER")

        Add_employee_button.place(relx=0.715, rely=0.25, relwidth=rel_width, height=row_height, anchor="e")
        Add_manager_button.place(relx=0.815, rely=0.25, relwidth=rel_width, height=row_height, anchor="e")

        #second row
        First_name_label_search = tk.Label(self, text="First name", width="15")
        First_name_label_search.pack()
        self.First_name_entry_search = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.First_name_entry_search.pack()

        Last_name_label_search = tk.Label(self, text="Last name", width="15")
        Last_name_label_search.pack()
        self.Last_name_entry_search = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Last_name_entry_search.pack()

        self.First_name_entry_search.place(relx=0.215, rely=0.45, relwidth=rel_width, height=row_height, anchor="e")
        First_name_label_search.place(relx=0.215, rely=0.4, relwidth=rel_width, height=row_height, anchor="e")
        Last_name_label_search.place(relx=0.315, rely=0.4, relwidth=rel_width, height=row_height, anchor="e")
        self.Last_name_entry_search.place(relx=0.315, rely=0.45, relwidth=rel_width, height=row_height, anchor="e")

        Add_employee_button = tk.Button(self, text="Search")
        Add_employee_button.place(relx=0.515, rely=0.45, relwidth=rel_width, height=row_height, anchor="e")

        # #Placement Text
        # Book_search.place(relx=0.18, rely=0.15, relwidth=rel_width, relheight=rol_height, anchor="e")
        # Title.place(relx=0.2, rely=0.3, relwidth=rel_width, relheight=rol_height, anchor="e")
        # Author.place(relx=0.35, rely=0.3, relwidth=rel_width, relheight=rol_height, anchor="e")
        # Editor.place(relx=0.3, rely=0.3, relwidth=rel_width, relheight=rol_height, anchor="e")
        # Version.place(relx=0.65, rely=0.3, relwidth=rel_width, relheight=rol_height, anchor="e")
        # Language.place(relx=0.8, rely=0.3, relwidth=rel_width, relheight=rol_height, anchor="e")
        # All.place(relx=0.95, rely=0.3, relwidth=rel_width, relheight=rol_height, anchor="e")
'''
        self.search_results = ttk.Treeview(self)
        # rest = "Title", "Author", "Surname", "Edition", "Comment", "Language", "Publisher", "Year", "Pages", "Book Type", "Location", "Section", "Genre", "Translator", "Original Title", "Original Title", "Origin"
        self.search_results['columns'] = ("First ", "Comment", "Title [Original title]", "Author [Translator]",
                                          "Edition", "Language", "Genre", "Publisher",
                                          "Book Type", "Year", "Pages", "Place",

                                          # "Translator","Original Title", "Origin",
                                          "Price", "Amount")

        self.search_results.column("#0", width=20, stretch=False)
        self.search_results.column("ISBN", anchor="w", width=110, minwidth=50)
        self.search_results.column("Comment", anchor="w", width=100, minwidth=50)
        self.search_results.column("Title [Original title]", anchor="w", width=200, minwidth=100)
        self.search_results.column("Author [Translator]", anchor="w", width=100, minwidth=50)
'''
        def test_emp_id(self):
            print(Admin_inventory_window.emp_id)
            print('this is just to test that we have the emp_id loaded - not sure if we need it here but ye')
            print("we could make it so that in one of the corners there would be sth like logged as:")