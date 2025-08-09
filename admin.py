
    
def admin():
    uname=input("ENTER USERNAME:")
    password=input("ENTER PASSWORD:")
    if uname=="admin" and password=="admin":
        print("-----------------Welcome to Admin Login-------------------")
        m=1
        while m==1:
            print("1.Add a new customer")
            print("2.view cutomer")
            print("3.Particular view")
            print("4.Update customer details")
            i=int(input("Enter your option"))
            if i==1:
                cname=input("Enter customer name:")
                cid=int(input("Enter customer id:"))
                product=input("Enter customer product:")
                with open("info.txt","a") as file:
                    file.write(str(cid)+"\t"+cname+"\t"+product+"\n")
                    print("Customer added successfully")
            elif i==2:
                with open("info.txt","r") as f:
                    print(f.read())
            elif i==3:
                d=int(input("Enter your searching id:"))
                with open("info.txt","r") as f:
                    info=f.read().split("\n")
                    for i in info:
                        t=i.split("\t")
                        if t[0]==str(d):
                            print(t[1]," and  Product name is: ",t[2])
                            print("-----------------------------------------")
            elif i == 4:
                    edit_id = input("Enter the customer ID to edit: ")
                    new_product = input("Enter the new product name: ")

                    updated = False
                    with open("info.txt", "r") as file:
                        lines = file.readlines()

                    with open("info.txt", "w") as file:
                        for line in lines:
                            parts = line.strip().split("\t")
                            if len(parts) >= 3 and parts[0] == edit_id:
                                # Update product
                                parts[2] = new_product
                                updated = True
                                print("Customer product updated successfully.")
                            file.write("\t".join(parts) + "\n")

                    if not updated:
                        print("Customer ID not found."  )              
    
            m=int(input("Are you continue press 1.Otherwire press any key..."))    
def customer():
    print("---------------------Welcome to customer login-------------------------")
    cid=int(input("Enter customer id:"))
    cname=input("Enter username :")
    with open("info.txt","r") as file:
        f=file.read().split("\n")
        for i in f:
            t=i.split("\t")
            if str(cid)==t[0] and cname==(t[1]):
                print("Login successfully completed..")
                print("Your product is:",t[2])
                print("--------------------------------------")
                break
            
  
print("1.Admin login")
print("2.customer Login")
n=int(input("Enter your choice:"))
if n==1:
    admin()
elif n==2:
    customer()
else:
    print("Choose correct option")   
    
                

        
            
