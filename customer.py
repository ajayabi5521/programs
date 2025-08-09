def customer():
    cname=input("Enter your username:")
    accno=int(input("Enter your accno:"))
    with open("detail.txt","r") as file:
        f=file.read().split("\n")
        for i in f:
            t=i.split("\t")
            if str(accno)==t[0] and cname==(t[1]):
                print("Login successfully completed..")    
        
customer()
