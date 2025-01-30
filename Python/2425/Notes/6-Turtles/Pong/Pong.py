import ball as b
import turtle as t
import court as c

#left player or player blue
leftPlayer = t.Turtle("square")
leftPlayer.color("blue")
leftPlayer.penup()
leftPlayer.speed(0)
leftPlayer.turtlesize(4,1)                   #turtlesize will stretch the turtle
leftPlayer.setx(-c.COURTWIDTH/2+10)

#left player or player blue
rightPlayer = t.Turtle("square")
rightPlayer.color("orange")
rightPlayer.penup()
rightPlayer.speed(0)
rightPlayer.turtlesize(4,1)                   #turtlesize will stretch the turtle
rightPlayer.setx(c.COURTWIDTH/2-10)

wn = t.Screen()
wn.onkeypress(b.resetBall,"r")

def up(paddle):
    if not(paddle.ycor() >= c.COURTHEIGHT/2-25): 
        paddle.sety(paddle.ycor()+10)
def down(paddle):
    if not(paddle.ycor() <= -c.COURTHEIGHT/2+25): 
        paddle.sety(paddle.ycor()-10)

def collidePaddle(paddle,ball):
    if paddle.distance(ball)<20:
        ball.seth(180-ball.heading())
        if ball.xcor()>0:
            ball.setx(ball.xcor()-5)
        else:
            ball.setx(ball.xcor()+5)
        ball.fd(10)
wn.onkeypress(lambda: up(leftPlayer),"w")
wn.onkeypress(lambda: down(leftPlayer),"s")
wn.onkeypress(lambda: up(rightPlayer),"Up")
wn.onkeypress(lambda: down(rightPlayer),"Down")

c.drawCourt()
b.moveBall()

wn.listen()
wn.mainloop()
