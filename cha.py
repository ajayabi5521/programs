import tkinter as tk
from tkinter import messagebox

# Function to check login
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Create main window
root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")

# Username label and entry
tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# Password label and entry
tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Login button
tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()
