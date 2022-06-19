import tkinter as tk
# from tkinter import ttk
import Start_window
import Admin_inventory_window
import Admin_employee_window
# import Admin_finance_window
# from AdminClass import Admin, add_to_Price_exceptions
# from datetime import date
# from tkinter import OptionMenu, messagebox





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

        # text
        Search_records = tk.Label(self, text="Search records: ", font=button_font)
        Found_books = tk.Label(self, text="Found Books: ", font=button_font)
        Title = tk.Label(self, text="Title")
        Author = tk.Label(self, text="Author")
        Edition = tk.Label(self, text="Edition")
        Version = tk.Label(self, text="Version")
        Buy_price = tk.Label(self, text="BuyPrice")
        Sold_price = tk.Label(self, text="SoldPrice")
        Number_of_sales = tk.Label(self, text="NumberOfSales")
        Profit_margin = tk.Label(self, text="Profit Margin: ", font=button_font)
        Sold_min_buy = tk.Label(self, text="(SoldPrice - BuyPrice)/BuyPrice")
        Set_margin = tk.Label(self, text="Set Margin To: ", font=button_font)
        Delete_text = tk.Label(self, text="Delete Sell Records Older Than 5 Years: ", font=button_font)

        # Placement Buttons
        

        Search_records_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        Search_records_text.pack()
        Search_records_text.place(relx=0.3, rely=0.15, relwidth=0.2, relheight=rel_height, anchor="e")

        Margin_text = tk.Entry(self, width=30, borderwidth=1, relief="groove")
        Margin_text.pack()
        Margin_text.place(relx=0.7, rely=0.5, relwidth=rel_width, relheight=rel_height, anchor="e")

        # placement Text
        Search_records.place(relx=0.2, rely=0.1, relwidth=rel_width, relheight=rel_height, anchor="e")
        Found_books.place(relx=0.2, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor="e")
        Title.place(relx=0.2, rely=0.35, relwidth=rel_width, relheight=rel_height, anchor="e")
        Author.place(relx=0.3, rely=0.35, relwidth=rel_width, relheight=rel_height, anchor="e")
        Edition.place(relx=0.4, rely=0.35, relwidth=rel_width, relheight=rel_height, anchor="e")
        Version.place(relx=0.5, rely=0.35, relwidth=rel_width, relheight=rel_height, anchor="e")
        Buy_price.place(relx=0.6, rely=0.35, relwidth=rel_width, relheight=rel_height, anchor="e")
        Sold_price.place(relx=0.7, rely=0.35, relwidth=rel_width, relheight=rel_height, anchor="e")
        Number_of_sales.place(relx=0.8, rely=0.35, relwidth=rel_width, relheight=rel_height, anchor="e")
        Profit_margin.place(relx=0.2, rely=0.5, relwidth=rel_width, relheight=rel_height, anchor="e")
        Sold_min_buy.place(relx=0.3, rely=0.55, relwidth=0.2, relheight=rel_height, anchor="e")
        Set_margin.place(relx=0.6, rely=0.5, relwidth=rel_width, relheight=rel_height, anchor="e")
        Delete_text.place(relx=0.375, rely=0.7, relwidth=0.3, relheight=rel_height, anchor="e")
