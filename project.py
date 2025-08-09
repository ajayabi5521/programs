o=1
while o==1:
    n=int(input('''Enter your option:
1.fibonacci series
2.reverse nuber
3.adam number\n'''))
    if n==1:
          v=int(input("Enter your number:"))
          f1=-1
          f2=1
          while v>0:
                f3=f1+f2
                print(f3)
                f1=f2
                f2=f3
                v-=1
    elif n==2:
        v=int(input("Enter your number:"))
        rem=0
        b=0
        while v>0:
            rem=v%10
            b=(b*10)+rem
            v=v//10
        print(b)
    elif n==3:
        v=int(input("Enter your number"))
        rem=0
        a=0
        while v>0:
            rem=v%10
            rem=rem*rem*rem
            a=a+rem
            v=v//10
        print(a)
    else:
        print("Choose corect option..!")
    if o==1:
              o=int(input("Are you continue press 1 otherwire press any key\n"))
    
