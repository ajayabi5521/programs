import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tree View Example")

tree = ttk.Treeview(root)

# Define columns
tree['columns'] = ('Size', 'Modified')

# Format columns
tree.column('#0', width=150, anchor='w')  # This is the tree column
tree.column('Size', anchor='center', width=200)
tree.column('Modified', anchor='center', width=200)

# Headings
tree.heading('#0', text='File Name', anchor='center')
tree.heading('Size', text='Size')
tree.heading('Modified', text='Modified')

# Insert data
tree.insert('', 'end', text='Folder1', values=('---', 'Today'))
tree.insert('', 'end', text='File1.txt', values=('15 KB', 'Yesterday'))

# Nested item
folder2 = tree.insert('', 'end', text='Folder2', values=('---', 'This Week'))
tree.insert(folder2, 'end', text='SubFile.txt', values=('2 KB', 'This Week'))

tree.pack(expand=True, fill='both')
root.mainloop()
