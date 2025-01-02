import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor(0,.5,.75)
#Pen setup
pen = turtle.Turtle()
pen.speed(0)

#Image registrations
screen.register_shape("r2d2.gif")
screen.register_shape("c3po.gif")
screen.register_shape("deathstar.gif")
#variables
animating = False
coords = [(-47, 61),(36.0, -71.0),(37.0, -8.0),(-46.0, -15.0),(-14.0, 22.0),(31.0, 15.0),(18.0, 91.0),(-10.0, 77.0)]

def stampImage(image,x,y):
     pen.teleport(x,y)
     pen.shape(image)
     pen.stamp()
     pen.shape('classic')

def drawCircle(radius, color, x, y, steps=None):
    pen.teleport(x,y)
    pen.begin_fill()
    pen.color(color)
    pen.circle(radius,None,steps)
    pen.end_fill()

def drawTier(x, y, size):
    pen.teleport(x,y)
    pen.begin_fill()
    pen.color("green")
    pen.setheading(60)
    for _ in range(3):
        pen.forward(size)
        pen.right(120)
    pen.end_fill()
    a,b,c = random.random(),random.random(),random.random()
    pen.teleport(0,0)


def drawTree():
    pen.teleport(-25, -100)
    pen.color("brown")
    pen.begin_fill()
    for i in range(2):
        pen.fd(50)
        pen.right(90)
        pen.fd(75)
        pen.right(90)
    pen.end_fill()
    drawTier(-100, -100, 200)
    drawTier(-80, -40, 160)
    drawTier(-60, 40, 120)
    for x,y in coords:
        drawCircle(3,"red", x,y)
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
    a,b,c = random.random(),random.random(),random.random()
    pen.setheading(0)
    pen.teleport(x,y)
    pen.begin_fill()
    pen.color(a,b,c)
    for i in range(4):
        pen.forward(40)
        pen.left(90)
    a,b,c = random.random(),random.random(),random.random()
    pen.end_fill()
    pen.width(5)
    pen.setheading(0)
    pen.teleport(x,y+20)
    pen.color(a,b,c)
    pen.fd(40)
    pen.setheading(90)
    pen.teleport(x+20,y)
    pen.color(a,b,c)
    pen.fd(40)
    pen.width(0)
    drawStar(x+20,y+40,15)

drawTree()
#drawStar(0, 130, 30)
#drawSnowman(-150, -100)
drawPresent(100, -180)
drawPresent(-100, -180)

pen.teleport(0,300)
pen.write("Merry Christmas!",False,"center",("arial",50,"normal"))

stampImage("r2d2.gif",-150,-120)
stampImage("c3po.gif",200,-95)
stampImage("deathstar.gif", 250,250)
if animating:
    snowflakes = []

    for i in range(25):
        flake = turtle.Turtle()
        flake.shape("circle")
        flake.penup()
        flake.color("white")
        flake.teleport(random.randint(-300, 300), random.randint(0, 300))
        snowflakes.append(flake)



    while animating:
        for s in snowflakes:
                    speedX,speedY = random.randint(-20,20),random.randint(-20,0)
                    s.rt(random.randint(0,90))
                    newX = s.xcor()+speedX
                    newY = s.ycor()+speedY
                    s.teleport(newX,newY)
                    #reset the snow to the sky
                    if s.ycor() < -300:
                            s.stamp()
                            s.teleport(random.randint(-300,300),random.randint(0,300))
                            s.color('white')
screen.mainloop()