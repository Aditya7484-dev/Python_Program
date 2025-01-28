# In this code we using enumerate keyword 
l=['a','b','c','d','e']

# index=0
# for alpha in l:
#   print(f'At index {index} = {alpha} item stabled.')
#   index+=1

# Now above code is excute without initialize or increase the  index variable--------

for index,alpha in enumerate(l):
  print(f'At index {index} = {alpha} item stabled.')
  