import tkinter as tk
from AdminClass import Admin
import AdminClass
import Start_window
import Admin_inventory_window
import Admin_employee_window
import Admin_sales_window
from tkinter import ttk


emp_id = None
db = None


class Admin_finance_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        rel_height = 0.05
        rel_width = 0.1
        row_height = 20
        button_height = 45
        button_font = "Helvetica 18 bold"


        # Tabs
        Log_out = tk.Button(self, text="Log out", command=lambda: self.log_out(controller))

        Employee = tk.Button(self, text="Employee", command=lambda: self.employee(controller))
        Finance = tk.Button(self, text="Finance", relief="sunken", state="disabled")
        Inventory = tk.Button(self, text="Inventory", command=lambda: self.inventory(controller))
        Book_sell = tk.Button(self, text="Sell book", command= lambda: self.admin_sales(controller))

        # Tabs Placement
        Log_out.place(relx=0, rely=0, relwidth=rel_width, height=button_height, anchor="nw")

        Employee.place(relx=1, relwidth=rel_width, height=button_height, anchor="ne")
        Finance.place(relx=0.9, relwidth=rel_width, height=button_height, anchor="ne")
        Inventory.place(relx=0.8, relwidth=rel_width, height=button_height, anchor="ne")
        Book_sell.place(relx=0.7, relwidth=rel_width, height=button_height, anchor="ne")


        Delete = tk.Button(self, text="Delete", command=self.deletion)
        Set_margin_Button = tk.Button(self, text="Set", command=self.set_margin_func)
        Profit_margin_calc = tk.Button(self, text="Show margin", command=self.get_margin)
        Search_records_button = tk.Button(self, text="Search", command=self.transaction_search)
        
        Search_records_button.place(relx=0.3, rely=0.15, relwidth=rel_width, height=row_height, anchor="e")

        # text
        self.string_variable = tk.StringVar()  # Create the variable
        self.string_variable.set("Pending")
        Search_records = tk.Label(self, text="Search records: ", font=button_font)
        Found_books = tk.Label(self, text="Found transactions: ", font=button_font)

        # transid bookid empid transdate price

        self.search_results = ttk.Treeview(self)
        self.search_results['columns'] = ("TID", "BID", "EID", "Transdate", "Price")


        self.search_results.column("#0", width=20, stretch=False)
        self.search_results.column("TID", anchor="w", width=110, minwidth=50)
        self.search_results.column("BID", anchor="w", width=110, minwidth=50)
        self.search_results.column("EID", anchor="w", width=110, minwidth=50)
        self.search_results.column("Transdate", anchor="w", width=110, minwidth=50)
        self.search_results.column("Price", anchor="w", width=110, minwidth=50)

        self.search_results.heading("#0", text="", anchor="center")
        self.search_results.heading("TID", text="Transaction ID", anchor="center")
        self.search_results.heading("BID", text="Book ID", anchor="center")
        self.search_results.heading("EID", text="Employee ID", anchor="center")
        self.search_results.heading("Transdate", text="Date", anchor="center")
        self.search_results.heading("Price", text="Price", anchor="center")

        self.search_results.place(relx=0.025, rely=0.25, relwidth=0.95, relheight=0.15)



        Profit_margin = tk.Label(self, text="Profit Margin: ", font=button_font)
        Sold_min_buy = tk.Label(self, textvariable=self.string_variable)
        Set_margin = tk.Label(self, text="Set Margin To: ", font=button_font)
        Delete_text = tk.Label(self, text="Delete Sell Records Older Than 5 Years: ", font=button_font)

        # Placement of buttons
        Delete.place(relx=0.2, rely=0.75, relwidth=rel_width, relheight=rel_height, anchor="e")
        Set_margin_Button.place(relx=0.8, rely=0.5,relwidth=rel_width, relheight=rel_height, anchor="e")
        Profit_margin_calc.place(relx=0.3, rely=0.5,relwidth=rel_width, relheight=rel_height, anchor="e")

        self.Search_records_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Search_records_text.pack()
        self.Search_records_text.place(relx=0.2, rely=0.15, relwidth=rel_width, height=row_height, anchor="e")

        self.Margin_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Margin_text.pack()
        self.Margin_text.place(relx=0.7, rely=0.5, relwidth=rel_width, height=row_height, anchor="e")

        # Placement of text
        Search_records.place(relx=0.2, rely=0.1, relwidth=rel_width, relheight=rel_height, anchor="e")
        Found_books.place(relx=0.27, rely=0.22, relwidth=rel_width*2, relheight=rel_height, anchor="e")

        Profit_margin.place(relx=0.2, rely=0.5, relwidth=rel_width, relheight=rel_height, anchor="e")
        Sold_min_buy.place(relx=0.4, rely=0.5, relwidth=0.1, relheight=rel_height, anchor="e")
        Set_margin.place(relx=0.6, rely=0.5, relwidth=rel_width, relheight=rel_height, anchor="e")
        Delete_text.place(relx=0.375, rely=0.7, relwidth=0.3, relheight=rel_height, anchor="e")


    def set_margin_func(self):
        new_margin = self.Margin_text.get()
        try:
            new_margin = float(new_margin)
            new_margin = round(new_margin,3)
            my_cursor = db.cursor()
            my_cursor.execute(f"update variables set margin={new_margin}")
            my_cursor.execute("commit")
            self.get_margin()
        except Exception as e:
            print(e)
            print("we could make this red?")
        print(new_margin)

    def get_margin(self):
        mycursor = db.cursor()
        mycursor.execute("select margin from variables;")
        for x in mycursor:
            self.string_variable.set(str(x[0]))
    def deletion(self):
        Admin_object = AdminClass.Admin(db)
        Admin_object.clean()
        self.confirmation_label_password_change = tk.Label(self, text="Deleted", width="15", fg="green")
        self.confirmation_label_password_change.place(relx=0.315, rely=0.75, anchor="e")


    def transaction_search(self):
        for record in self.search_results.get_children():
            self.search_results.delete(record)
        search_input = self.Search_records_text.get()
        a = Admin(db)
        b = a.search_transactions(search=search_input)
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
            self.confirmation_label_password_change.destroy()
        except AttributeError:
            pass
    def inventory(self, controller):
        controller.show_frame(Admin_inventory_window.Admin_inventory_window)
        try:
            self.confirmation_label_password_change.destroy()
        except AttributeError:
            pass
    def employee(self, controller):
        controller.show_frame(Admin_employee_window.Admin_employee_window)
        try:
            self.confirmation_label_password_change.destroy()
        except AttributeError:
            pass
    def admin_sales(self, controller):
        controller.show_frame(Admin_sales_window.Admin_sales_tab)
        try:
            self.confirmation_label_password_change.destroy()
        except AttributeError:
            pass