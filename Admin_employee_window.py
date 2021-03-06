import tkinter as tk
from tkinter import ttk
import Start_window
import Admin_inventory_window
import Admin_finance_window
import Admin_sales_window
import user_creation
from AdminClass import add_to_employees
from AdminClass import Admin



db = None
emp_id = None


# class in which the frame runs
class Admin_employee_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # size constants
        rel_width = 0.1
        row_height = 20
        button_height = 45
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
        Book_sell = tk.Button(self, text="Sell book",
                              command= lambda: controller.show_frame(Admin_sales_window.Admin_sales_tab))

        # Tabs Placement
        Log_out.place(relx=0, rely=0, relwidth=rel_width, height=button_height, anchor="nw")
        Employee.place(relx=1, relwidth=rel_width, height=button_height, anchor="ne")
        Finance.place(relx=0.9, relwidth=rel_width, height=button_height, anchor="ne")
        Inventory.place(relx=0.8, relwidth=rel_width, height=button_height, anchor="ne")
        Book_sell.place(relx=0.7, relwidth=rel_width, height=button_height, anchor="ne")


        # first row - Big label definition and placement - Add Employee
        Add_employee_label = tk.Label(self, text="Add Employee:", font=button_font)
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
        New_password_save = tk.Button(self, text="Add as STAFF", command=self.add_employee)
        Add_manager_button = tk.Button(self, text="Add as MANAGER", command=self.add_manager)

        # first row - Buttons placing
        New_password_save.place(relx=0.715, rely=0.25, relwidth=rel_width, height=row_height, anchor="e")
        Add_manager_button.place(relx=0.815, rely=0.25, relwidth=rel_width, height=row_height, anchor="e")

        # second row - Big label definition - Search Employee
        Search_employee_label = tk.Label(self, text="Search Employee:", font=button_font)
        # second row - Big label placement
        Search_employee_label.place(relx=0.1, rely=0.3, relwidth=0.15, height=title_height, anchor="nw")

        self.First_name_search_entry = tk.Entry(self, width=30, borderwidth=1, relief="groove")


        # second row - Placing of all labels and their respective entries
        self.First_name_search_entry.place(relx=0.215, rely=0.45, relwidth=rel_width, height=row_height, anchor="e")

        # second row - Button definition and place
        Search_button = tk.Button(self, text="Search", command=self.employee_search)
        Search_button.place(relx=0.515, rely=0.45, relwidth=rel_width, height=row_height, anchor="e")

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
        New_password_save = tk.Button(self, text="Change", command=self.change_password)
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
        Dismiss_button = tk.Button(self, text="Dismiss", command=self.user_dismiss)
        Dismiss_button.place(relx=0.515, rely=0.85, relwidth=rel_width, height=row_height, anchor="e")

        # treeview definition (Object which holds the information about employees)
        self.search_results = ttk.Treeview(self)
        # defining columns of treeview
        self.search_results['columns'] = ("Employee ID", "First Name", "Last Name", "Email", "Position")

        # definition of columns of the treeview
        self.search_results.column("#0", width=20, stretch=False)
        self.search_results.column("Employee ID", anchor="w", width=20, minwidth=15)
        self.search_results.column("First Name", anchor="w", width=110, minwidth=50)
        self.search_results.column("Last Name", anchor="w", width=100, minwidth=50)
        self.search_results.column("Email", anchor="w", width=200, minwidth=100)
        self.search_results.column("Position", anchor="w", width=80, minwidth=100)


        # definition of headings of the treeview
        self.search_results.heading("#0", text="", anchor="center")
        self.search_results.heading("Employee ID", text="ID", anchor="center")
        self.search_results.heading("First Name", text="First name", anchor="center")
        self.search_results.heading("Last Name", text="Last name", anchor="center")
        self.search_results.heading("Email", text="Email", anchor="center")
        self.search_results.heading("Position", text="Position", anchor="center")


        # placing of treeview
        self.search_results.place(relx=0.615, rely=0.45, relheight=0.4)

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
        #checks if email exists
        search_input = email
        a = Admin(db)
        b = a.emp_search(search=search_input)
        if b[0][3] == email:
            return 'alrady exists'

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
            self.error_label.place(relx=0.615, rely=0.205, anchor="e")
        else:
            try:
                self.error_label.destroy()
            except AttributeError:
                print("label has not yet been created")
            self.confirmation_label = tk.Label(self, text="Manager added", width="15", fg="green")
            self.confirmation_label.place(relx=0.62, rely=0.25, anchor="e")
            query = add_to_employees(Name=first_name, Surname=last_name, position="Manager",email=email)
            mycursor = db.cursor()
            mycursor.execute(query)
            mycursor.execute(f"grant create user on *.* to '{email}'@'localhost' with grant option")
            mycursor.execute(f"grant reload on *.* to '{email}'@'localhost' with grant option")
            mycursor.execute("commit")

    def add_employee(self):
        first_name = self.First_name__entry3.get()
        last_name = self.Last_name_entry3.get()
        email = self.Email_entry.get()
        password = self.Password_entry.get()
        #checks if email exists
        search_input = email
        a = Admin(db)
        b = a.emp_search(search=search_input)
        try:
            if b[0][3]==email:
                return 'alrady exists'
        except IndexError:
            pass


        addition = user_creation.employee_user_addition(db=db, username=email, password=password)
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
                         "1 special character", width="15", fg="red")
            except AttributeError:
                print("label has not yet been created")
            self.error_label = tk.Label(
                self,
                text="Password is too weak,\n"
                     "please use at least\n"
                     "1 capital letter\n"
                     "1 lowercase letter\n"
                     "1 number\n"
                     "1 special character", width="15", fg="red")
            self.error_label.place(relx=0.615, rely=0.205, anchor="e")
        else:
            try:
                self.error_label.destroy()
            except AttributeError:
                print("label has not yet been created")
            self.confirmation_label = tk.Label(self, text="Employee added", width="15", fg="green")
            self.confirmation_label.place(relx=0.62, rely=0.25, anchor="e")
            query = add_to_employees(Name=first_name, Surname=last_name, position="Staff",email=email)
            mycursor = db.cursor()
            try:
                mycursor.execute(query)
                mycursor.execute("commit")
            except Exception as e:
                return e


    def change_password(self):
        self.clean_up()
        Email = f"`{self.New_password_email_entry.get()}`@`localhost`"
        New_password = self.New_password_entry.get()
        mycursor = db.cursor()
        try:
            mycursor.execute(f"ALTER USER {Email} IDENTIFIED BY '{New_password}'")
            mycursor.execute("commit")
            self.confirmation_label_password_change = tk.Label(self, text="Changed", width="15", fg="green")
            self.confirmation_label_password_change.place(relx=0.42, rely=0.65, anchor="e")

        except Exception as e:
            if e.errno == 1819:
                # this error catches if passsword doesn't satisfy the policy requirements
                self.error_label_password_change = tk.Label(
                    self,
                    text="Password is too weak,\n"
                         "please use at least\n"
                         "1 capital letter\n"
                         "1 lowercase letter\n"
                         "1 number\n"
                         "1 special character", width="15", fg="red")
                self.error_label_password_change.place(relx=0.42, rely=0.605, anchor="e")


    def user_dismiss(self):
        self.clean_up()
        Email = f"`{self.Dismiss_email_entry.get()}`@`localhost`"
        mycursor = db.cursor()
        try:
            mycursor.execute(f"drop user {Email}")
            mycursor.execute("commit")
            self.confirmation_label_password_change = tk.Label(self, text="Dismissed", width="15", fg="green")
            self.confirmation_label_password_change.place(relx=0.415, rely=0.85, anchor="e")

        except Exception as e:
            if e.errno == 1396:
                self.error_label_dismiss = tk.Label(self, text="No user", width="15", fg="red")
                self.error_label_dismiss.place(relx=0.415, rely=0.85, anchor="e")

    def clean_up(self):
        try:
            self.error_label.destroy()
        except AttributeError:
            pass
        try:
            self.confirmation_label.destroy()
        except AttributeError:
            pass

        try:
            self.error_label_password_change.destroy()
        except AttributeError:
            pass
        try:
            self.confirmation_label_password_change.destroy()
        except AttributeError:
            pass

        try:
            self.error_label_dismiss.destroy()
        except AttributeError:
            pass

    def employee_search(self):
        for record in self.search_results.get_children():
            self.search_results.delete(record)
        search_input = self.First_name_search_entry.get()
        a = Admin(db)
        b = a.emp_search(search=search_input)
        m = len(b)
        count=0
        parent=''
        for i in range(m):
            n = len(b[i])
            values = []
            for j in range(n):
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

    def finance(self, controller):
        controller.show_frame(Admin_finance_window.Admin_finance_window)
        try:
            self.error_label.destroy()
        except AttributeError:
            pass

    def inventory(self, controller):
        controller.show_frame(Admin_inventory_window.Admin_inventory_window)
        try:
            self.error_label.destroy()
        except AttributeError:
            pass

    def employee(self, controller):
        controller.show_frame(Admin_employee_window.Admin_employee_window)
        try:
            self.error_label.destroy()
        except AttributeError:
            pass

    def sell(self):
        book_id = self.Book_text.get()
        Admin_object = Admin(db)
        Admin_object.sell(book_id=book_id, employee_id=emp_id)