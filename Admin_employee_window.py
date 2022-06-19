import tkinter as tk
from tkinter import ttk
import Start_window
import Admin_inventory_window
# import Admin_employee_window
import Admin_finance_window
# from AdminClass import Admin, add_to_Price_exceptions
# from datetime import date
# from tkinter import OptionMenu, messagebox





class Admin_employee_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        rel_width = 0.1
        rel_height = 0.05
        # row_height = 20
        rel_width = 0.1
        row_height = 20
        button_height = 45
        text_height = 20
        title_height = 30


        button_font = "Helvetica 18 bold"

        # Tabs
        Log_out = tk.Button(self, text="Log out", command=lambda: controller.show_frame(Start_window.Start_window))

        Employee = tk.Button(self, text="Employee", relief="sunken", state="disabled")
        Finance = tk.Button(self, text="Finance", command=lambda: controller.show_frame(Admin_finance_window.Admin_finance_window))
        Inventory = tk.Button(self, text="Inventory", command=lambda: controller.show_frame(Admin_inventory_window.Admin_inventory_window))

        # Tabs Placement
        Log_out.place(relx=0,rely=0,relwidth=rel_width, height=button_height, anchor="nw")

        Employee.place(relx=1, relwidth=rel_width, height=button_height, anchor="ne")
        Finance.place(relx=0.9, relwidth=rel_width, height=button_height, anchor="ne")
        Inventory.place(relx=0.8, relwidth=rel_width, height=button_height, anchor="ne")




        Add_employee_label = tk.Label(self, text="Add Employee:", font=button_font)
        Search_employee_label = tk.Label(self, text="Search Employee:", font=button_font)

        Add_employee_label.place(relx=0.09, rely=0.15, relwidth=0.15, height=row_height, anchor="w")
        Search_employee_label.place(relx=0.1, rely=0.35, relwidth=0.15, height=row_height, anchor="w")
        
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

        New_password_save = tk.Button(self, text="Add as STAFF")
        Add_manager_button = tk.Button(self, text="Add as MANAGER")

        New_password_save.place(relx=0.715, rely=0.25, relwidth=rel_width, height=row_height, anchor="e")
        Add_manager_button.place(relx=0.815, rely=0.25, relwidth=rel_width, height=row_height, anchor="e")

        #second row
        New_password_email = tk.Label(self, text="First name", width="15")
        New_password_email.pack()
        self.New_password_email_entry = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.New_password_email_entry.pack()

        New_password_label = tk.Label(self, text="Last name", width="15")
        New_password_label.pack()
        self.New_password_entry = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.New_password_entry.pack()

        self.New_password_email_entry.place(relx=0.215, rely=0.45, relwidth=rel_width, height=row_height, anchor="e")
        New_password_email.place(relx=0.215, rely=0.4, relwidth=rel_width, height=row_height, anchor="e")
        New_password_label.place(relx=0.315, rely=0.4, relwidth=rel_width, height=row_height, anchor="e")
        self.New_password_entry.place(relx=0.315, rely=0.45, relwidth=rel_width, height=row_height, anchor="e")

        New_password_save = tk.Button(self, text="Search")
        New_password_save.place(relx=0.515, rely=0.45, relwidth=rel_width, height=row_height, anchor="e")

        #third row - changing passwords
        New_password_label = tk.Label(self, text="Change password:", font=button_font)
        New_password_label.place(relx=0.1, rely=0.55, relwidth=0.15, height=row_height, anchor="w")



        New_password_email = tk.Label(self, text="Email", width="15")
        New_password_email.pack()
        self.New_password_email_entry = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.New_password_email_entry.pack()

        New_password_label = tk.Label(self, text="New Password", width="15")
        New_password_label.pack()
        self.New_password_entry = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.New_password_entry.pack()

        self.New_password_email_entry.place(relx=0.215, rely=0.65, relwidth=rel_width, height=row_height, anchor="e")
        New_password_email.place(relx=0.215, rely=0.6, relwidth=rel_width, height=row_height, anchor="e")
        New_password_label.place(relx=0.315, rely=0.6, relwidth=rel_width, height=row_height, anchor="e")
        self.New_password_entry.place(relx=0.315, rely=0.65, relwidth=rel_width, height=row_height, anchor="e")

        New_password_save = tk.Button(self, text="Change")
        New_password_save.place(relx=0.515, rely=0.65, relwidth=rel_width, height=row_height, anchor="e")

        #fourth row dismission
        User_dismiss = tk.Label(self, text="User dismiss:", font=button_font)
        User_dismiss.place(relx=0.1, rely=0.75, relwidth=0.15, height=row_height, anchor="w")

        Dismiss_email = tk.Label(self, text="Email", width="15")
        Dismiss_email.pack()
        self.Dismiss_email_entry = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Dismiss_email_entry.place(relx=0.215, rely=0.85, relwidth=rel_width, height=row_height, anchor="e")
        Dismiss_email.place(relx=0.215, rely=0.8, relwidth=rel_width, height=row_height, anchor="e")

        Dismiss_button = tk.Button(self, text="Dismiss")
        Dismiss_button.place(relx=0.515, rely=0.85, relwidth=rel_width, height=row_height, anchor="e")


        self.search_results = ttk.Treeview(self)
        self.search_results['columns'] = ("First Name", "Last Name", "Email")

        self.search_results.column("#0", width=20, stretch=False)
        self.search_results.column("First Name", anchor="w", width=110, minwidth=50)
        self.search_results.column("Last Name", anchor="w", width=100, minwidth=50)
        self.search_results.column("Email", anchor="w", width=200, minwidth=100)

        self.search_results.heading("#0", text="", anchor="center")
        self.search_results.heading("First Name", text="First name", anchor="center")
        self.search_results.heading("Last Name", text="Last name", anchor="center")
        self.search_results.heading("Email", text="Email", anchor="center")

        self.search_results.place(relx=0.615, rely=0.45, relheight=0.4)

    def test_emp_id(self):
        print(Admin_inventory_window.emp_id)
        print('this is just to test that we have the emp_id loaded - not sure if we need it here but ye')
        print("we could make it so that in one of the corners there would be sth like logged as:")
