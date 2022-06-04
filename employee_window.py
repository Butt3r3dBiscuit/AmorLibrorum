import tkinter as tk
import Start_window
import Admin_inventory_window

class employee_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        rel_width = 0.1
        rel_height = 0.05
        
        
        
        #Window
        # window = Tk()
        # width= window.winfo_screenwidth()
        # height= window.winfo_screenheight()
        # window.geometry("%dx%d" % (width, height))
        # window.title("Employee Window")
        
        
        
        #Buttons
        Financial = tk.Button(self, text="Financial")
        Add_book = tk.Button(self, text="Add Book", command=lambda: controller.show_frame(Admin_inventory_window.Admin_inventory_window))
        Sell = tk.Button(self, text="Sell")
        Add_employee = tk.Button(self, text="Add Employee")
        
        
        #Text
        Book_search = tk.Label(self, text="Book Search")
        Title = tk.LabelFrame(self, text="Title")
        Author = tk.LabelFrame(self, text="Author")
        Editor = tk.LabelFrame(self, text="Editor")
        Version = tk.LabelFrame(self, text="Version")
        Language = tk.LabelFrame(self, text="Language")
        All = tk.LabelFrame(self, text="All")
        
        
        #Placement Buttons
        Financial.place(relx=1, relwidth=rel_width, relheight=rel_height, anchor="ne")
        Add_book.place(relx=0.9, relwidth=rel_width, relheight=rel_height, anchor="ne")
        Sell.place(relx=0.8, relwidth=rel_width, relheight=rel_height, anchor="ne")
        Add_employee.place(relx=0.7, relwidth=rel_width, relheight=rel_height, anchor="ne")
        
        #Placement Text
        Book_search.place(relx=0.18, rely=0.15, relwidth=rel_width, relheight=rel_height, anchor="e")
        Title.place(relx=0.2, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor="e")
        Author.place(relx=0.35, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor="e")
        Editor.place(relx=0.5, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor="e")
        Version.place(relx=0.65, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor="e")
        Language.place(relx=0.8, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor="e")
        All.place(relx=0.95, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor="e")
    
