
def operation(n,*a):
    
    
    if n==1:
        a1=0
        for i in a:
            a1=i+a1
        print(a1)
    elif n==2:
        a1=0
        for i in a:
            a1=i-a1
        print(a1)
    elif n==3:
        a1=1
        for i in a:
            a1=a1*i
        print(a1)
    elif n==4:
        a1=1
        for i in a:
            a1=a1/i
        print(a1)
    else:
        print("Choose correct option")
'''           
def operation(n,*a):
    ans=0
    for c in a:
        if n==1:
            ans+=c
        elif n==2:
            ans-=1
        elif n==3:
            if ans==0:
                 ans+=1
            ans*=c
        elif n==4:
            ans/=c
    return (ans)
        
        
'''    
      



n=int(input('''Enter your operation:
1.add
2.sub
3.mul
4.div'''))
a=input("Enter a values")
b=map(int,a.split())

print(operation(n,*b))






    

           






















    
