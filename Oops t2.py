#Get index in the list of objects by attribute in Python
  
class X:
    def __init__(self,val):
        self.val = val
        
def getIndex(li,target):
    for index, x in enumerate(li):
        if x.val == target:
            return index
    return -1
  
# Driver code
li = [1,2,3,4,5,6]
  
# Converting all the items in list to object of class X
a = list()
for i in li:
    a.append(X(i))
      
#print(getIndex(a,8))



#build flashcard using class in Python

class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        
        #we will return a string 
        return self.word+' ( '+self.meaning+' )'
        
flash = []
#print("welcome to flashcard application")
  
#the following loop will be repeated until user stops to add the flashcards
#while(True):
    #word = input("enter the name you want to add to flashcard : ")
    #meaning = input("enter the meaning of the word : ")
      
    #flash.append(flashcard(word, meaning))
    #option = int(input("enter 0 , if you want to add another flashcard : "))
      
#    if(option):
#ye        break
          
# printing all the flashcards 
#print("\nYour flashcards")
#for i in flash:
#    print(">", i)




#flashcards 2

import random
  
class flashcard:
    def __init__(self):
        
        self.fruits={'apple':'red',
                     'orange':'orange',
                     'watermelon':'green',
                     'banana':'yellow'}
          
    def quiz(self):
        while (True):
            
            fruit, color = random.choice(list(self.fruits.items()))
              
            print("What is the color of {}".format(fruit))
            user_answer = input()
              
            if(user_answer.lower() == color):
                print("Correct answer")
            else:
                print("Wrong answer")
                  
            option = int(input("enter 0 , if you want to play again : "))
            if (option):
                break
  
print("welcome to fruit quiz ")
fc=flashcard()
fc.quiz()