# HIT THE TARGET GAME
import turtle

# NAMED CONSTANTS
SCREEN_WIDTH = 600  # screen width
SCREEN_HEIGHT = 600  # screen height
TARGET_LLEFT_X = 100  # TARGETS LOWER LEFT X
TARGET_LLEFT_Y = 200  # TARGETS LOWER LEFT Y
TARGET_WIDTH = 25  # TARGETS WIDTH
FORCE_FACTOR = 30  # ARBITRARY FORCE FACTOR
PROJECTILE_SPEED = 1  # ANIMATION SPEED
NORTH = 90  # ANGLE OF NORTH DIRECTION
SOUTH = 270 # ANGLE OF SOUTH DIRECTION
EAST = 0    # ANGLE OF EAST DIRECTION
WEST = 180  # ANGLE OF WEST DIRECTION

#SET UP WINDOW
turtle.setup(SCREEN_WIDTH,SCREEN_HEIGHT)

#DRAW TARGET
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X,TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

#Center turtle
turtle.goto(0,0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# Get the angle and force from the user
angle = float(input('Enter the projectile\'s\' angle: '))
force=float(input('Enter the launch force (1-10): '))

# Calculate the distance
distance = force * FORCE_FACTOR

# Set the turtle heading
turtle.setheading(angle)

# Launch the projectile
turtle.pendown
turtle.forward(distance)

# Did you hit the target
if (turtle.xcor() >= TARGET_LLEFT_X and
    turtle.xcor() <=(TARGET_LLEFT_X + TARGET_WIDTH) and
    turtle.ycor() >= TARGET_LLEFT_Y and
    turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
        print('Target Hit')
else:
    print('You missed the target')

