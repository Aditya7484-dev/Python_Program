# How to create and write in a file from python

# firstfile="""It's my first file from python.\nAur sb thik hai.\nkya aaj kl chal rha hai.\nsb toh thik hi hoga na.\n"""
# f=open("MyPythonFile.txt","w")
# f.write(firstfile)
# f.close()

# How to read a file line by line 

# f=open("MyPythonFile.txt")
# Readfile=f.readlines()
# print(Readfile)
# f.close()

# Reading a file through a loop

# f=open("MyPythonFile.txt")
# line=f.readline()
# while(line!=""):
#   print(line)
#   line=f.readline()
# f.close()

# How to append a file

# st="""Is line ko append krna hai."""
# f=open("MyPythonFile.txt","a")
# f.write(st)
# f.close

# # Check that the file append or not using with

# with open("MyPythonFile.txt","r") as padh:
#   f=padh.read()
# print(f)
  
# with facilitates that we don't need to close the file , it will automatically
