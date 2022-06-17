from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x500")

my_tree = ttk.Treeview(root)

my_tree['columns']= ("Name", "ID","Favorite Pizza")

#columns
my_tree.column("#0", width=120, minwidth=25)
my_tree.column("Name", anchor=W, width=120)
my_tree.column("ID", anchor=CENTER, width=80)
my_tree.column("Favourite Pizza", anchor=W, width=120)

#heading
my_tree.heading("#0", text"Label", anchor=W)
my_tree.heading("Name", text"Name", anchor=W)



root.mainloop()
