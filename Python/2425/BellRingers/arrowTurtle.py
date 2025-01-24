import turtle
import time

wn = turtle.Screen()
painter = turtle.Turtle()
painter.direction = ""
exit = False
def move():
    if painter.direction == "up":
        painter.sety(painter.ycor()+20)
    if painter.direction == "down":
        painter.sety(painter.ycor()-20)
    if painter.direction == "left":
        painter.setx(painter.xcor()-20)
    if painter.direction == "right":
        painter.setx(painter.xcor()+20)
    if painter.direction == "stop":
        exit = True
    
def up():
    painter.direction="up"
def down():
    painter.direction="down"
def right():
    painter.direction="right"
def left():
    painter.direction="left"
def stop():
    painter.direction="stop"
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")
wn.onkeypress(stop,"Q")
wn.listen()
while not exit:
    wn.update()
    move()
    time.sleep(0.1)
