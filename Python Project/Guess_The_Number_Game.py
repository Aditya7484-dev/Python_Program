import random 

m_G=random.randint(1,100)
guess=0
p_G=0

while p_G!=m_G:
  
  guess+=1
  p_G=int(input("Make a guess between 1 to 100: "))
  
  if(m_G>p_G):
    print("Make a higher guess.") 
  elif p_G>m_G:
    print("Make a lower guess.")

print(f"You have guessed the right number {m_G} in {guess} attempt.")  