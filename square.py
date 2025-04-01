import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")  # Set a background color for the window

# Create a turtle object
t = turtle.Turtle()
t.shape("turtle")  # Change the turtle's shape to a turtle
t.color("blue")  # Set the turtle's drawing color
t.speed(2)  # Set the drawing speed (1 is slow, 10 is fast)

# Function to draw a square
def draw_square(side_length):
    for _ in range(4):  # A square has 4 sides
        t.forward(side_length)  # Move the turtle forward by the given side length
        t.left(90)  # Turn the turtle left by 90 degrees

# Draw a square with side length 100
draw_square(100)

# Hide the turtle after drawing
t.hideturtle()

# Keep the window open until clicked
turtle.done()
