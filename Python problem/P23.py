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