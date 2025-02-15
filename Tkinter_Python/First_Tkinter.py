from tkinter import *
# /creating a window this is important 
root=Tk()
# Here I create my label to show 
mylable1=Label(root,text="Hey my name is Aman")
mylable2=Label(root,text="Hey my name is Karan")

# # Here I pack my label
# mylable.pack()


def clickFunc():
  mylabel=Label(root,text='Button clicked Now!!')
  mylabel.grid(row=4,column=0)

# Creating a button
myButton=Button(root,text="Click me baby",state='normal',padx=50,pady=5,bg='grey',fg='Red',command=clickFunc)
myButton.grid(row=1,column=0)

# This is a grid function that used to arrange the text in the label
mylable1.grid(row=3,column=0)
mylable2.grid(row=2,column=0)


# This is the loop that must be inserted 
root.mainloop()
