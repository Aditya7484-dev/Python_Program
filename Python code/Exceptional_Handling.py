# try:
#   a=int(input("Enter a number: "))
#   print(a)
# except Exception as e:
#   print(f'{e} This is the exception')

# print("This statement run which can be possible in exception handling.")

# # Another type of try and except method------------------------
# try:
#   n=int(input("Enter a value: "))
#   print(n)
  
# except ValueError as Ve:
#   print(f"'{Ve}' This the error when operation is wrong")
  
# except ZeroDivisionError as Z:
#   print(f"'{Z}' This is the exception")
  
# print("Thank You")

# # Keyword 'raise' is using-----------------
# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))

# if(b==0):
#   raise ZeroDivisionError("Don't divide any number with 0 as it is not computable")
# else:
#   print(f"Division of first number by second number is : {a/b}")

# # try except with else keyword----------------
# try:
#   a=int(input("Enter a number: "))
#   print(a)
# except Exception as e:
#   print(f'{e} This is the exception')
# else:#this block of code will run after the successful excution of above code
#   print("This code is run successfully and no exception found")
