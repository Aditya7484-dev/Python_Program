import random
from random import randint  
# Question number 1--------------------------------------
# class Programmer:
#   Company="Microsoft"
#   name="Aditya Kumar"
#   language="Python"
#   Salary=1300000
#   HODname="Kem William Willson"
  
#   def Microsoft(lemcho):
#     print(lemcho.name,lemcho.Salary,lemcho.language)
        
#   def __init__(lemcho,name,language,Company,Salary):
#     lemcho.Company=Company
#     lemcho.name=name
#     lemcho.Salary=Salary
#     lemcho.language=language
      

# aditya=Programmer("Aditya Kumar","python","Microft",200000000)
# print(aditya.Company,aditya.name,aditya.Salary,aditya.language)
# aditya.Microsoft()

#  Question number 2--------------------------------------------------------

# class Calculator:
#   def __init__(lemcho,square,cube,squareroot):
#     lemcho.square= (square*square)
#     lemcho.cube= (cube**3)
#     lemcho.squareroot= (squareroot**0.5)
    
# S=int(input("Enter number for it's Square: "))
# C=int(input("Enter number for it's cube: "))
# Sr=int(input("Enter number for it's Squareroot: "))

# maths=Calculator(S,C,Sr)
# print(f"Square of {S} is : {maths.square}")
# print(f"Cube  of {C} is : {maths.cube}")
# print(f"Squareroot of {Sr} is : {maths.squareroot}")

#  Question number 3---------------------------------------------------------

# class attribute:
#   a=4

# o=attribute()
# print(o.a) #This will print 4 'cause instance attribute is not present 
# o.a=7 #it's a instance attribute
# print(o.a) #This will print 7 'cause instance attribute is present now 
# print(attribute.a) #This will print 4 again 'cause the class attribute is called 
#conclusion is that the class attribute is not changed only  value changes due to instance attribute's value

# Question number 4------------------------------------------------------------

# class Calculator:
#   def __init__(lemcho,square,cube,squareroot):
#     lemcho.square= (square*square)
#     lemcho.cube= (cube*cube*cube)
#     lemcho.squareroot= (squareroot**0.5)
  
#   @staticmethod
#   def greet():
#     print("Good Morninng")  
# S=int(input("Enter number for it's Square: "))
# C=int(input("Enter number for it's cube: "))
# Sr=int(input("Enter number for it's Squareroot: "))

# maths=Calculator(S,C,Sr)
# maths.greet()
# print(f"Square of {S} is : {maths.square}")
# print(f"Cube  of {C} is : {maths.cube}")
# print(f"Squareroot of {Sr} is : {maths.squareroot}")

#  Question number 5--------------------------------------------------------------

class Train:
  
  def __init__(lemcho,trainName,trainNo):
    lemcho.trainName=trainName
    lemcho.trainNo=trainNo
        
  def bookticket(lemcho,From,To):
    print(" ")
    print(f"Your ticket is booked in train number: {lemcho.trainNo},from {From} to {To}.")
  
  def getstatus(lemcho,status):
    print(f"Your tain {lemcho.trainName} is arriving on {status}")
  
  def fairtax(lemcho,From,To):
    print(f"Your ticket of {lemcho.trainName} costs You : {random.randint(100,1000)} from {From} to {To}.")
  
  def coach(lemcho):
    print(f"Your seat has been alloted in the {random.choices(["Ac","Sleeper","General"])} coach.")

Tn1=input("Enter your train name: ")
Tn2=int(input("Enter your train number: "))
Tbt1=input("Enter your station: ")
Tbt2=input("Enter your destination: ")

t=Train(Tn1,Tn2)
t.bookticket(Tbt1,Tbt2)
t.fairtax(Tbt1,Tbt2)
t.coach() 
t.getstatus(random.choice(["Bandarpur Jn","Chamgadarpur Jn","Karela Singh jn"])) 