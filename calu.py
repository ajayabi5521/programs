while True:
    try:
       a=int(input("Enter a value:"))
       b=int(input("Enter b value:"))
    except ValueError:
        print("Enter correct input value!")
                
    else:                                                            
        print("1.Enter your operation.")
        print("1.Addition")
        print("2.sub")
        print("3.mul")
        print("4.div")
        n=int(input("enter your operation"))    
        if n==1:
             print(a+b)
        elif n==2:
                 print(a-b)
        elif n==3:
                   print(a*b)
        elif n==4:
              try:
                    c=a/b
                    print(c)
      
                                                         
              except ZeroDivisionError:
                    print("zero is doesnot divisible")
        else:
            print("Chhose correct option")                                             
                                                                                           
            
        
          
         
