def fibo(n,v):
        f1=-1
        f2=1
        while v>0:
            f3=f1+f2
            print(f3)
            f1=f2
            f2=f3
            v-=1
def reverse(n,v):            
           rem=0
           b=0
           while v>0:
               rem=v%10
               b=(b*10)+rem
               v=v//10
           print(b)
def adam(n,v):
        rem=0
        b=0
        z=v
        while v>0:
               rem=v%10
               b=(b*10)+rem
               v=v//10
        print(b)
        v1=z*z
        print(v1)
        b1=b*b
        s=0
        while b1>0:
            rem=b1%10
            s=(s*10)+rem
            b1=b1//10
            
        print(s)
        if v1==s:
            print("Adam number")
        else:
            print("Not adam number")
       
def mainfun():
    i=1
    while i==1:
    
       n=int(input('''Enter your operation
1.fibo
2.reverse
3.Adam number\n'''))
       if n<4 and n>0:
             v=int(input("Enter your number"))
       
       if n==1:
           fibo(n,v)
       elif n==2:
           reverse(n,v)
       elif n==3:
           adam(n,v)
       else:
            print("Choose correct option")
       if i==1:
           i=int(input("Are yor continue press 1 otherwire press any key"))
print("Are you perform mathematical operation press 1")
i=int(input("Otherwire press any key"))
if i==1:
    mainfun()
print("Thank you")    









"""
i=1
while i==1:
    
       n=int(input('''Enter your operation
1.fibo
2.reverse
3.Adam number\n'''))
       v=int(input("Enter your number"))
       if n==1:
           fibo(n,v)
       elif n==2:
           reverse(n,v)
       elif n==3:
           adam(n,v)
       else:
            print("Choose correct option")
       if i==1:
           i=int(input("Are yor continue press 1 otherwire press any key"))
print("Thank you!")
"""





    
    
