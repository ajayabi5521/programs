'''from tkinter import *
import webbrowser

def callback(url):
    webbrowser.open_new(url)

root = Tk()
link1 = Label(root, text="Browse here", fg="blue", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("http://www.google.com"))

link2 = Label(root, text="Hyperlink", fg="blue", cursor="hand2")
link2.pack()
link2.bind("<Button-1>", lambda e: callback("http://www.google.org"))

root.mainloop()
import tkinter as tk

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="This is Page One")
        label.pack(pady=10)
        button = tk.Button(self, text="Go to Page Two", command=lambda: controller.show_frame(PageTwo))
        button.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="This is Page Two")
        label.pack(pady=10)
        button = tk.Button(self, text="Back to Page One", command=lambda: controller.show_frame(PageOne))
        button.pack()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multi-Page Example")
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(PageOne)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()'''
from tkinter import *

# Create the main window
root = Tk()
root.title("Simple Multi-Page App")
root.geometry("400x200")

# --- Page One ---
page_one = Frame(root)

label1 = Label(page_one, text="This is Page One", font=("Arial", 16))
label1.pack(pady=20)

# Hyperlink-style label to go to Page Two
link1 = Label(page_one, text="Go to Page Two", fg="blue", cursor="hand2", font=('Arial', 12, 'underline'))
link1.pack()
link1.bind("<Button-1>", lambda e: show_page(page_two))


# --- Page Two ---
page_two = Frame(root)

label2 = Label(page_two, text="This is Page Two", font=("Arial", 16))
label2.pack(pady=20)

# Hyperlink-style label to go back to Page One
link2 = Label(page_two, text="Back to Page One", fg="blue", cursor="hand2", font=('Arial', 12, 'underline'))
link2.pack()
link2.bind("<Button-1>", lambda e: show_page(page_one))


# Function to show a specific page
def show_page(page):
    page.tkraise()

# Stack pages on top of each other
for page in (page_one, page_two):
    page.place(x=0, y=0, relwidth=1, relheight=1)

# Show the first page initially
show_page(page_one)

# Start the app
root.mainloop()


