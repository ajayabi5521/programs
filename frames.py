import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Header-Body-Footer Layout")
root.geometry("600x400")  # width x height

# --- Header Frame ---
header_frame = tk.Frame(root, bg='lightblue', height=50)
header_frame.pack(fill='x')  # fill horizontally

header_label = tk.Label(header_frame, text="Header", bg='lightblue', font=('Arial', 16, 'bold'))
header_label.pack(pady=10)

# --- Body Frame ---
body_frame = tk.Frame(root, bg='white')
body_frame.pack(fill='both', expand=True)  # expands to fill available space

body_label = tk.Label(body_frame, text="Main Body Content Here", bg='white', font=('Arial', 14))
body_label.pack(pady=20)

# You could also add widgets like Entry, Treeview, etc. here

# --- Footer Frame ---
footer_frame = tk.Frame(root, bg='lightgrey', height=40)
footer_frame.pack(fill='x')

footer_label = tk.Label(footer_frame, text="Footer", bg='lightgrey')
footer_label.pack(pady=10)

# Run the app
root.mainloop()
'''
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Multiple Frame Layout")
root.geometry("800x500")  # width x height

# --- Header Frame ---
header_frame = tk.Frame(root, bg='lightblue', height=60)
header_frame.pack(side='top', fill='x')

header_label = tk.Label(header_frame, text="Header", bg='lightblue', font=('Arial', 16, 'bold'))
header_label.pack(pady=15)

# --- Body Frame (contains sidebar and main content) ---
body_frame = tk.Frame(root)
body_frame.pack(fill='both', expand=True)

# --- Sidebar Frame ---
sidebar_frame = tk.Frame(body_frame, bg='lightgrey', width=200)
sidebar_frame.pack(side='left', fill='y')

sidebar_label = tk.Label(sidebar_frame, text="Sidebar", bg='lightgrey')
sidebar_label.pack(pady=10)

# --- Main Content Frame ---
main_frame = tk.Frame(body_frame, bg='white')
main_frame.pack(side='left', fill='both', expand=True)

main_label = tk.Label(main_frame, text="Main Content Area", bg='white', font=('Arial', 14))
main_label.pack(pady=20)

# --- Footer Frame ---
footer_frame = tk.Frame(root, bg='lightblue', height=40)
footer_frame.pack(side='bottom', fill='x')

footer_label = tk.Label(footer_frame, text="Footer", bg='lightblue')
footer_label.pack(pady=10)

# Run the app
root.mainloop()'''

