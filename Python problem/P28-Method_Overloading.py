# # First Problem------------------------------
# class Two_D_Vector:
#   def __init__(lemcho,i,j):
#     lemcho.i=i
#     lemcho.j=j
    
# class Three_D_Vector(Two_D_Vector):
#   def __init__(lemcho,i,j,k):
#     super().__init__(i,j)
#     lemcho.k=k
    
#   def show(lemcho):
#     print(f'The vector are {lemcho.i}i and {lemcho.j}j and {lemcho.k}k.')
    
# a=Three_D_Vector(8,3,6)
# a.show()

# # Second Problem----------------------------
# class Animal:
#   pass
# class Pet(Animal):
#    pass
 
# class Dog(Pet):
#   staticmethod
#   def bark():
#     print("Bow Bow Bow!")
    
# d=Dog
# d.bark()

# # Third Problem--------------------------------

# class Employee:
#   def __init__(lemcho,salary,increment):
#     lemcho.salary=salary
#     lemcho.increment=increment
    
#   @property
#   def salaryAfterIncreament(lemcho):
#     return (lemcho.salary+(lemcho.salary*(lemcho.increment/100)))
  
#   # @salaryAfterIncreament.setter
#   # def IncreseSalary(lemcho,salary):
#   #   lemcho.increment=(salary*lemcho.increment)/100

# salaryInput=int(input("Enter your salary: "))
# increaseInput=int(input("Enter desire increment percentage in salary: "))
# e=Employee(salaryInput,increaseInput)
# print(f'You want {e.salaryAfterIncreament} as salary')

# #Fourth Problem------------------------------------

# class Complex:
#   def __init__(self,r,i):
#     self.a=r
#     self.b=i
    
#   def __add__(self,num):
#     return Complex(self.a+num.a,self.b+num.b)
  
#   def __mul__(self,num):
#     realPart=(self.a*num.a)-(self.b*num.b)
#     imgPart=(self.a*num.b)+(self.b*num.a)
#     return Complex(realPart,imgPart)
  
#   def __str__(self):
#     return f"{self.a}+{self.b}i"

# n1=int(input("Enter a real number: "))
# n2=int(input("Enter a imaginary number: "))
# n3=int(input("Enter a real number: "))
# n4=int(input("Enter a imaginary number: "))

# c1=Complex(n1,n2)
# c2=Complex(n3,n4)

# print(f"Sum of given real and imaginary numbers is :{c1+c2}")
# print(f"Product of given real and imaginary numbers is :{c1*c2}")

# #Fifth Problem----------------------------
class vector:
  def __init__(self,x,y,z):
    self.a=x
    self.b=y
    self.c=z
  
  def __add__(self,v2):
    return vector((self.a + v2.a),(self.b + v2.b),(self.c + v2.c))
  
  def __mul__(self,v2):
    return (self.a*v2.a + self.b*v2.b + self.c*v2.c)
  
  def __str__(self):
    return f'{self.a}i+{self.b}j+{self.c}k'

n1=int(input("Enter value of i cap for first vector  : "))
n2=int(input("Enter value of j cap for first vector  : "))
n3=int(input("Enter value of k cap for first vector  : "))
n4=int(input("Enter value of i cap for another vector: "))
n5=int(input("Enter value of j cap for another vector: "))
n6=int(input("Enter value of k cap for another vector: "))
print(" ")

v1=vector(n1,n2,n3)
v2=vector(n4,n5,n6)

print(f"Sum of first and second vector is:{v1+v2}")
print(f"Product of first and second vector is:{v1*v2}")