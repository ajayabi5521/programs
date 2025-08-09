import pymysql
from tkinter import *


r = Tk()
r.geometry("500x700")
r.title("Login Box")
r.configure(bg="#4d7095")
#  Footer Frame
Label(r, text="USER LOGIN FORM", font=("Arial", 17, "bold"), bg="#3399ff", fg="white").place(x=100, y=10, width=320)
#Frame(r, bg="#3399ff", height=50).pack(side='bottom', fill='x')
Label(r, text="© 2025 MyApp. All rights reserved.", bg="#3399ff", fg="white", font=("Arial", 10)).place(x=150, y=660)

# Main Form Frame
form_frame =Frame(r, bg="#ffffff", highlightbackground="#ffffff", highlightthickness=1)
form_frame.place(x=50, y=50, width=440, height=540)



Label(r, text="Name", bg="#ffffff").place(x=50, y=80)
Label(r, text="balance", bg="#ffffff").place(x=50, y=120)
Label(r, text="pinno", bg="#ffffff").place(x=50, y=160)

e1 = Entry(r)
e2 = Entry(r)
e3 = Entry(r, show="*")
e1.place(x=150, y=80, width=175)
e2.place(x=150, y=120, width=175)
e3.place(x=150, y=160, width=175)


def submit():
    insert_query = """
    INSERT INTO users (name,balance, pinno, )
    VALUES (%s, %s, %s)"""
    cursor.execute(insert_query, (e1.get(), e2.get(), e3.get()))
    connection.commit()
    print("Form submitted successfully")
Button(r, text="Submit", bg="#3399ff", command=submit).place(x=160, y=250)

r.mainloop()
connection.close()
