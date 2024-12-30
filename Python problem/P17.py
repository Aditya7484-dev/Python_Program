print("40% total and 30% in each subject to pass")

sub1= int(input("Enter marks in 1st subject: "))
sub2= int(input("Enter marks in 2nd subject: "))
sub3= int(input("Enter marks in 3rd subject: "))
STotal= ((sub1+sub2+sub3)/300)*100

if STotal >= 40 and sub1>=33 and sub2>=33 and sub3>=33:
  # if :
    print("You are promoted to next standard. Well done.")
  # else:
  #   print("Not promoted.Keep focus on studies.")
else:
  print("I'm sorry.You failed this time.")
