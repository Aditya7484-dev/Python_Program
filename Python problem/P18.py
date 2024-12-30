# print("Track spam from your comment")
# p1="Make a lot of money"
# p2="subcribe this"
# p3="buy now"
# p4="click this"

# comment=input("Write a comment:")

# if((p1 in comment)or(p2 in comment)or(p3 in comment)or(p4 in comment)):
#   print("Don't spam with me your son of jerk.")
# else:
#   print("ok")
l1=['make a lot of money','subscribe this','buy now','click this']
comment=input("Write a comment : ")
for i in l1:
  if i in comment.lower():
    print(f"The comment '''{comment}''' is a spam")
    break

else:
  print(f"The comment '''{comment}''' is not a spam")
