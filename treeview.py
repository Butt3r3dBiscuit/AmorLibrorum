from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x500")

my_tree = ttk.Treeview(root)

my_tree['columns']= ("ISBN", "Title","Price") #author too Ig

#columns
my_tree.column("#0", width=20)
my_tree.column("ISBN", anchor=CENTER, width=120)
my_tree.column("Title", anchor=CENTER, width=80)
my_tree.column("Price", anchor=E, width=120)

#heading
my_tree.heading("#0", text="", anchor=CENTER)
my_tree.heading("ISBN", text="ISBN", anchor=CENTER)
my_tree.heading("Title", text="Title", anchor=CENTER)
my_tree.heading("Price", text="Price", anchor=CENTER)

# data = [
#  ('Book Lovers', 'Emily', 'Henry', 'English', 'Sisters Fiction, Romantic Comedy', 17, None, 'paperback', -1222, 1),
#  ("Oh, the Places You'll Go!", 'Theodor', 'Seuss Geisel', 'English', 'Children Classics', 77, None, None, -898, 1),
#  ('Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones', 'James', 'Clear', 'English', 'Psychology', 11, None, 'hardcover', -1198, 1),
#  ('Where the Crawdads Sing', 'Delia', 'Owens', 'English', 'Fiction', 7, None, 'paperback', -998, 3),
#  ("Phil: The Rip-Roaring (and Unauthorized!) Biography of Golf's Most Colorful Superstar", 'Alan', 'Shipnuck', 'English', 'Biographies', 747, None, 'hardcover', -2499, 3),
#  ('It Ends with Us', 'Colleen', 'Hoover', 'English', 'College Romance, Fiction', 78, None, 'paperback', -1081, 9), ('The Seven Husbands of Evelyn Hugo: A Novel', 'Taylor', 'Jenkins Reid', 'English', 'Holiday Romance', 2, None, 'paperback', -942, 1),
#  ('Verity', 'Colleen', 'Hoover', 'English', 'Suspense, Thriller', 74, None, 'paperback', -1126, 1), ('Priesaikos laužytojas', 'Leena', 'Lehtolainen', 'Lithuanian', 'Thriller, Suspense, Romantic', 2, 1, 'hardcover', -739, 1)]


# my_tree.insert(parent='', index='end', iid=0, values=("9780593334833", "Book Lovers", "1479"))
my_tree.insert(parent='', index='end', iid=0, values=("978059", "Book Lovers", "1479"))

my_tree.insert(parent='0', index='end', iid=1, values=("extra", "more", "stuff"))

my_tree.pack(pady=20)
root.mainloop()
