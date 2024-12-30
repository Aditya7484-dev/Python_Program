a = (23,"red","frog","tiger",34, False,True,23,"frog","tiger","tiger")

print(type(a))

print(a[3])

print("Repetation of tiger and '23' in tuple is",a.count("tiger"),"and",a.count(23),"repectively")

print(a.index(False))

print("Pankhuri" in a)

print("tiger" in a)  

print(len(a))

print(a*2),"""This will repeate the tuple as specified."""

# print(min(a)),""" This will use with similar type of data """

# print(max(a)),""" This will use with similar type of data """

adi=(1,2,3,4,5)

a,b,c,d,e = adi,"""We cannot use 1,2,3 .. to assign tuple correspondingly"""

print(a,b,c,b,e)