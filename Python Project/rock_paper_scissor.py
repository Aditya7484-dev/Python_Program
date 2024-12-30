import random 
#importing random package to choose random number

computerChoice=random.choice([-1,0,1])
#random function will assign a value to computer

playerChoice=int(input("Select a number -1,0 or 1: "))

if(playerChoice == -1 or playerChoice == 1 or playerChoice == 1):

  moves= {-1:'rock',0:'paper',1:'scissor'}
  #Here moves specifies

  print(f"You choose:{moves[playerChoice]}\n computer choose:{moves[computerChoice]}")
  #Now the game begins 



  if(computerChoice==playerChoice):
    print("Game is draw.\nPlay again.")
  else:
    if(computerChoice==-1 and playerChoice==1):
      print("You loose!!Awwwwwwww")
    elif(computerChoice==0 and playerChoice==-1):
      print("You loose!!Awwwwwwww")
    elif(computerChoice==1 and playerChoice==0):
      print("You loose!!Awwwwwwww")
    elif(computerChoice==-1 and playerChoice==0):
      print("You win!!Yehhhhhhh")
    elif(computerChoice==0 and playerChoice==1):
      print("You win!!Yehhhhhhh")
    elif(computerChoice==1 and playerChoice==-1):
      print("You win!!Yehhhhhhh")
    else:
      print("Thankyou to play")
else:
  print("Please Enter A Valid Option.")