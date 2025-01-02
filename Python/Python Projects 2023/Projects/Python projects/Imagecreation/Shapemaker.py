from turtle import * 
from random import randint
import time
     
     
speed(0)
penup()
goto(0, 0)


def shapemaker (sides, length, width):
    for i in range(sides):
        pendown()
        forward(length)
        left(360/sides)
        forward(width)

sides = int(input("Amount of sides: "))
length = float(input("Length: "))
width = float(input("Width: "))

print (360/sides)
shapemaker(sides, length, width)

time.sleep(5)