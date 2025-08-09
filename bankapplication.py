def manager():
    uname=input("ENTER USERNAME:")
    password=input("ENTER PASSWORD:")
    if uname=="admin" and password=="admin":
        print("-----------------------Welcome to manager login----------------------")
        print("1.Add new customer")
        print("2.View customer details")
        print("3.Edit customer details ")
        n=int("Enter your operation  Mr.Adin:")
        if n==1:
            newcutomer()
        elif n==2:
            viewcustomerdetails()
        elif n==3:
            editcustomerdetailsparticular()
        else:
            print("choose correct opeeration ....1")
def newcustomer():
    name=input("Enter customer name:")
    accno=int(input("Enter customer account no:"))
    amt=int(input("Enter customer inidial deposit amount:"))
    with open("detail.txt","a") as file:
            file.write(accno+"\t"+name+"\t"+str(amt)+"\n")
def viewcustomerdetails():
    with open("details.txt","r") as file:
        print(file.read())
def  editcustomerdetailsparticular():
    cid=int("Enter customer id:")
    eamt=input("Enter amount:")
    uploated=False
    
    with open("details.txt","r") as file:
        lines=file.readlines()
        
       
        with open("deails.txt","w") as file:
            for line in lines:
                parts=line.strip().split("\t")
                if parts[0]==cid:
                    parts[2]=eamt
                    updated=True
                    print("updated successfully")
                file.wirte("\t".join(parts)+"\n")
            if not updated:
                print("customer id not found")
            
        
        
    
            
