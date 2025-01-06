#single inheritance
#Parent class 

# class first:
#   employee="Aman Gupta"
#   language1="Javascript"
  
#   def first(lemcho):
#     print(f"Your employee name is {lemcho.employee} whose work on {lemcho.language1}.")

# #Child class

# class second(first): 
#   language1="Python"
#   def second(lemcho):
#     print(f"language is {lemcho.language1}")
#     print(f"Your employee name is {lemcho.employee}")
    
# a=second()
# a.second()

#Multiple Inheritance-------------------------------------------------------------------
# Parent classes
# class Parent1:
#   name="Aditya Kumar"
#   salary=200000

# class Parent2:
#   company="Microsoft India"
#   post="H.R."

# # Child Class
# class Child1(Parent1,Parent2):
#   def child1(lemcho):
#     print(f"Your company name is {lemcho.company} and Your salary will be {lemcho.salary}.")
# class Child2(Parent1,Parent2):
#   def child2(lemchus):
#     print(f"Your name is {lemchus.name} and Your post in this company will be {lemchus.post}.")

# a = Child1()
# b= Child2()
# b.child2()
# a.child1()

# Multilevel inheritance------------------------------------------------------------------

# class Coder: #This is a parent class of below two classes.
#   a="Python"
# class Programmer(Coder): #This is a child class one
#   b="BCA"
# class Manager(Programmer): #And this is a child class two
#   c="B N College"

# o=Manager()

# print(f"You are a programmer of {o.a} language with degree of {o.b} from {o.c}")

#Super() Method-----------------------------------------------------------------------------

# class Aditya:
#   def __init__(lemcho):
#     print("This is a Parent class.")

# class Aman(Aditya):
#   def __init__(lemcho):
#     super().__init__()
#     print("This is the first child class.")

# class Baman(Aman):
#   a=43
#   def __init__(lemcho):
#     super().__init__()
#     print(f"This is another child class. And it's value is {lemcho.a}")
    
# o=Baman()
# o.a=29

# o.__init__()

# class Aditya:
#   a=74 #class attribute
  
#   @classmethod #This is called decorator which give preference to class declared value to be used instead of instance attribute  
#   def aditya(cls): #Here cls is used because we use the class attribute 
#     print(f"My name is Aditya {cls.a}") 
    
#   @property #This is also a decorator 
#   def course(lemcho):
#     return lemcho.courseName
  
#   @course.setter #This is too
#   def course(lemcho,value):
#     lemcho.courseName=value  
  
# o=Aditya()
# o.a=65 ,"""It's an instance attribute and it has preference more than class attribute until there is no @classmethod comstructor"""

# o.course='BCA'
# print(o.course)
# o.aditya()

class Operator:
  def __init__(lemcho,n):
    lemcho.n = n
  
  # def __add__(lemcho,num):
  #   return lemcho.n + num.n 
  
  def __str__(lemcho):
    return lemcho.n
   
z=Operator('Aditya')
m=Operator(3)
k=Operator(34)
print(z)