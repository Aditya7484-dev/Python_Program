# list1=[1,2,3,4,5]
# list2=[2,5,3,8,9]
# list3=[]

# for i in list1:
#   if(i in list2):
#     list3.append(i)
# print(f'Intersection element of {list1} and {list2} lists are {list3}')

# st1=input('Enter a string: ')

# for i in st1:
#   st1.lower()
#   st2=st1[::-1]
#   if st2==st1:
#     print(f' Is {st1} a palindrome? :{True}')
#   else:
#     print(f' Is {st1} a palindrome? :{False}')
#   break

# num=int(input("Enter a number: "))
# def Factorial(num):
#    if num==0:
#      return 1
#    else:
#      fact=num*Factorial(num-1)
#      return fact
# res=f'Factorial of {num} is {Factorial(num)}'
# print(res) 
# --------------------
# li=[1,7,9,12,16]
# print(li[0:3])  
# print(li[0:-1])  
# print(li[0::-1])  
# print(li[-1:-4]) 

# -------------------------------
 
# class Rectangle:
#   def __init__(self,width,height):
#     self.width=width
#     self.heigth=height
    
#   def area(self):
#     return self.width*self.heigth
  
#   def __gt__(self,other):
#     return self.area()>other.area()
  
# rect1=Rectangle(8,5)
# rect2=Rectangle(8,7)

# if rect1 > rect2:
#   print("First rectangle is greater")
# else:
#   print("Second rectangle is greater")

# Armstrong Number---------------------------------------

# num=int(input("Enter a number: "))
# temp=str(num)
# numPower=len(str(abs(num)))
# sum=0
# for i in temp:
#   j=int(i)
#   k=int(numPower)
#   sum+=j**k

# if(num==sum):
#   print(f'{num} is an armstrong number.')
# else:
#   print(f'{num} is not an armstrong number.')

# prime or not------------------------------

# num=int(input('Enter a number: '))

# if(num==1):
#   print('1 is neither a prime nor a composite number.')
# elif(num==2):
#   print('2 is not a prime number.')
# else :
#   for i in range(2,num-1,1):
#     if(num%i==0):
#       print(f'{num} is not a prime number.')
#       break
  
#   else:
#     print(f'{num} is a prime number.')

# Palindrome Number---------

# num=int(input('Enter a number: '))
# temp=str(num)
# k=int(temp[::-1])
# if(num==k):
#   print('Palindrome')
# else:
#   print('Not Palindrome')

# fibonacci Series---------------------------------

# num=int(input('Enter a number: '))
# a=0
# b=1
# for i in range(num):
#   print(a,end="\n") 
#   a,b=b,a+b

# Factorial
# num=int(input("Enter a number: "))
# temp=num
# fact=1
# for i in range(0,num,1):
#   fact*=temp
#   temp=temp-1
# print(f'Factorial of {num} is {fact}')

# Practise a question