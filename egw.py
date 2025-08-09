def adam(n,*s):
    for v in s:
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
n=1            
adam(n,11,55,44,88,77)
