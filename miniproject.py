from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
from ttkbootstrap import ttk,Window
root=Window(themename="solar")
root.title("project")
root.geometry("550x600")
root.configure(bg="gray")
img=Image.open("ajay.jpg")
photo=ImageTk.PhotoImage(img)
image=Label(root,image=photo)
image.place(x=215,y=0)

frame1=Frame(root,height=500,width=400,bg="white")
frame1.place(x=60,y=50)
Label(root,text="WELCOME TO LOGIN PAGE\n login here",font=('Helvetic',16,'bold'),padx=15,pady=10).place(x=66,y=55)
l1=Label(root,text="Enter your eamil:",font=("Helvetica",12,"bold"))
l1.place(x=80,y=120)
e1=Entry(root,width=30)
e1.place(x=230,y=120)
l2=Label(root,text="Enter your\n username:",font=("Helvetica",12,"bold"))
l2.place(x=80,y=160)
e1=Entry(root,width=30)
e1.place(x=230,y=165)
