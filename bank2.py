details={'amt':0}
def create():
    name=input("Enter account holder name:")
    accno=7
    while accno>8 or accno<8:
        num=int(input("Enter 8-digit account number:"))
        accno=len(str(num))
    mo=11
    while mo>10 or mo<10:
          phone=int(input("Enter your phone number:"))
          mo=len(str(phone))
    
    amountt=0
    while amountt==0:
        amt=int(input("Enter your initial deposit amount:"))
        amountt=len(str(amt))
    detail={'name':'name','accno':'accno','phone':'phone','amt':amt}
    details.update(detail)
def deposite():
    amount=int(input("Enter your depsit amt"))
    if amount>0:
           print(f"Your deposite amount {amount}.Current balance is {(details['amt'])+amount}")
           d=details['amt']+amount
           details['amt']=d
    else:
        print(f"you can't withdraw this {amount} amount.")
def withdraw(): 
    amount=int(input("Enter your widthdraw amount:"))
    if details['amt']>=amount:
           print(f"your widthdraw amount {amount}.Current balance is{(details['amt'])-amount}")
           d=details['amt']-amount
           details['amt']=d
    else:
        print("Insufficient balance")
    

 


while True:
    print("1.Create")
    print("2.Deposite")
    print("3.Withdraw")
    print("4.exit")
    i=int(input("Enter your operation:"))
    if i==1:
          create()
    elif i==2:
         deposite()
    elif i==3:
        withdraw()
    elif i==4:
        break
    else:
        print("choose correct option")
print("Thank you")        



