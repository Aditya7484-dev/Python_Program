#For problem 2
import random
 
# First problem-----------------------------------------------------------------------------

# f=open("Poem.txt")
# f.read()
# f.close()
# with open("Poem.txt","r") as padh:
#   f=padh.read()
#   if("twinkle" in f):
#     print(f"twinkle word is present in:\n\n{f}")
#   else:
#     print(f"twinkle word is not present in:\n\n{f}")

# Second problem-----------------------------------------------------------------------------

# def Game():
  
#     score=0
#     computer=random.choice([1,0])
#     gameChoice={1:'Heads',0:'Tails'}
#     playerChoice=int(input("Enter your choice(1 or 0): "))
    
#     print(f"You choose {gameChoice[playerChoice]} and computer choose {gameChoice[computer]}")
    
#     if(computer==playerChoice):
#       score=random.randint(1,1000)
#       #print(f"You choose {gameChoice[playerChoice]} and computer choose {gameChoice[computer]}.\nAnd You win.Congratulation.")
#     else:
#       score
#       # print(f"You choose {gameChoice[playerChoice]} and computer choose {gameChoice[computer]}.\nAnd You loose.Awwwwwwwww.")
    
#     with open("Score.txt","r") as likh:
#       f=likh.read()
#       if(f!=""):
#         f=int(f)
#       else:
#         f=0
        
#     print(f"Your score is: {score}")
    
#     if(score>f):
#       with open("Score.txt","w") as likh:
#         likh.write(str(score)) 
#     return score

# choose=input("Write Enter to start the Game or else write no: ")

# if(choose.lower()=="enter" or choose.upper()=="Enter"):
#   Game()
# elif(choose.lower()!="enter" or choose.upper()!="Enter"):
#    print("No problem play whenever you want.\nTHANKYOU")  

# Third problem----------------------------------------------------------------------------------

# And this function will creating txt files within TableFile

# def Gentable(n):
#   table = ""
#   for i in range(1,11):
#     table+=f"{n} X {i} = {n*i}\n"
  
#   with open(f"TablesFile/table-Of-{n}.txt","w") as Table:
#     Table.write(table)

# #this loop will take a parameter for the function

# for i in range(2,21):
#   Gentable(i)
 
# Fourth-Fifth Problem------------------------------------------------------------------------------------

# content="Hey piggy boy don't fuck up with me else You'll be find yourself murdered.Bullshit man"
# with open("File1.txt","w") as f:
#   c=f.write(content)
  
# list=["fuck","piggy","murdered","Bullshit"]

# for item in list:
#   content=content.replace(item,"#"*len(item))

# with open("File1.txt","w") as f:
#     f.write(content)

# Sixth problem--------------------------------------------------------------------------------------------

# st="My name is Aditya Kumar. And I'm doing my Bachelor's from Bihar National College ,Patan. Right Now I'm writing a code in Python language.Thankyou."

# with open("Python.txt","w") as likh:
#   likh.write(st)
  
# with open("Python.txt","r") as likh:
#   content=likh.read()

# if("Python" in content):
#   print("Yes")
# else:
#   print("No")

# Seventh problem---------------------------------------------------------------------------------------------

# with open("Python1.txt") as f:
#   lines=f.readlines()
  
#   lineno=1
  
#   for line in lines:
#     if "Python" in line:
#       print(f"Yes Python is in line number : {lineno}")
#       break
#     lineno+=1
  
#   else:
#     print("No Python is not present in the given paragraph.")

# Eighth Problem---------------------------------------------------------------------------------------------

# with open("this.txt") as f:
#   content=f.read()

# with open("this_copy.txt","w") as f:
#   f.write(content)

# Nineth Problem----------------------------------------------------------------------------------------------

# st="Aditya is poor as dull in life"

# with open("this.txt","w") as f:
#   content1=f.write(st)

# with open("this_copy.txt","w") as f:
#   content2=f.write(st)

# if(content1==content2):
#   print("Yes content of both the txt files are matched")
# else:
#   print("No contents matches of the given two files.")

# Tenth problem------------------------------------------------------------------------------------------------

# with open("this_copy.txt","w") as f:
#   f.write("") #if you want to wipe out the content of a file do "" in the write() only.

# Eleventh problem-----------------------------------------------------------------------------------------
# This can be done with a module which I still not studied