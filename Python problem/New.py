import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(2)

# Draw a square
for _ in range(12):
  
    # t.forward(100)  # Move forward by 100 units
    # t.left(60)     # Turn 90 degrees to the left 
    # t.right(30)

# Close the window when clicked
screen.exitonclick()
