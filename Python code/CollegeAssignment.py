# # WAP to reverse a number a number.--------------

# n1=int(input("Enter a number: "))
# temp=str(n1)
# print(temp[::-1]) 

# #WAP to check a number is palindrome----------

# n2=int(input("Enter a number : "))
# temp1=str(n2)
# rev=int(temp1[::-1])
# if(n2==rev):
#   print(f"{n2} is a palindrome number ,i.e, it is same even reversed")
# else:
#   print(f"{n2} is not a palindrome number ")

# #Check armstrong number or not----------------------------

# n3=int(input("Enter a number : "))
# pow=len(str(abs(n3)))
# temp3=str(n3)
# sum=0
# for i in temp3:
#   lenum=int(i)
#   sum+=lenum**pow
# else:
#   if(n3==sum):print(f'{n3} is armstrong number')
#   else:print(f'{n3} is not armstrong number')

# #count lowercase,uppercase and digits-------------------------------

# user=input("Write anything: ")

# countLower=0
# countUpper=0
# countDigit=0

# for chara in user:
#   if(chara is str):
#     if(chara.islower()):
#       countLower+=1
#     elif(chara.isupper()):
#       countUpper+=1
#   elif(chara.isdigit()):
#     countDigit+=1

# print(f"Number of lowercase is {countLower}, uppercase is {countUpper} and digits is {countDigit}")

# #finding substring in mainstring-------------------------------

# mainString=input("Write main string: ")
# subString=input("Write sub-string string: ")

# if(subString in mainString):
#   print(f"Yes {subString} is sub-string of {mainString}")
# else:
#   print(f"No {subString} is sub-string of {mainString}")

#Fibonacci series-------------------------------------------

# tr=int(input("Enter number of term: "))

# if(tr<=0):
#   print("Enter a positive number and non-zero number of term.")
# else:
#   a,b=0,1
#   for i in range(0,tr,1):
#     print(a, end=" ")
#     a,b=b,a+b
#     print()-45

#prime or not--------------------------------------
# num=int(input("Enter a number: "))

# if(num==1):
#   print("1 is neither prime nor a composite number.")
  
# elif(num==2):
#   print(f"You give {num} which is a prime number.")
  
# else:
#   for i in range(2,num-1,1):
#     if(num%i!=0):
#       continue
#     elif(num%i==0):
#       print(f"You give {num} which is not a prime number.")
#       break
    
#   else:
#     print(f"You give {num} which is a prime number.")
# row=int(input("Enter number of rows: "))
# for i in range(1,row+1):
#   for j in range(1,i+1):
#     print(j,end=" ")
#   print()
# num=int(input("Enter a number: "))

# if(num%2==0):
#   print("Even")
# else:
#   print("Not even") 
# ------------------------------
# def Rectangle(lenth,width):
#   area=lenth*width
#   return area

# num1=Rectangle(14,12)
# num2=Rectangle(13,8)

# if(num1>num2):
#   print("Area of first rectangle is greater")
# else:
#   print("Area of second rectangle is greater")