import numpy as np 

number = [1,2,3,4,5,6,7,8]

computer_number = np.random.choice(number)

class guess_number:
    num =""
    times = 0
    def __init__(self , computer_number ):
        self.computer_number = computer_number 


    def play(self):
        while(self.computer_number!=self.num):
            self.num = int(input("enter a number : "))
            if(self.computer_number>self.num):
                print("enter greater number \n")
                self.times +=1 
            elif(self.computer_number<self.num):
                print("enter smaller number \n")
                self.times +=1 
            elif(self.computer_number==self.num):
                print(f"computer number = {self.computer_number}\nuser number ={self.num}")
                print(f"you guess correct number in {self.times+1} times\n")
            else:
                print("invalid input\n")

o = guess_number(computer_number)
o.play()