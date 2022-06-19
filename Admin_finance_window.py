import tkinter as tk
import Start_window
import Admin_inventory_window
import Admin_employee_window
from tkinter import ttk
# import Admin_finance_window
# from AdminClass import Admin, add_to_Price_exceptions
# from datetime import date
# from tkinter import OptionMenu, messagebox
# from book_search import book_search

emp_id = None
db = None
 # Set the value of the variable


class Admin_finance_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        rel_width = 0.1
        rel_height = 0.05

        button_font = "Helvetica 18 bold"
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

        Employee = tk.Button(self, text="Employee", command=lambda: controller.show_frame(Admin_employee_window.Admin_employee_window))
        Finance = tk.Button(self, text="Finance", relief="sunken", state="disabled")
        Inventory = tk.Button(self, text="Inventory", command=lambda: controller.show_frame(Admin_inventory_window.Admin_inventory_window))

        # Tabs Placement
        Log_out.place(relx=0, rely=0, relwidth=rel_width, height=button_height, anchor="nw")

        Employee.place(relx=1, relwidth=rel_width, height=button_height, anchor="ne")
        Finance.place(relx=0.9, relwidth=rel_width, height=button_height, anchor="ne")
        Inventory.place(relx=0.8, relwidth=rel_width, height=button_height, anchor="ne")


        Delete = tk.Button(self, text="Delete", command=self.get_margin)
        Set_margin_Button = tk.Button(self, text="Set", command=self.set_margin_func)
        Profit_margin_calc = tk.Button(self, text="Show margin", command=self.get_margin)

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



        Profit_margin = tk.Label(self, text="Profit Margin: ", font=button_font)
        Sold_min_buy = tk.Label(self, textvariable=self.string_variable)
        Set_margin = tk.Label(self, text="Set Margin To: ", font=button_font)
        Delete_text = tk.Label(self, text="Delete Sell Records Older Than 5 Years: ", font=button_font)

        # Placement Buttons

        Delete.place(relx=0.2, rely=0.75, relwidth=rel_width, relheight=rel_height, anchor="e")
        Set_margin_Button.place(relx=0.8, rely=0.5,relwidth=rel_width, relheight=rel_height, anchor="e")
        Profit_margin_calc.place(relx=0.3, rely=0.5,relwidth=rel_width, relheight=rel_height, anchor="e")

        Search_records_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        Search_records_text.pack()
        Search_records_text.place(relx=0.3, rely=0.15, relwidth=0.2, relheight=rel_height, anchor="e")

        self.Margin_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        self.Margin_text.pack()
        self.Margin_text.place(relx=0.7, rely=0.5, relwidth=rel_width, relheight=rel_height, anchor="e")

        # placement Text
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


