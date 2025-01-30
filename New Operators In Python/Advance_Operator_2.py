from functools import reduce
# # Function can be written in this way with the help of lambda keyword-------

# square =lambda z:z*z #In this code we also use lambda keyword to define a function

# n=int(input("Enter the number:"))

# print(square(n))

# # Using join keyword------
# l=['Aditya','Kumar','Rajeev','Kumar']
# print("+".join(l))

# # Using formate keyword-------
# a="{} is a good {}".format("Aditya","boy")
# print(a)

# # Using map keyword---------
l2=[1,2,3,4,5,6,7,8,9,10]

# square=lambda z:z**3
# s=list(map(square,l2))
# print(s)

# # Using filter keyword ---------------
# def odd(n):
#   if n%2!=0:
#     return True
#   return False

# a=filter(odd,l2)
# print(f'This is the list of odd numbers:{list(a)}')

# Using reduce keyword -----------
def sum(a,b):
  return a+b
def mul(a,b):
  return a*b
a=reduce(sum,l2)

b=reduce(mul,l2)

print(f'Adition: {a} and Multiplication: {b}')