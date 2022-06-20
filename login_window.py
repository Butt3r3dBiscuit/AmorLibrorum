import tkinter as tk

import Admin_sales_window
import Start_window
import Employees_sales_tab
from connect import connect_employee
import Admin_inventory_window
import Admin_finance_window
import Admin_employee_window
import AdminClass


class login_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        print(Admin_inventory_window.emp_id)

        back_button = tk.Button(self, text="Return home", height=2, width=11, command= lambda: self.back_button(controller))
        back_button.pack()
        back_button.place(x=0, y=0)

        email_label = tk.Label(self, text="Email Adress", width = "15")
        email_label.pack()
        self.email_text = tk.Entry(self, width=40)
        self.email_text.pack()

        password_label = tk.Label(self, text="Password", width = "15")
        password_label.pack()
        self.password_text = tk.Entry(self, width=40, show="*")
        self.password_text.pack()

        self.login_button = tk.Button(self, text="Log in", height=2, width=11, command=lambda: self.log_in(controller))
        self.login_button.bind('<Return>', lambda event: self.log_in(controller)) # this line makes it so that you can "click" on Log in button via Return key on keyboard
        self.login_button.pack()

    def log_in(self, controller):
        email = self.email_text.get()
        print("email: ", email)
        if email == "margje@amorlibrorum.boek":
            print(True)
        else:
            print([email])
        password = self.password_text.get()
        # print("password: ", password)
        # email = "casual@amorlibrorum.boek" #temp
        # password = "YetAn0!herqwertyp4ssword" #temp
        email = "frank@amorlibrorum.boek"
        password = "An0!herqwertyp4ssword"
        self.db = connect_employee(email, password)
        if self.db == 1045:
            try:
                self.error_label.destroy()
                self.error_label = tk.Label(self, text="User not found!", width = "15", fg = "red")
            except AttributeError:
                print("label has not yet been created")
            self.error_label = tk.Label(self, text="User not found!", width = "15", fg = "red")
            self.error_label.place(relx=0.5, rely=0.15, anchor="n")
        else:
            self.my_cursor = self.db.cursor()
            self.my_cursor.execute(f"select position, Employee_ID from employees where email='{email}'")
            for (x) in self.my_cursor:
                position = x[0]
                print("here is position: ", position)
                self.employee_id = x[1]
                print("here is the id: ", self.employee_id)
            self.new_window(position,controller)

    def new_window(self,position, controller):
        self.password_text.destroy()
        self.password_text = tk.Entry(self, width=40, show="*")
        self.password_text.pack()
        self.login_button.destroy()
        self.login_button = tk.Button(self, text="Log in", height=2, width=11, command=lambda: self.log_in(controller))
        self.login_button.pack()
        if position == "Staff":
            try:
                self.error_label.destroy()
            except AttributeError:
                print("label has not yet been created")
            Employees_sales_tab.emp_id = self.employee_id
            Employees_sales_tab.db = self.db
            print(Employees_sales_tab.emp_id)
            controller.show_frame(Employees_sales_tab.Employee_sales_window)
        elif position == "Manager":
            try:
                self.error_label.destroy()
            except AttributeError:
                print("label has not yet been created")
            Admin_inventory_window.emp_id = self.employee_id
            Admin_inventory_window.db = self.db
            Admin_finance_window.emp_id = self.employee_id
            Admin_finance_window.db = self.db
            Admin_employee_window.db = self.db
            Admin_employee_window.emp = self.employee_id
            AdminClass.db = self.db
            Admin_sales_window.db = self.db
            Admin_sales_window.emp_id = self.employee_id
            print(Admin_inventory_window.emp_id)
            controller.show_frame(Admin_sales_window.Admin_sales_tab)

    def back_button(self, controller):
        try:
            self.error_label.destroy()
        except AttributeError:
            print("label has not yet been created")
        self.password_text.destroy()
        self.password_text = tk.Entry(self, width=40, show="*")
        self.password_text.pack()
        self.login_button.pack()

        controller.show_frame(Start_window.Start_window)