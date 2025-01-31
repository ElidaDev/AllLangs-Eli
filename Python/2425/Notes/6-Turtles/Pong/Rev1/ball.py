import turtle
import court as c
import random as r


scoreL = 0
scoreR = 0
fontSetup = ("Comic Sans MS", 30, "normal")

ball = turtle.Turtle(shape="circle")
ball.color("ivory")
ball.penup()
ball.speed(0)

scoreKeeper = turtle.Turtle()
scoreKeeper.speed(0)
scoreKeeper.teleport(-c.COURTWIDTH/4,c.COURTHEIGHT/2+15)
scoreKeeper.color("blue")
scoreKeeper.ht()

scoreKeeperR = turtle.Turtle()
scoreKeeperR.speed(0)
scoreKeeperR.teleport(c.COURTWIDTH/4,c.COURTHEIGHT/2+15)
scoreKeeperR.color("orange")
scoreKeeperR.ht()

leftPlayer = turtle.Turtle("square")
leftPlayer.color("blue")
leftPlayer.penup()
leftPlayer.speed(0)
leftPlayer.turtlesize(4,1)                   #turtlesize will stretch the turtle
leftPlayer.setx(-c.COURTWIDTH/2+10)

#left player or player blue
rightPlayer = turtle.Turtle("square")
rightPlayer.color("orange")
rightPlayer.penup()
rightPlayer.speed(0)
rightPlayer.turtlesize(4,1)                   #turtlesize will stretch the turtle
rightPlayer.setx(c.COURTWIDTH/2-10)

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

def up(paddle):
    if not(paddle.ycor() >= c.COURTHEIGHT/2-25): 
        paddle.sety(paddle.ycor()+10)
def down(paddle):
    if not(paddle.ycor() <= -c.COURTHEIGHT/2+25): 
        paddle.sety(paddle.ycor()-10)

def updateScores():
    scoreKeeper.clear()
    scoreKeeperR.clear()
    scoreKeeper.write(f"Score: {scoreL}", align="left",font=fontSetup)
    scoreKeeperR.write(f"Score: {scoreR}", align="right",font=fontSetup)

def moveBall():
    global scoreR
    global scoreL
    if ball.ycor() >= COURTHEIGHT/2 or ball.ycor() <= -COURTHEIGHT/2:
        ball.setheading(-ball.heading())
    collidePaddle(leftPlayer,ball)
    collidePaddle(rightPlayer, ball)
    if ball.xcor() >= COURTWIDTH/2+BUFFER:
        scoreL += 1
        updateScores()
        resetBall()
    elif ball.xcor() <= -COURTWIDTH/2-BUFFER:
        scoreR += 1
        updateScores()
        resetBall()
    ball.fd(10)
    wn.ontimer(moveBall,10)
