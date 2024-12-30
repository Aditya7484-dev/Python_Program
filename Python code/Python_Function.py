# def Greet(name):
#   print(f"Good Morning {name} !!!!!!")

# times=int(input("How many times you want to greet someone= "))
# for i in range(1,times+1):
#   name=input("Enter a name: ")
#   Greet(name)
#   print("thankyou")

# Function with returning value

name=input("Enter a name: ")
def jam(name):
  print(f"Hi {name} kem cho sb sahi hai na!!")
  return "The code is run smoothly."
a=jam(name)
print(a)