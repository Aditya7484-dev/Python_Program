# Problem Number 1-----------------------------
# try:
#   with(
#     open("1.txt","r") as f1,
    
#     open("2.txt","r") as f2,
    
#     open("3.txt","r") as f3
#   ):
#     j=f3.read()
#     p=f1.read()
#     k=f2.read()
# except Exception as e:
#   print(e)

# xxxxxxxxxxx Shotcut code xxxxxxxxxxxxxxxxxxxxxxxxxx

# l=['1.txt','2.txt','3.txt']
# for index,file in enumerate(l):
#   try:
#     with open(file,"r") as i:
#       k=i.read()
#   except Exception as e:
#     print(f"The file in the list with index {index} is open with an exception as {e}")

# print("Thankyou")

# # Problem Number 2------------------------
# l=[1,2,3,4,5,6,7,8,9]
# for index,item in enumerate(l):
#   if(index==2 or index==4 or index==6):
#     print(f"{item} is the {index+1}th element")

# else:
#     print("Thank You")

# # Problem Number 3 and 5-------------------------
num=int(input("Enter a number: "))
TableList=[num*i for i in range(1,11,1)]
print(TableList) #5 Starts

with open("Table.txt","a") as Pahara:
  Pahara.write(str(TableList)+"\n")

# # Problem Number 4------------------
# try:
#   print(5/0)
# except Exception as e:
#   print("Infinite by handling the 'ZeroDivisionError' ")
