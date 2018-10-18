


'''
Design 2 shapes of my choice using a turtle
'''
# Import turtle
import turtle

# Begin drawing a circle
turtle.hideturtle()     # Hide the turtle from view
turtle.begin_fill()     # Fill the shape solid black
turtle.circle(100)      # Draw a circle with a radius of 100
turtle.end_fill()       # End the shape fill

# Begin drawing a square
turtle.penup()          # Pick up the pen to avoid extra lines
turtle.begin_fill()     # Fill the shape solid black
turtle.right(90)        # Turn the turtle 90 degrees
turtle.forward(100)     # Move the turtle forward 100
turtle.pendown()        # Put the pen down to begin drawing
turtle.right(90)        # Turn the turtle 90 degrees
turtle.forward(100)     # Move the turtle forward 100
turtle.left(90)         # Turn the turtle 90 degrees
turtle.forward(100)     # Move the turtle forward 100
turtle.left(90)         # Turn the turtle 90 degrees
turtle.forward(100)     # Move the turtle forward 100
turtle.left(90)         # Turn the turtle 90 degrees
turtle.forward(100)     # Move the turtle forward 100
turtle.left(90)         # Turn the turtle 90 degrees
turtle.end_fill()       # End the shape fill

turtle.done()           # Keep the window from closing upon completion
