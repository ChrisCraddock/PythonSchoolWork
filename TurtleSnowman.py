
import turtle

# drawBase = draw the base of the snowman, the largest snowball at the bottom
# drawMidSection = draw the middle snowball
# drawArms = draw snowman arms
# drawHead = draw snowman head, with eyes/mouth/ect
# drawHat = draw snowman hat

# Make it faster than typing out "Tutrle"
t = turtle

# X and Y coords for circles
MID_X = 0
MID_Y = 25
HEAD_X = 0
HEAD_Y = 100
HAT_X = 10
HAT_Y = 190


def main():
    drawBase()
    drawMidSection()
    drawHead()
    drawArms()
    drawHat()


def drawBase():
    t.penup()
    t.setx(0.0)
    t.sety(-250)
    t.pendown()
    t.circle(100)


def drawMidSection():
    t.penup()
    t.setx(0.0)
    t.sety(-50)
    t.pendown()
    t.circle(75)


def drawHead():
    t.penup()
    t.setx(0.0)
    t.sety(100)
    t.pendown()
    t.circle(50)
    t.penup()
    t.setx(-30)
    t.sety(125)
    t.pendown()
    t.forward(60)
    t.penup()
    t.goto(HEAD_X, HEAD_Y)
    t.setx(-30)
    t.sety(150)
    t.pendown()
    t.circle(5)
    t.penup()
    t.forward(60)
    t.pendown()
    t.circle(5)
    t.penup()


def drawArms():
    t.penup()
    t.setx(MID_X)
    t.sety(MID_Y)
    t.forward(75)
    t.pendown()
    t.left(30)
    t.forward(50)
    t.left(20)
    t.forward(20)
    t.back(20)
    t.right(40)
    t.forward(20)
    t.penup()
    t.goto(MID_X, MID_Y)
    t.left(170)
    t.forward(75)
    t.pendown()
    t.right(30)
    t.forward(50)
    t.right(20)
    t.forward(20)
    t.back(20)
    t.left(40)
    t.forward(20)
    t.penup()


def drawHat():
    t.goto(HAT_X, HAT_Y)
    t.back(40)
    t.setheading(180)
    t.pendown()
    t.begin_fill()
    t.forward(100)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(61)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.end_fill()

main()
turtle.done()
