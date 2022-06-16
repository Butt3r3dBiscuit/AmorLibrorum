import tkinter as tk
import Start_window
import Admin_inventory_window
import Admin_finance_window

class employee_window(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        rel_width = 0.1
        rel_height = 0.05

        # Window
        # window = Tk()
        # width= window.winfo_screenwidth()
        # height= window.winfo_screenheight()
        # window.geometry("%dx%d" % (width, height))
        # window.title("Employee Window")
        
        
        
        #Buttons
        Employee = tk.Button(self, text="Employee", state="disabled")
        Finance = tk.Button(self, text="Finance",command=lambda: controller.show_frame(Admin_finance_window.Admin_finance_window))
        Inventory = tk.Button(self, text="Inventory",
                              command=lambda: controller.show_frame(Admin_inventory_window.Admin_inventory_window))
        Log_out = tk.Button(self, text="Log out", command=lambda: controller.show_frame(Start_window.Start_window))

        
        
        #Text
        Book_search = tk.Label(self, text="Book Search")
        Title = tk.LabelFrame(self, text="Title")
        Author = tk.LabelFrame(self, text="Author")
        Editor = tk.LabelFrame(self, text="Editor")
        Version = tk.LabelFrame(self, text="Version")
        Language = tk.LabelFrame(self, text="Language")
        All = tk.LabelFrame(self, text="All")
        
        
        #Placement Buttons
        Employee.place(relx=1, relwidth=rel_width, relheight=rel_height, anchor="ne")
        Finance.place(relx=0.9, relwidth=rel_width, relheight=rel_height, anchor="ne")
        Inventory.place(relx=0.8, relwidth=rel_width, relheight=rel_height, anchor="ne")
        Log_out.place(relx=0,rely=0,relwidth=rel_width, relheight=rel_height, anchor="nw")


        # Placement Text
        Book_search.place(relx=0.18, rely=0.15, relwidth=rel_width, relheight=rel_height, anchor="e")
        Title.place(relx=0.2, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor="e")
        Author.place(relx=0.35, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor="e")
        Editor.place(relx=0.5, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor="e")
        Version.place(relx=0.65, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor="e")
        Language.place(relx=0.8, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor="e")
        All.place(relx=0.95, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor="e")

    def test_emp_id(self):
        print(Admin_inventory_window.emp_id)
        print('this is just to test that we have the emp_id loaded - not sure if we need it here but ye')
        print("we could make it so that in one of the corners there would be sth like logged as:")
