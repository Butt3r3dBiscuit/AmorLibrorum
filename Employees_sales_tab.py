import tkinter as tk
import Start_window

emp_id = None

class Employee_sales_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        rel_width = 0.1
        row_height = 20
        button_height = 45
        text_height = 20
        title_height = 30


        Search = tk.Button(self, text = "Search")
        Search.place(relx=0.4, rely=0.35, relwidth=rel_width, height=20, anchor="e")

        Sell = tk.Button(self, text = "Sell")
        Sell.place(relx=1, rely=0.9, relwidth=rel_width, height=2, anchor="e")

        Log_out = tk.Button(self, text = "Log out",
                            command = lambda: controller.show_frame(Start_window.Start_window))
        Log_out.place(relx = 1, rely = 0, relwidth = rel_width, height=2, anchor="ne")

        Book_label = tk.Label(self, text = "Book ID", width = "15")
        Book_label.pack()
        Book_text = tk.Text(self, borderwidth=1, relief="groove")
        Book_text.pack()
