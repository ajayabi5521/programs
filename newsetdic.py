d={}
i=1
while i==1:
    name=input("Enter a name:")
    phone=int(input("Enter a phone no:"))
    email=input("Enter your email i'd:")
    d[name]=(phone,email)
    if i==1:
        i=int(input("Are you continue press 1.Otherwise press any key"))
        
print(d)

sets = set(d.values()) 
print("Set of contact info:", sets)
