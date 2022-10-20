from RandomNum import Ran

class Game(Ran): #inherited Ran class to Game class
    def __init__(self): 
        #which gives welcoe messsage to user
        print('*'*40,'\n')
        print('Hello Welcome to Guess The number Game\n')
        print('*'*40,'\n')
        #whic used to take input from user and store as choice
        print('Enter your choices : [1,3,5]')
        self.choice=int(input()) 
    
    def rounds(self):
        R=Ran() #creation of Ran class obj
        #selection of choices
        if self.choice==1:
            R.ran(1,10)
        elif self.choice==3:
            R.ran(1,50)
        elif self.choice==5:
            R.ran(1,100)
        for i in range(1,self.choice+1):
            R.printRound(i)
            if self.choice==3 or self.choice==5:
                if R.num==R.r:
                    break #if we got guessing correct at initial so we break remaining
                else:
                    R.gOrL() # for more than 1 choice we gives some hint!
                
        R.wonOrLost()
        return (self.choice-(i))
        
    def stat(self,s): #which provides the stats of recent
        self.s=s
        return ((self.s/self.choice)*100 )                  
g=Game()#creation of Game class object
avg=g.rounds() #Calling rounds method and collecting the at which place he passed value
print('Your percentage is ',g.stat(avg),' %') #printing stats