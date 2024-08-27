# snake water gun game :) ........

import numpy as np 

number = [-1 , 0 , 1]

computer = np.random.choice(number)

round = int(input("enter number of rounds \n"))
i= 1
static_computer_score = 0
static_your_score = 0 
for i in range(1,round+1):
    youstr = input("enter your choice : ")
    youDict = {"s":1 , "g" :0 , "w" : -1}
    reverseDict = {1: "snake" , -1 : "water" ,0 : "gun"}
    you = youDict[youstr] 
     
    
    print("you choose :",reverseDict[you],"\ncomputer choose :",reverseDict[computer])
    if(computer==you):
        print("game draw :) \n")
        static_computer_score +=1
        static_your_score +=1
    else:
        if(computer==-1 and you ==0):
            static_computer_score +=1
        elif(computer==-1 and you == 1):
            static_your_score+=1

        elif(computer==1 and you ==-1):
            static_computer_score +=1
        elif(computer==1 and you ==0):
            static_your_score +=1
            
        elif(computer==0 and you ==1):
            static_computer_score +=1
        elif(computer==0 and you ==0):
            static_your_score +=1
    print(f"score : \nyour score = {static_your_score}\ncomputer score ={static_computer_score}\n")
    if(static_your_score==static_computer_score):
        print("both win the game \n")
    elif(static_your_score>static_computer_score):
        print("you win the game \n")
    else:
        print("computer win \n")