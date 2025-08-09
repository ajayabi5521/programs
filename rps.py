
import random

i=1
while True:
    detail={1:'Rock',2:'paper',3:'scissor'}
    
    player=int(input("Enter ...\n 1 for Rock \n 2 for Paper \n 3 for Scissor\n"))
    computer=int(random.choice("123"))
    if player>0 and player<4:
        print("you choose",detail[int(player)])
        print("Computer choose",detail[int(computer)])
    
        if player==1 and computer==3 :
            print("you win")
        elif player==3 and computer==2 :
            print("You win")
        elif player== 2 and computer==3:
            print("you win")
        elif player==computer:
            print("Match draw or tie")
        else:
            print("computer win")
    
