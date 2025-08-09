def operation(n,v):
    if n==1:
        f1=-1
        f2=1
        while v>0:
            f3=f1+f2
            print(f3)
            f1=f2
            f2=f3
            v-=1
    elif n==2:
           rem=0
           b=0
           while v>0:
               rem=v%10
               b=(b*10)+rem
               v=v//10
           print(b)
    elif n==3:
        rem=0
        a=0
        while v>0:
            rem=v%10
            rem=rem*rem*rem
            a=a+rem
            v=v//10
        print(a)
    else:
        print("invalid")
