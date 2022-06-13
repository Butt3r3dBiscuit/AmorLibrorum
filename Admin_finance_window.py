from tkinter import *

rel_width = 0.1
rel_height = 0.05

#Window
window = Tk()
width= window.winfo_screenwidth()
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.title("Employee Window")

#Buttons
Employee = Button(window, text="Employee")
Finance = Button(window, text="Finance")
Inventory = Button(window, text="Inventory")
Delete = Button(window, text="Delete")

#text
Search_records = Label(window, text="Search records: ", font='Helvetica 18 bold')
Found_books = Label(window, text="Found Books: ", font='Helvetica 18 bold')
Title = Label(window, text="Title")
Author = Label(window, text="Author")
Edition = Label(window, text="Edition")
Version = Label(window, text="Version")
Buy_price = Label(window, text="BuyPrice")
Sold_price = Label(window, text="SoldPrice")
Number_of_sales = Label(window, text="NumberOfSales")
Profit_margin = Label(window, text="Profit Margin: ", font='Helvetica 18 bold')
Sold_min_buy = Label(window, text="(SoldPrice - BuyPrice)/BuyPrice")
Set_margin = Label(window, text="Set Margin To: ", font='Helvetica 18 bold')
Delete_text = Label(window, text="Delete Sell Records Older Than 5 Years: ", font='Helvetica 18 bold')

#Placement Buttons
Employee.place(relx=1, relwidth=rel_width, relheight=rel_height, anchor=NE)
Finance.place(relx=0.9, relwidth=rel_width, relheight=rel_height, anchor=NE)
Inventory.place(relx=0.8, relwidth=rel_width, relheight=rel_height, anchor=NE)
Delete.place(relx=0.2, rely=0.75, relwidth=rel_width, relheight=rel_height, anchor=E)

Search_records_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Search_records_text.pack()
Search_records_text.place(relx=0.3, rely=0.15, relwidth=0.2, relheight=rel_height, anchor=E)

Margin_text = Text(window, height=0.5, width=30, borderwidth=1, relief="groove")
Margin_text.pack()
Margin_text.place(relx=0.7, rely=0.5, relwidth=rel_width, relheight=rel_height, anchor=E)



#placement Text
Search_records.place(relx=0.2, rely=0.1, relwidth=rel_width, relheight=rel_height, anchor=E)
Found_books.place(relx=0.2, rely=0.3, relwidth=rel_width, relheight=rel_height, anchor=E)
Title.place(relx=0.2, rely=0.35, relwidth=rel_width, relheight=rel_height, anchor=E)
Author.place(relx=0.3, rely=0.35, relwidth=rel_width, relheight=rel_height, anchor=E)
Edition.place(relx=0.4, rely=0.35, relwidth=rel_width, relheight=rel_height, anchor=E)
Version.place(relx=0.5, rely=0.35, relwidth=rel_width, relheight=rel_height, anchor=E)
Buy_price.place(relx=0.6, rely=0.35, relwidth=rel_width, relheight=rel_height, anchor=E)
Sold_price.place(relx=0.7, rely=0.35, relwidth=rel_width, relheight=rel_height, anchor=E)
Number_of_sales.place(relx=0.8, rely=0.35, relwidth=rel_width, relheight=rel_height, anchor=E)
Profit_margin.place(relx=0.2, rely=0.5, relwidth=rel_width, relheight=rel_height, anchor=E)
Sold_min_buy.place(relx=0.3, rely=0.55, relwidth=0.2, relheight=rel_height, anchor=E)
Set_margin.place(relx=0.6, rely=0.5, relwidth=rel_width, relheight=rel_height, anchor=E)
Delete_text.place(relx=0.375, rely=0.7, relwidth=0.3, relheight=rel_height, anchor=E)


window.mainloop()
