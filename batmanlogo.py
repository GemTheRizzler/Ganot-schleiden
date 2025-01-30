#Drawing the Batman Logo
import turtle  # Import the turtle graphics module

# Create a turtle object to draw
t = turtle.Turtle()

# Set the background color to black
turtle.bgcolor("black")

# Lift the pen to move the turtle without drawing
t.penup()

# Move the turtle to a starting position (0, -100)
t.goto(0, -100)

# Lower the pen to start drawing
t.pendown()

# Set the shape of the turtle to "circle" and the fill color to yellow
turtle.shape("circle")
turtle.fillcolor("yellow")

# Scale the turtle's shape to make it large
turtle.shapesize(20, 40)

# Move the turtle to position (0, 80)
t.goto(0, 80)

# Start filling in the shape with black color
t.begin_fill()
t.fillcolor("black")

# Draw the pattern using the turtle
# The following commands control the turtle's movement and direction
t.forward(10)
t.left(60)
t.forward(30)
t.right(140)
t.forward(45)
t.left(100)
t.forward(100)
t.left(60)
t.forward(40)
t.right(90)

# Draw a curved shape by moving forward and turning in small increments
for i in range(70):  
    t.forward(4.5)
    t.right(1)

# Draw part of a circle (arc)
t.right(170)
t.circle(90, 135)
t.right(90)
t.circle(135, 90)

# Continue drawing another arc and curved path
t.right(130)
t.circle(135, 90)
t.right(90)
t.circle(90, 135)
t.right(171.5)

# Draw another curved path
for i in range(70):  
    t.forward(4.5)
    t.right(1)

# Move and draw more shapes to complete the pattern
t.right(90)
t.forward(40)
t.left(65)
t.forward(100)
t.left(80)
t.forward(45)
t.right(140)
t.forward(25)
t.left(80)
t.forward(10)

# End the filling of the shape
t.end_fill()

# Hide the turtle once the drawing is complete
t.hideturtle()

# Finish the drawing and keep the window open
turtle.done()