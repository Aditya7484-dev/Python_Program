
from typing import List,Tuple
#----------------------------
## Match-Case
# def arithematicOperation(n1,n2,op):
#   match op:
#     case "add": 
#       return n1+n2
#     case "sub":
#       if(n1>n2):
#         return n1-n2
#       else:
#         return n2-n1
#     case "mul":
#       return n1*n2
#     case "div":
#       if(n1>n2):
#         return n1//n2
#       else:
#         return n2//n1
#     case _:
#       return "Operation Not Found or Matched"

# num1=int(input("Enter a number: "))
# num2=int(input("Enter a number: "))

# print("Select operation: add,sub,mul,div")
# oper=input("Enter the operation: ")
# oper.lower()

# res=arithematicOperation(num1,num2,oper)
# print(f"result of {num1} {oper} {num2} = {res}.")
# ----------------------------------------------------------------------
# n: int=3
# name:str="aditya"
# name.capitalize()
# print(name)
# n:list[int,str]=[1,2,3,4,5,'Aditya']
# print(n)
# ------------------------------------------------------------------
# # It was introduced in python 3.8
# if(n:=len([1,2,3,4,5]))<3:
#   print(f"Length of list is {n}")
# else:
#   print(f"Length of list is greater than 3.")
# --------------------------------------------------------------------
# # Avance Use of dictionary 
# dict1={'key1':1,'key2':9}
# dict2={'key2':8,'key3':7}
# mergedDict=dict1|dict2
# print(mergedDict)
# Advance form of 'with'
# with (
#   open("MyPythonFile.txt","r") as padh,
#   open("Poem.txt","r") as padhFir
#   ):
#   f=padh.read()
#   k=padhFir.read()
  
# print(f)
# print(k)