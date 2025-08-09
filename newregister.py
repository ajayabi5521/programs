import pymysql
from ttkbootstrap import Window
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Connect to MySQL
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='livewire'
)

try:
    with connection.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS company")
        cursor.execute("USE company")
        create_table = """
        CREATE TABLE IF NOT EXISTS store (
            name VARCHAR(256),
            fname VARCHAR(256),
            age INT,
            gender VARCHAR(20),
            skill VARCHAR(256),
            address VARCHAR(256),
            location VARCHAR(20)
        )
        """
        cursor.execute(create_table)
        connection.commit()

    # Tkinter Window setup
    root = Window(themename="superhero")
    root.geometry("850x600")

    img = Image.open("nature.jpeg")
    photo = ImageTk.PhotoImage(img)
    la = Label(root, image=photo)
    la.place(x=0, y=0)

    frame1 = Frame(root, width=500, height=50, padx=5, pady=5)
    frame1.place(relx=0.5, rely=0.15, anchor="center")

    frame = Frame(root, width=500, height=500, bg="#F2B949", pady=15, padx=20)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    radio = IntVar()

    head = Label(frame1, text=" WELCOME TO STUDENT \nREGISTRATION FORM ",
                 font=("Helvetica", 18, "bold"), pady=5, background="#F2D394")
    head.grid(row=0, column=4)

    # Labels
    Label(frame, text=" Enter your Name : \t ", background="#F2D394", font=("Helvetica", 12, "bold")).grid(row=1, column=0, sticky=W, pady=5)
    Label(frame, text=" Enter your Father's Name : ", background="#F2D394", font=("Helvetica", 12, "bold")).grid(row=2, column=0, sticky=W, pady=5)
    Label(frame, text=" Enter your Age : \t\t", background="#F2D394", font=("Helvetica", 12, "bold")).grid(row=3, column=0, sticky=W, pady=5)
    Label(frame, text=" Choose your gender : \t", background="#F2D394", font=("Helvetica", 12, "bold")).grid(row=4, column=0, sticky=W, pady=5)
    Label(frame, text=" Choose your skills : \t", background="#F2D394", font=("Helvetica", 12, "bold")).grid(row=5, column=0, sticky=W, pady=5)
    Label(frame, text=" Enter your address :\t", background="#F2D394", font=("Helvetica", 12, "bold")).grid(row=6, column=0, sticky=W, pady=5)
    Label(frame, text=" Select your location\t", background="#F2D394", font=("Helvetica", 12, "bold")).grid(row=7, column=0, sticky=W, pady=5)

    # Entry fields
    e1 = Entry(frame, background="#A67F32", font=("Helvetica", 12, "bold"))
    e1.grid(row=1, column=1)
    e2 = Entry(frame, background="#A67F32", font=("Helvetica", 12, "bold"))
    e2.grid(row=2, column=1)
    e3 = Entry(frame, background="#A67F32", font=("Helvetica", 12, "bold"))
    e3.grid(row=3, column=1)

    # Gender radio
    r1 = Radiobutton(frame, text="Male", variable=radio, value=1, background="#A67F32", font=("Helvetica", 12, "bold"))
    r1.grid(row=4, column=1)
    r2 = Radiobutton(frame, text="Female", variable=radio, value=2, background="#A67F32", font=("Helvetica", 12, "bold"))
    r2.grid(row=4, column=2)

    # Skills checkboxes
    a = IntVar()
    b = IntVar()
    c = IntVar()
    d = IntVar()
    Checkbutton(frame, text="Communication ", variable=a, background="#A67F32", font=("Helvetica", 12, "bold")).grid(row=5, column=1, pady=2)
    Checkbutton(frame, text="Colabration ", variable=b, background="#A67F32", font=("Helvetica", 12, "bold")).grid(row=5, column=2, pady=2)
    Checkbutton(frame, text="Leader ships ", variable=c, background="#A67F32", font=("Helvetica", 12, "bold")).grid(row=5, column=3, pady=2)
    Checkbutton(frame, text="Adaptive ", variable=d, background="#A67F32", font=("Helvetica", 12, "bold")).grid(row=5, column=4, pady=2)

    e4 = Entry(frame, background="#A67F32", font=("Helvetica", 12, "bold"))
    e4.grid(row=6, column=1)

    combo = ttk.Combobox(frame, values=["Mayiladuthurai", "Chennai", "Trichy", "Thanjore"], font=("Helvetica", 12, "bold"))
    combo.grid(row=7, column=1)

    # Submit function
    def submit():
        gender = "male" if radio.get() == 1 else "female"
        skills = []
        if a.get(): skills.append("communication")
        if b.get(): skills.append("colabration")
        if c.get(): skills.append("leader ships")
        if d.get(): skills.append("adaptive")
        skill_str = ", ".join(skills)

        cursor = connection.cursor()
        insert_query = """INSERT INTO store (name, fname, age, gender, skill, address, location)
                          VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(insert_query, (
            e1.get().upper(), e2.get(), e3.get(), gender, skill_str, e4.get(), combo.get()
        ))
        connection.commit()
        cursor.close()
        print("Form submitted successfully!")

    # View function
    def view():
        new_window = Toplevel(root)
        new_window.title("Database Records")
        new_window.geometry("800x400")

        new_cursor = connection.cursor()
        new_cursor.execute("SELECT * FROM store")
        rows = new_cursor.fetchall()
        columns = [desc[0] for desc in new_cursor.description]

        tree = ttk.Treeview(new_window, columns=columns, show='headings')

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=100)

        for row in rows:
            tree.insert('', END, values=row)

        tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(new_window, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        new_cursor.close()

    # Buttons
    Button(frame, text="Submit", activebackground="green", command=submit, font=("Helvetica", 12, "bold")).grid(row=8, column=1, pady=5)
    Button(frame, text="View", activebackground="green", command=view, font=("Helvetica", 12, "bold")).grid(row=8, column=2, pady=5)

    root.mainloop()

finally:
    connection.close()
