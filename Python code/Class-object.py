class first: 
  name="Aditya Kumar"#this is an class atribute
  dept="B.C.A"#this is an class atribute
  rollno=51#this is an class atribute
  
  def greet(self):
    print(f"You are welcome Mr. {self.name}.Your room number is {self.rollno}.")
  
  @staticmethod #Isse self lsgane ka jarurat nhi prta 
  
  def well():#self likhna jauri nhi hai kuch bhi likh skte ho 
    print("Good morning bro kem cho")
    
  def __init__(self,name,rollno,dept):
    self.name=name 
    self.rollno=rollno
    self.dept=dept    
    print("initi ek dunder method hai,kyunki ye bin bulaye call ho jata hai.")

aditya=first("Aditya Kumar",51,"B.C.A") #this is an object atribute
print(aditya.name,aditya.rollno,aditya.dept)
# aditya.dept="BBA"#This is an instance object attribute 
# aditya.language="Python"
# aditya.well()
# aditya.greet()
# first.greet(aditya)
# print(aditya.name,aditya.rollno,aditya.dept,aditya.language)