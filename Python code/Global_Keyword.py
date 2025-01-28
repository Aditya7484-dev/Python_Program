a=23
def GlobalFunc():
  global a
  a=34
  print(f'This is global keyword with modification {a}')

print(f'This is global keyword without modification {a}')

GlobalFunc()