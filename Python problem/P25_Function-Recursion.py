# num1=int(input("Enter a number: "))
# num2=int(input("Enter a number: "))
# num3=int(input("Enter a number: "))

# def compare(num1,num2,num3):
#    if(num1>num2 and num1>num3): 
#     return num1
#    elif(num2>num1 and num2>num3): 
#     return num2
#    else: 
#     return num3

# print(f"The greatest number among all is {compare(num1,num2,num3)}")

#------------------------------------------------
# Celsius to fahrenheit

# temp=float(input("Enter temperature in celsius: "))

# def temperature(temp):
#   fahrenheit=round((9/5)*temp+32,2)
#   return fahrenheit

# print(f"{temperature(temp)} degree fahrenheit is in {temp} degree celsius")

# -------------------------------------------------

# num=int(input("Enter a number of terms: "))
# def sum(num):
#   if(num==1):
#     return 1
#   return num+sum(num-1)
# print(f"Sum upto terms {num} is :{sum(num)}")

# -------------------------------------------------

# row=int(input("Enter number of rows: "))

# def patterns(row):
#   if(row==0):
#     return print("Ho gaya apka ab baju wale ko jagah do!!")
#   print("*"*row)
#   patterns(row-1)
    
# patterns(row)

# -------------------------------------------------

# measure=int(input("Enter inches to convert it in cm: "))
# def inchTocenti(measure):
#   return measure*2.54
# print(f"The value of {measure} inches in centimeters is : {inchTocenti(measure)} cm")

# ---------------------------------------------------
# list=['Aditya','sahil','ayush','priyanshu','aman','jigar']
# print(list)
# print("type a name to remove it")
# name=input("Enter a name : ")
# list.remove(name)
# print(list)

# ----------------------------------------------------

num=int(input("Enter a number: "))
def multiable(num):
  for i in range(1,11):
    print(f"{num} X {i} = {num*i}")
multiable(num)