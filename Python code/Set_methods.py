s={1,3,5,7,"Aditya",2}
print("Length of given set is :",len(s))

d={53,4,2,5,"Aditya"}
print(s.union(d))
print("Common element of the set",s,"and",d,"is",s.intersection(d))

s.remove("Aditya")
print(s)

print(s.pop(),s)

