import random

char="abcdefghijklmnopqrstuvwxyz!@#$%^&*1234567890()\{}[]"

length=int(input("Enter the length of password: "))
password=""

for i in range(length):
  password+=random.choice(char)

print(password)