import random

class Ran():
    
    def printRound(self,i): #Used to print No of Rounds and similarly taking input
        self.i=i
        print('*'*20,'\n')
        print('Round ',self.i,'\n')
        print('*'*20,'\n') 
        print('Guess the Number in between ',self.a,' and ',self.b,' : \n')
        self.num=int(input())    
     
    def ran(self,a,b): #Used to take random values in the range of a and b
        self.a=a
        self.b=b
        self.r=random.randint(self.a,self.b)
        return self.r
    
    def gOrL(self): #if num great than random or num less random will display and helps user to find number
        if self.num>self.r:
                 print('It is greater!')
        elif self.num<self.r:
                 print('It is Lesser!')
    
    def valid(self): #here it validates the num given by user and num provided by computer
        self.res=False
        if self.num==self.r:
            self.res=True
        else:
            self.res=False
        return self.res
        
    def wonOrLost(self): #Here finally declares the user as winner or looser
        
        if self.valid():
            print('You Won!',chr(128525),'\n')
        else:
            print('You Lost!',chr(128532),'\n')
        print(self.r,' Was Answer')