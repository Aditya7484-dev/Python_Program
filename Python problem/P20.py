list=["Aditya","Priyanshu","Aman","Reshma","Sonal","Karishma","Vivek","Pratyush"]
name=input("Enter a name: ")

if(name in list):
  print(f"Yes this name {name} is in the list.")
else:
  print(f"No this name {name} is not in the list.")