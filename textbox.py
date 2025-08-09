'''from tkinter import*
root=Tk()
l1=Label(text="Enter your information:")
l1.grid(row=0,column=0)
text2=Text(root,height=5,width=60)
text2.grid(row=0,column=1,columnspan=6)
def content():
    info=str(text2.get("1.0", "end-1c"))
    with open("content.txt","a") as f:
        f.write(info+"\n")

button=Button(text="upload to file",activebackground="green",command=lambda:content())
button.grid(row=5,column=5)
l2=Label(root,text="Enter your password:").grid(row=6,column=0)
e1=Entry(root,show="*").grid(row=6,column=1)
root.geometry("500x500")
from tkinter import*
root=Tk()
L1=Label(text="Choose your skills").grid(row=0,column=0)
c1=Checkbutton(root,text="Communication").grid(row=0,column=1)
c2=Checkbutton(root,text="Colabration").grid(row=0,column=2)
        
root.geometry("200x200")
root.mainloop
from tkinter import *
from tkinter import ttk
root=Tk()
Label(root,text="Choose you location:  ").grid(row=0,column=0)
print("\t")
com=ttk.Combobox(root,values=["Mayiladuthurai","Chennai","Thanjore","Trichy"])
com.grid(row=0,column=1)
def choose():
    select=com.get()
    print(f"You selected {select} City .Wecome to {select}")
    com.bind()
    
Button(text="upload my city",activebackground="green",command=choose).grid(row=1,column=1)
root.mainloop()

from tkinter import *
root=Tk()
radio=IntVar()
Label(text="Gender").grid(row=0,column=0)
r1=Radiobutton(root,text="Male",variable=radio,value=1).grid(row=0,column=1)
r2=Radiobutton(root,text="Female",variable=radio,value=2).grid(row=0,column=2)
root.mainloop()
'''
from tkinter import*
from PIL import Image
from PIL.ImageTk import PhotoImage

root=Tk()
root.geometry("1000x1000")
img=PhotoImage(Image.open("nature.jpeg"))
label=Label(root,image=img)
label.pack()
root.mainloop() 



    
    

