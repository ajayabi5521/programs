'''i=1
while i==1:
     
    name=input("Enter your name:")
    age=int(input("enter your age:"))
    place=input("Enter your place:")
    #open("data1.txt","x")
    f=open("data1.txt","a")
    f.write(name +"\t"+str(age)+"\t"+place+"\n")
    i=int(input("Are you Add one more data press 1. Otherwire press any key."))'''
f=open("data1.txt","r")
n=f.read().split("\n")
p=n.pop()
for i in n:
    t=i.split("\t")
    if int(t[1]) > 25 :
        print(t[0]," : ",t[1])
        

          
