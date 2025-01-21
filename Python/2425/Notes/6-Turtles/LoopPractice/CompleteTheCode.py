import turtle as trtl
from random import random
painter = trtl.Turtle()
wn=trtl.Screen() #Fixed trtl.Turtle
painter.speed(0)

def drawingPedals(pedals,x,y, distance = 30, color="Random"):
    if color != "Random":
        painter.color(color)
    painter.teleport(x,y)
    for i in range(pedals): # Added to complete flower pedals
        if color == "Random":
            painter.color((random(),random(),random()))
        painter.stamp() # Added to complete flower pedals
        painter.right(360/pedals) # Added to complete flower pedals
        painter.fd(distance) # Added to complete flower pedals
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
    drawingPedals(18,20,180)
wn.mainloop()