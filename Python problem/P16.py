a1=int(input("Enter first number:"))
a2=int(input("Enter second number:"))
a3=int(input("Enter third number:"))
a4=int(input("Enter fourth number:"))

if a1>a2:
  if a1>a3 and a1>a4:
    print(f"{a1} is the greatest number at all.")
  elif a2>a1:
    if a2>a3 and a2>a4:
      print(f"{a2} is the greatest number at all.")
  elif a3>a1:
    if a3>a2 and a3>a4:
      print(f"{a3} is the greatest number at all.")
  elif a4>a1:
    if a4>a2 and a4>a3:
      print(f"{a4} is the greatest number at all.")
else:
  print("All numbers are equal")
 