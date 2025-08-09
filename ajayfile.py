#open("input.txt","x")
'''f=open("input.txt","w")
f.write("Welcome to Mayiladuthurai")

n=int(input("How many name's you will Enter:"))
for i in range(1,n+1):


    name=input(f"Enter your {i}name:")
    f=open("input.txt","a")
    f.write(name+"\n")

file=open("input.txt","r")
print(file.read())
file=open("input.txt","w")
file.write("Welcome to My home")
f=open("input.txt","r")
print(f.read())'''
n=int(input("Which table is you want ?"))
for i in range(1,11):
    f=open("input.txt","a")
    f.write(f"{i} X {n} ={i*n}"+"\n")
with open('input.txt', 'a') as i:
    i.write("welcome to table values")
with open("input.txt","r") as i:
    print(i.read())
    
       
    

