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
