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

# Second Problem----------------------------

class Animals:
  def __init__(lemcho,a): 
    lemcho.a=a
    
class Pet(Animals):
  def __init__(lemcho):
    super().__init__()
    

class Dog(Pet):
  def bark(lemcho):
    print('But the dog barks')

b=Dog()
b.bark()