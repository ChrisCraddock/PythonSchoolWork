

'''
This program will do the following:
1. Ask for input of the number of squares to draw
2. Use a nested loop to draw requested number of squares
'''

import turtle

#===Constants
num_squares = 1
t = turtle.Turtle()
t.pendown()
side = side_unit = 30
#===Input
while True:
    try:
        num_squares = int(input('input the number of squares: '))
    except ValueError:
        print("please enter an integer")
    if num_squares > 1:
        break
#===Process
for sq in range(1, num_squares + 1):
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
    side = side_unit + 3 * sq  # increase the size of the side

    t.goto(0,0)                # return to base

turtle.done()
