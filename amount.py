cid=int(input("Enter your id:"))
eamt=int(input("Enter your update amount:"))
with open("detail.txt","r") as file:
    f=file.read().strip().split("\n")
    for i in f:
      t=i.split("\t")
      
      if int(t[0])==cid:
          amt=int(t[2])+eamt
          t[2]=str(amt)
          print("updated successfully")
          with open("detail.txt","a") as file:
                file.write("\t".join(t)+"\n")
      else:
          with open("detail.txt","a") as file:
              file.write("\t".join(t)+"\n")
           
          
