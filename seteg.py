i=1
while i==1:
    name=[]
    phone=[]
    email=[]
    n=input("Enter your name:")
    ph=input("Enter your phone number:")
    emil=input("Enter your email id:")
    name.append(n)
    phone.append(ph)
    email.append(emil)
    if i==1:
        i=int(input("Are you continue press 1.Otherwise press any key"))
        
print("Data are inserted succeesully")
a=set(name)
b=set(phone)
c=set(email)
print("1.Name")
print("2.Phone")
print("3.email")
m=int(input("Enter your serching optino:"))
n=input("Enter your searching name:")

if m==1:
     a1={n for x in a if x in n}
elif m==2:
    b2={n for x in b if x in n}
elif m==3:
    c3={n for x in c if x in n}
else:
    print("choose correct option")



