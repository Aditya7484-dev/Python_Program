from functools import reduce
# Problem number 2-------------------
# name=input("Enter the name: ")
# marks=int(input("Enter your marks: "))
# number=int(input("Enter your number: "))
# s="The name of the student is {0},his marks are {1} and phone number is {2}".format(name,marks,number)
# print(s)

# # Problem number 3------------------
# lst=[7*i for i in range(1,11)]
# for item in lst:
#   print(str(item),end="\n")

# # Problem 4-----------------
# lst=[i for i in range(1,100,1)]
# def check(n):
#   if n%5==0:
#     return True
#   return False
# s=list(filter(check,lst))
# print(s,end="\n")

# Problem number 5---------------
lst=[i for i in range(1,101,1)]
def checking(n,m):
  if n>m:
    return n 
  return m
s=reduce(checking,lst)
print(s)