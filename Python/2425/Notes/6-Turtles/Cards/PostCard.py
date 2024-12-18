##PostCard
#import turtle 
#import math
#
#turt = turtle.Turtle()
#wn = turtle.Screen()
#
#def createShape(sides,length,reg=0,dir=1,color="black",startposition=[0,0]):
#    x,y = startposition
#    turt.teleport(x,y)
#    turt.color(color)
#    angle = 360/sides
#    if reg == 0:
#        for i in range(sides):
#            turt.fd(length)
#            if dir == 1:
#                turt.right(angle)
#            else:
#                turt.left(angle)
#    else:
#        for i in range(math.floor(sides/2)):
#            turt.fd(length)
#            if dir == 1:
#                turt.right(angle)
#            else:
#                turt.left(angle)
#            turt.fd(length/2)
#            if dir == 1:
#                turt.right(angle)
#            else:
#                turt.left(angle)
#
#createShape(4,50,dir=1,reg=1)
#
#wn.mainloop()


import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor(0,.5,.75)

# Create the turtle object for drawing
pen = turtle.Turtle()
pen.speed(10)

# Function to draw a circle
def drawCircle(radius, color, x, y, steps=None):
    pen.teleport(x,y)
    pen.begin_fill()
    pen.color(color)
    pen.circle(radius,None,steps)
    pen.end_fill()

# Function to draw the Christmas tree
def drawTree():
    # Draw the three tiers of the 
    #start = -100,-100
    #+20,+60
    #+20,+80
    pen.teleport(-100, -100)
    pen.begin_fill()
    pen.color("green")
    pen.setheading(60)
    for i in range(3):
        pen.forward(200)
        pen.right(120)
    pen.end_fill()

    # Draw second tier
    pen.teleport(-80, -40)
    pen.begin_fill()
    pen.setheading(60)
    for i in range(3):
        pen.forward(160)
        pen.right(120)
    pen.end_fill()

    # Draw third tier
    pen.teleport(-60, 40)
    pen.begin_fill()
    pen.setheading(60)
    for i in range(3):
        pen.forward(120)
        pen.right(120)
    pen.end_fill()

# Function to draw the star
def drawStar(x, y, size):
    pen.teleport(x,y)
    pen.begin_fill()
    pen.color("yellow")
    for i in range(5):
        pen.forward(size)
        pen.right(144)
    pen.end_fill()

# Function to draw the snowman
def drawSnowman(x, y):
    #body
    drawCircle(30,"white",x,y)
    drawCircle(25,"white",x,y+45)
    drawCircle(20,"white",x,y+75)
    #eyes
    drawCircle(3,"black",x-10,y+85)
    drawCircle(3,"black",x+10,y+85)
    #nose
    drawCircle(5,"orange",x,y+75,steps=3)

# Function to draw a wrapped present
def drawPresent(x, y):
    pen.setheading(0)
    pen.teleport(x,y)
    pen.begin_fill()
    pen.color("red")
    for i in range(4):
        pen.forward(40)
        pen.left(90)
    pen.end_fill()
    pen.width(5)
    pen.setheading(0)
    pen.teleport(x,y+20)
    pen.color("yellow")
    pen.fd(40)
    pen.setheading(90)
    pen.teleport(x+20,y)
    pen.color("yellow")
    pen.fd(40)
    pen.width(0)

drawTree()
drawStar(0, 130, 30)
drawSnowman(-150, -100)
drawPresent(100, -180)

for i in range(50):
        x = random.randint(-300, 300)
        y = random.randint(100, 300)
        drawCircle(3, "white", x, y)

# Hide the turtle
pen.hideturtle()

screen.mainloop()
