import tkinter as tk
from tkinter import ttk
import Start_window
import Admin_inventory_window
# import Admin_employee_window
import Admin_finance_window
import user_creation


# from AdminClass import Admin, add_to_Price_exceptions
# from datetime import date
# from tkinter import OptionMenu, messagebox
db = None


# class in which the frame runs
class Admin_employee_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # size constants
        rel_width = 0.1
        rel_height = 0.05
        rel_width = 0.1
        row_height = 20
        button_height = 45
        text_height = 20
        title_height = 60

        # defining font for buttons
        button_font = "Helvetica 18 bold"

        # Tabs
        Log_out = tk.Button(self, text="Log out", command=lambda: self.log_out(controller))
        Employee = tk.Button(self, text="Employee", relief="sunken", state="disabled")
        Finance = tk.Button(self, text="Finance",
                            command=lambda: self.finance(controller))
        Inventory = tk.Button(self, text="Inventory",
                              command=lambda: self.inventory(controller))

        # Tabs Placement
        Log_out.place(relx=0, rely=0, relwidth=rel_width, height=button_height, anchor="nw")
        Employee.place(relx=1, relwidth=rel_width, height=button_height, anchor="ne")
        Finance.place(relx=0.9, relwidth=rel_width, height=button_height, anchor="ne")
        Inventory.place(relx=0.8, relwidth=rel_width, height=button_height, anchor="ne")

        # first row - Big label definition - Add Employee
        Add_employee_label = tk.Label(self, text="Add Employee:", font=button_font)
        # first row - Big label placement
        Add_employee_label.place(relx=0.09, rely=0.1, relwidth=0.15, height=title_height, anchor="nw")
        # first row - All labels and their respective entries
        First_name_label3 = tk.Label(self, text="First name", width="15")
        self.First_name__entry3 = tk.Entry(self, width=30, borderwidth=1, relief="groove")

        Last_name_label3 = tk.Label(self, text="Last name", width="15")
        self.Last_name_entry3 = tk.Entry(self, width=30, borderwidth=1, relief="groove")

        Email_label = tk.Label(self, text="Email", width="15")
        self.Email_entry = tk.Entry(self, width=30, borderwidth=1, relief="groove")

        Password_label = tk.Label(self, text="Password", width="15")
        self.Password_entry = tk.Entry(self, width=30, borderwidth=1, relief="groove", show="*")

        # first row - Placing of all labels and their respective entries
        self.First_name__entry3.place(relx=0.215, rely=0.25, relwidth=rel_width, height=row_height, anchor="e")
        First_name_label3.place(relx=0.215, rely=0.2, relwidth=rel_width, height=row_height, anchor="e")
        Last_name_label3.place(relx=0.315, rely=0.2, relwidth=rel_width, height=row_height, anchor="e")
        self.Last_name_entry3.place(relx=0.315, rely=0.25, relwidth=rel_width, height=row_height, anchor="e")
        Email_label.place(relx=0.415, rely=0.2, relwidth=rel_width, height=row_height, anchor="e")
        self.Email_entry.place(relx=0.415, rely=0.25, relwidth=rel_width, height=row_height, anchor="e")
        Password_label.place(relx=0.515, rely=0.2, relwidth=rel_width, height=row_height, anchor="e")
        self.Password_entry.place(relx=0.515, rely=0.25, relwidth=rel_width, height=row_height, anchor="e")

        # first row - Buttons definition
        New_password_save = tk.Button(self, text="Add as STAFF")
        Add_manager_button = tk.Button(self, text="Add as MANAGER", command=self.add_manager)

        # first row - Buttons placing
        New_password_save.place(relx=0.715, rely=0.25, relwidth=rel_width, height=row_height, anchor="e")
        Add_manager_button.place(relx=0.815, rely=0.25, relwidth=rel_width, height=row_height, anchor="e")

        # second row - Big label definition - Search Employee
        Search_employee_label = tk.Label(self, text="Search Employee:", font=button_font)
        # second row - Big label placement
        Search_employee_label.place(relx=0.1, rely=0.3, relwidth=0.15, height=title_height, anchor="nw")

        # second row - All labels and their respective entries
        First_name_search = tk.Label(self, text="First name", width="15")
        self.First_name_search_entry = tk.Entry(self, width=30, borderwidth=1, relief="groove")

        Last_name_search_label = tk.Label(self, text="Last name", width="15")
        self.Last_name_search_entry = tk.Entry(self, width=30, borderwidth=1, relief="groove")

        # second row - Placing of all labels and their respective entries
        self.First_name_search_entry.place(relx=0.215, rely=0.45, relwidth=rel_width, height=row_height, anchor="e")
        First_name_search.place(relx=0.215, rely=0.4, relwidth=rel_width, height=row_height, anchor="e")
        Last_name_search_label.place(relx=0.315, rely=0.4, relwidth=rel_width, height=row_height, anchor="e")
        self.Last_name_search_entry.place(relx=0.315, rely=0.45, relwidth=rel_width, height=row_height, anchor="e")

        # second row - Button definition and place
        New_password_save = tk.Button(self, text="Search")
        New_password_save.place(relx=0.515, rely=0.45, relwidth=rel_width, height=row_height, anchor="e")

        # third row - Big label definition - Changing passwords
        New_password_label = tk.Label(self, text="Change password:", font=button_font)
        # third row - Big label placement
        New_password_label.place(relx=0.1, rely=0.5, relwidth=0.15, height=title_height, anchor="nw")

        # third row - All labels and their respective entries
        New_password_email = tk.Label(self, text="Email", width="15")
        self.New_password_email_entry = tk.Entry(self, width=30, borderwidth=1, relief="groove")

        New_password_label = tk.Label(self, text="New Password", width="15")
        self.New_password_entry = tk.Entry(self, width=30, borderwidth=1, relief="groove", show="*")

        # third row - Placing of all labels and their respective entries
        self.New_password_email_entry.place(relx=0.215, rely=0.65, relwidth=rel_width, height=row_height, anchor="e")
        New_password_email.place(relx=0.215, rely=0.6, relwidth=rel_width, height=row_height, anchor="e")
        New_password_label.place(relx=0.315, rely=0.6, relwidth=rel_width, height=row_height, anchor="e")
        self.New_password_entry.place(relx=0.315, rely=0.65, relwidth=rel_width, height=row_height, anchor="e")

        # third row - Button definition and place
        New_password_save = tk.Button(self, text="Change")
        New_password_save.place(relx=0.515, rely=0.65, relwidth=rel_width, height=row_height, anchor="e")

        # fourth row - Big label definition - Dismission
        User_dismiss = tk.Label(self, text="User dismiss:", font=button_font)
        # fourth row - Big label placement
        User_dismiss.place(relx=0.1, rely=0.75, relwidth=0.15, height=title_height, anchor="w")

        # fourth row - Label and its respective entry
        Dismiss_email = tk.Label(self, text="Email", width="15")
        self.Dismiss_email_entry = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        # fourth row - Placing of label and its respective entry
        self.Dismiss_email_entry.place(relx=0.215, rely=0.85, relwidth=rel_width, height=row_height, anchor="e")
        Dismiss_email.place(relx=0.215, rely=0.8, relwidth=rel_width, height=row_height, anchor="e")

        # fourth row - Button definition and place
        Dismiss_button = tk.Button(self, text="Dismiss")
        Dismiss_button.place(relx=0.515, rely=0.85, relwidth=rel_width, height=row_height, anchor="e")

        # treeview definition (Object which holds the information about employees)
        self.search_results = ttk.Treeview(self)
        # defining columns of treeview
        self.search_results['columns'] = ("First Name", "Last Name", "Email")

        # definition of columns of the treeview
        self.search_results.column("#0", width=20, stretch=False)
        self.search_results.column("First Name", anchor="w", width=110, minwidth=50)
        self.search_results.column("Last Name", anchor="w", width=100, minwidth=50)
        self.search_results.column("Email", anchor="w", width=200, minwidth=100)

        # definition of headings of the treeview
        self.search_results.heading("#0", text="", anchor="center")
        self.search_results.heading("First Name", text="First name", anchor="center")
        self.search_results.heading("Last Name", text="Last name", anchor="center")
        self.search_results.heading("Email", text="Email", anchor="center")

        # placing of treeview
        self.search_results.place(relx=0.615, rely=0.45, relheight=0.4)

    def test_emp_id(self):
        print(Admin_inventory_window.emp_id)
        print('this is just to test that we have the emp_id loaded - not sure if we need it here but ye')
        print("we could make it so that in one of the corners there would be sth like logged as:")

    def finance(self, controller):
        controller.show_frame(Admin_finance_window.Admin_finance_window)
        self.clean_up()

    def inventory(self, controller):
        controller.show_frame(Admin_inventory_window.Admin_inventory_window)
        self.clean_up()

    def log_out(self, controller):
        controller.show_frame(Start_window.Start_window)
        self.clean_up()

    def add_manager(self):
        first_name = self.First_name__entry3.get()
        last_name = self.Last_name_entry3.get()
        email = self.Email_entry.get()
        password = self.Password_entry.get()
        print(first_name, last_name, email,password)
        addition = user_creation.admin_user_addition(db=db, username=email, password=password)
        if addition is not None:
            try:
                self.error_label.destroy()
                self.error_label = tk.Label(
                    self,
                    text="Password is too weak,\n"
                         "please use at least\n"
                         "1 capital letter\n"
                         "1 lowercase letter\n"
                         "1 number\n"
                         "1 special character", width = "15", fg = "red")
            except AttributeError:
                print("label has not yet been created")
            self.error_label = tk.Label(
                    self,
                    text="Password is too weak,\n"
                         "please use at least\n"
                         "1 capital letter\n"
                         "1 lowercase letter\n"
                         "1 number\n"
                         "1 special character", width = "15", fg = "red")
            # error_label.pack()
            self.error_label.place(relx=0.615, rely=0.205, anchor="e")
        else:
            try:
                self.error_label.destroy()
            except AttributeError:
                print("label has not yet been created")
            self.confirmation_label = tk.Label(self, text="Manager added", width="15", fg="green")
            self.confirmation_label.place(relx=0.62, rely=0.25, anchor="e")


    def add_employee(self):
        pass

    def change_password(self):
        pass

    def user_dismiss(self):
        pass
    def clean_up(self):
        try:
            self.error_label.destroy()
            self.confirmation_label.destroy()
            # more to be added
        except AttributeError:
            return "labels have not been created"


