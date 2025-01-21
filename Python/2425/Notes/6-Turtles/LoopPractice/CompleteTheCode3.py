import turtle as trtl
from random import random
painter = trtl.Turtle()
wn=trtl.Screen() #Fixed trtl.Turtle
painter.speed(0)

def drawingPedals(pedals,x,y, color,distance = 30):
    painter.teleport(x,y)
    for i in range(pedals): # Added to complete flower pedals
        if i % len(color) == 0:
            painter.color(color[0])
        else:
            painter.color(color[1])
        painter.right(360/pedals) # Added to complete flower pedals
        painter.fd(distance) # Added to complete flower pedals
        painter.stamp() # Added to complete flower pedals
# stem
painter.color("green")
painter.pensize(15)
painter.goto(0, -150)
painter.setheading(90)
painter.forward(100)
#  leaf
painter.setheading(270)
painter.circle(20, 120, 20)
painter.setheading(90)
painter.goto(0, -60)
# rest of stem
painter.forward(60)
painter.setheading(0)
# change pen
painter.penup()
painter.shape("circle")
painter.turtlesize(2)
# draw flower
while True:
    drawingPedals(18,20,180,distance= 30,color=("darkorchid","blue"))

wn.mainloop()