import pymysql
from ttkbootstrap import ttk,Window
from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image, ImageTk

connection=pymysql.connect(host='localhost',
                           user='root',
                           password='livewire')

try:
   
   with connection.cursor() as cursor:
        cursor.execute("USE company")
        create_table = """
        CREATE TABLE IF NOT EXISTS store(
            name VARCHAR(256),
            fname VARCHAR(256),
            age INT,
            gender VARCHAR(20),
            skill VARCHAR(256),
            address VARCHAR(256),
            location VARCHAR(20)
        )"""
        cursor.execute(create_table)
        connection.commit()
        cursor.execute(create_table)
        connection.commit()
        root=Window(themename="superhero")
        
  
         



        img=Image.open("nature.jpeg")
        photo = ImageTk.PhotoImage(img)
        la=Label(root,image=photo)
        la.place(x=0,y=0)
        frame1=Frame(root,width=500,height=50,padx=5,pady=5)
        frame1.place(relx=0.5,rely=0.15,anchor="center")

        frame=Frame(root,width=500,height=500,bg="#F2B949",pady=15,padx=20)
        frame.place(relx=0.5,rely=0.5,anchor="center")


        root.geometry("850x600")
        radio=IntVar()


        head=Label(frame1,text=" WELCOME TO STUDENT \nREGISTRATION FORM ",font=("Helvetica",18,"bold"),pady=5,background="#F2D394")
        head.grid(row=0,column=4)
        l1=Label(frame,text=" Enter your Name : \t ",background="#F2D394",font=("Helvetica",12,"bold"))
        l1.grid(row=1,column=0, sticky=W, pady=5)
        l2=Label(frame,text=" Enter your Father's Name : ",background="#F2D394",font=("Helvetica",12,"bold"))
        l2.grid(row=2,column=0,sticky=W, pady=5)
        l3=Label(frame,text=" Enter your Age : \t\t",background="#F2D394",font=("Helvetica",12,"bold"))
        l3.grid(row=3,column=0,sticky=W, pady=5)
        l4=Label(frame,text=" Choose your gender : \t",background="#F2D394",font=("Helvetica",12,"bold"))
        l4.grid(row=4,column=0,sticky=W, pady=5)
        l5=Label(frame,text=" Choose your skills : \t",background="#F2D394",font=("Helvetica",12,"bold"))
        l5.grid(row=5,column=0,sticky=W, pady=5)
        l6=Label(frame,text=" Enter your address :\t",background="#F2D394",font=("Helvetica",12,"bold"))
        l6.grid(row=6,column=0,sticky=W,pady=5)
        l7=Label(frame,text=" Select your location\t",background="#F2D394",font=("Helvetica",12,"bold"))
        l7.grid(row=7,column=0,sticky=W,pady=5)
        #Entery fields
        e1=Entry(frame,background="#A67F32",font=("Helvetica",12,"bold"))
        e1.grid(row=1,column=1)
        e2=Entry(frame,background="#A67F32",font=("Helvetica",12,"bold"))
        e2.grid(row=2,column=1)
        e3=Entry(frame,background="#A67F32",font=("Helvetica",12,"bold"))
        e3.grid(row=3,column=1)
        radio=IntVar()
        r1=Radiobutton(frame,text="Male",variable=radio,value=1,background="#A67F32",font=("Helvetica",12,"bold"))
        r1.grid(row=4,column=1)
        r2=Radiobutton(frame,text="Female",variable=radio,value=2,background="#A67F32",font=("Helvetica",12,"bold"))
        r2.grid(row=4,column=2)
        a=IntVar()
        b=IntVar()
        c=IntVar()
        d=IntVar()
        c1=Checkbutton(frame,text="Communication ",variable=a,background="#A67F32",font=("Helvetica",12,"bold")).grid(row=5,column=1,pady=2)
        c2=Checkbutton(frame,text="Colabration ",variable=b,background="#A67F32",font=("Helvetica",12,"bold")).grid(row=5,column=2,pady=2)
        c3=Checkbutton(frame,text="Leader ships ",variable=c,background="#A67F32",font=("Helvetica",12,"bold")).grid(row=5,column=3,pady=2)
        c4=Checkbutton(frame,text="Adaptive ",variable=d,background="#A67F32",font=("Helvetica",12,"bold")).grid(row=5,column=4,pady=2)
        e4=Entry(frame,background="#A67F32",font=("Helvetica",12,"bold"))
        e4.grid(row=6,column=1)
        var=IntVar()
        combo=ttk.Combobox(frame,values=["Mayiladuthurai","Chennai","Trichy","Thanjore"],background="#A67F32",font=("Helvetica",12,"bold"))
        combo.grid(row=7,column=1)
        
        def submit():
            if radio.get()==1:
                   gender="male"
            else:
                   gender="female"
            s=[]       
            if a.get()==1:
                   s.append("communication")
            if b.get()==1:
                   s.append("colabration")
            if c.get()==1:
                   s.append("Leader ships")
            if d.get()==1:
                   s.append("Adaptive")
            skill_str = ", ".join(s)    
            
            if not e1.get() or not e2.get() or not e3.get() or not radio.get() or not e4.get() or not combo.get()or not s:  
               messagebox.showwarning("Incomplete","Must fill all the field")
            else:   
               
               insert_query="""insert into store (name,fname,age,gender,skill,address,location)values(%s,%s,%s,%s,%s,%s,%s)"""
               cursor.execute(insert_query,(e1.get().upper(),e2.get(),e3.get(),gender,skill_str,e4.get(),combo.get()))                        
               connection.commit()
               print("form submitted successfully")
               messagebox.showinfo("Done !","Your form sumbitted successfully")
        def view():
         
            new_window=Toplevel(root)
            new_window.geometry("400x200")                                                                                                                                                                                
            '''def view1():
                view_query="select * from store where name=%s"
                cursor.execute(view_query,(e.get().upper))
                result=cursor.fetchall()
                for row in result:
                   print(row)
                connection.commit()'''
            def view1():
                try:
                     view_query = "SELECT * FROM store WHERE name=%s"
                     cursor.execute(view_query, (e1.get().upper(),))
                     result = cursor.fetchall()
                     e2.delete(0,END)
                     e2.insert(0,result[0][1])
                     '''
                     for row in result:
                           print(row)
                           result_out.delete("1.0", END)
                           result_out.insert(END,f"{row}\n")'''
                        
                except :
                        messagebox.showerror("Error", f"Enter correct name")
    
                     
                     
            
            lab1=Label(new_window,text="Enter your name:",font=("helvetica",11,"bold"))
            lab1.grid(row=0,column=0)
            e1=Entry(new_window,font=("Helvetica",12,"bold"))
            e1.grid(row=0,column=1)
            button=Button(new_window,text="search",command=lambda:view1(),font=("Helvetica",12,"bold"))
            button.grid(row=1,column=1)
            lab2=Label(new_window,text="Your father's name:",font=("Helvetica",12,"bold"))
            lab2.grid(row=4,column=0)
            e2=Entry(new_window,font=("Helvetica",12,"bold"))
            e2.grid(row=4,column=1)
            #result_out=Text(new_window)
            #result_out.grid(row=4,column=0,columnspan=3)
               
   
                      

           
            

        b1=Button(frame,text="Submit",activebackground="green",command=lambda:submit(),font=("Helvetica",12,"bold"))
        b1.grid(row=8,column=1,pady=5)
        b2=Button(frame,text="View",activebackground="green",font=("Helvetica",12,"bold"),command=lambda:view())
        b2.grid(row=8,column=2,pady=5)


        root.mainloop()
   
   
        

finally:
   connection.close()
