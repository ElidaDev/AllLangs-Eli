import turtle
import court as c
import random as r


ball = turtle.Turtle(shape="circle")
ball.color("ivory")
ball.penup()
ball.speed(0)

ball.setheading(0)
COURTHEIGHT = c.COURTHEIGHT
COURTWIDTH = c.COURTWIDTH
BUFFER = 25

wn = turtle.Screen()
wn.screensize(COURTHEIGHT+100,COURTWIDTH+100)
wn.bgcolor("black")

def resetBall():
    ball.setpos(0,0)
    if r.randint(0,1)==0:
        ball.seth(r.randint(-30,30))
    else:
        ball.seth(r.randint(150,210))

def collidePaddle(paddle,ball):
    if paddle.distance(ball)<20:
        ball.seth(180-ball.heading())
        if ball.xcor()>0:
            ball.setx(ball.xcor()-5)
        else:
            ball.setx(ball.xcor()+5)
        ball.fd(10)

def moveBall():
    if ball.ycor() >= COURTHEIGHT/2 or ball.ycor() <= -COURTHEIGHT/2:
        ball.setheading(-ball.heading())
    collidePaddle(leftPlayer,ball)
    collidePaddle(rightPlayer, ball)
    if ball.xcor() >= COURTWIDTH/2+BUFFER:
        resetBall()
    elif ball.xcor() <= -COURTWIDTH/2+BUFFER:
        resetBall()

    ball.fd(10)
    wn.ontimer(moveBall,10)

