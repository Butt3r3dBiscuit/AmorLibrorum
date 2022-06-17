import tkinter as tk
import Start_window
# from login_window import login_window
# from Employees_sales_tab import Employee_sales_window
# from Admin_inventory_window import Admin_inventory_window
# from employee_window import employee_window
# from Admin_finance_window import Admin_finance_window

emp_id = None

class Employee_sales_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        rel_width = 0.1
        row_height = 20

        button_font = "Helvetica 18 bold"

        Search = tk.Button(self, text = "Search")
        Search.place(relx=0.4, rely=0.35, relwidth=rel_width, height=20, anchor="e")

        Sell = tk.Button(self, text = "Sell")
        Sell.place(relx=1, rely=0.9, relwidth=rel_width, height=2, anchor="e")

        Log_out = tk.Button(self, text = "Log out",
                            command = lambda: controller.show_frame(Start_window.Start_window))
        Log_out.place(relx = 1, rely = 0, relwidth = rel_width, height=2, anchor="ne")

        Book_label = tk.Label(self, text = "Book ID", width = "15")
        Book_label.pack()
        Book_text = tk.Text(self, borderwidth = 1, relief = "groove")
        Book_text.pack()
        Book_text.place(relx=0.3, rely=0.35, relwidth=0.2, height=row_height, anchor="e")
        Book_label.place(relx=0.2, rely=0.25, relwidth=rel_width, height=row_height, anchor="e")


        Book_search = tk.Label(self, text = "Book search: ", font = button_font)
        # Found = tk.Label(self, text = "Found: ", font = button_font)
        # Title = tk.Label(self, text = "Title")
        # Author = tk.Label(self, text = "Author")
        # Edition = tk.Label(self, text = "Edition")
        # Version = tk.Label(self, text = "Version")
        # Location = tk.Label(self, text = "Location")
        # Section = tk.Label(self, text = "Section")
        # Language = tk.Label(self, text = "Language")
        # Sell_price = tk.Label(self, text = "SellPrice")
        # In_store = tk.Label(self, text = "InStore")


        Book_search.place(relx=0.25, rely=0.1, relwidth=0.2, height=row_height, anchor="e")
        # Found.place(relx=0.2, rely=0.5, relwidth=0.2, height=row_height, anchor="e")
        # Title.place(relx=0.1, rely=0.7, relwidth=rel_width, height=row_height, anchor="e")
        # Author.place(relx=0.2, rely=0.7, relwidth=rel_width, height=row_height, anchor="e")
        # Edition.place(relx=0.3, rely=0.7, relwidth=rel_width, height=row_height, anchor="e")
        # Version.place(relx=0.4, rely=0.7, relwidth=rel_width, height=row_height, anchor="e")
        # Location.place(relx=0.5, rely=0.7, relwidth=rel_width, height=row_height, anchor="e")
        # Section.place(relx=0.6, rely=0.7, relwidth=rel_width, height=row_height, anchor="e")
        # Language.place(relx=0.7, rely=0.7, relwidth=rel_width, height=row_height, anchor="e")
        # Sell_price.place(relx=0.8, rely=0.7, relwidth=rel_width, height=row_height, anchor="e")
        # In_store.place(relx=0.9, rely=0.7, relwidth=rel_width, height=row_height, anchor="e")




        # window.mainloop()

