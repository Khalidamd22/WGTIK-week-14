import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(10)

# Create the petals of the flower
for i in range(360):
    t.forward(100)
    t.right(30)
    t.forward(20)
    t.left(60)
    t.forward(50)
    t.left(30)
    t.penup()
    t.setposition(0, 0)
    t.pendown()
    t.right(1)

# Create the center of the flower
t.color("orange")
t.begin_fill()
t.circle(20)
t.end_fill()

# Hide the turtle
t.hideturtle()

# Keep the window open until it's closed
turtle.mainloop()