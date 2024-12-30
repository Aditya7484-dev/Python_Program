# # Multiplication Table 
# Linp=int(input("Enter a lower range number: "))
# Hinp=int(input("Enter a higher range number: "))
# while(Linp<=Hinp):
#    i=1
#    while(i<11):
#       print(f"{Linp} X {i} = {Linp*i}")
#       i+=1
#    print("\n")
#    Linp+=1 

# Greet whose name starts with S----------------------------------------

# l={"Aditya","Sahil","Priyanshu","Aman","Salman Bhai"}

# for name in l:
#    name.upper()
#    if(name.startswith("S")):
#       print(f"Hello {name} ") 

#Prime or not Program----------------------------------------------------

# num=int(input("Enter a number: "))
# for i in range(2,num):
#    if num%i==0:
#       print(f"{num} is not prime number.")
#       break
# else:
#    print(f"{num} is a prime number.")

# Sum of n natural numbers------------------------------------------------

# num=int(input("Enter number for sum upto it: "))
# i=1
# sum=0
# while(num>=i):
#    sum+=i
#    i+=1
# print(f"Sum upto {num} is : {sum}")

# Factorial of a number----------------------------------------------------

# num=int(input("Enter anumber to find it's factorial: "))
# fact=1

# for i in range(1,num+1):
#   fact*=i
#   i+=1
# print(f"Factorial of {num} is : {fact}")

# Print Pattern

# print("Whatever you enter is number of rows into which pattern with different stars in column will appears!!!!")
# num=int(input("Enter number of row: "))

# for i in range(1,num+1):
#   print(" "*(num-i),end=" ")
#   print("*"*(2*i-1),end=" ")
#   print(" ")
  
#--------------------------------------------------------------------------------------------------------#

# num=int(input("Enter number of row: "))

# for i in range(1,num+1):
#    if(i==1 or i==num):
#      print("*"*num,end="")
#    else:
#      print("*",end="")
#      print(" "*(num-2),end="")
#      print("*",end="")
#    print("")

# Multiplication Table 
Linp=int(input("Enter a lower range number: "))
Hinp=int(input("Enter a higher range number: "))
while(Linp<=Hinp):
   i=10
   while(i>0):
      print(f"{Linp} X {i} = {Linp*i}")
      i-=1
   print("\n")
   Linp+=1
     
     