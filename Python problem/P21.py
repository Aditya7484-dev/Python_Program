print("Check your grades.")
marks=float(input("Enter your marks: "))

if 100>=marks>90:
  print("your grade is 'Ex.' ")
elif 90>=marks>80:
  print("Your gradde is 'A'  ")
elif 80>=marks>70:
  print("Your gradde is 'B'  ")
elif 70>=marks>60:
  print("Your gradde is 'C'  ")
elif 60>=marks>50:
  print("Your gradde is 'D'  ")
elif 50>=marks:
  print("Your gradde is 'F' ")
else:
  print("Your number is invalid")