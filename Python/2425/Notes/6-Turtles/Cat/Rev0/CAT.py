import turtle as t
from random import randint
wn=t.Screen()
wn.bgcolor("black")
wn.screensize(300,300)
scoreKeep=t.Turtle()
scoreKeep.teleport(250,350)
scoreKeep.color("white")
scoreKeep.ht()
turtle =t.Turtle("turtle")
turtle.shapesize(2)
turtle.color("aquamarine")
turtle.speed(5)
score=0
def moveTurtle():
    turtle.goto(randint(-290,290),randint(-290,290))
def updateScore():
    global score
    score+=1
    scoreKeep.clear()
    scoreKeep.write(score, font=("Times New Roman",30,"normal"))
def hit(x,y):
    print("Whacked!")
    moveTurtle()
    updateScore()
turtle.onclick(hit)
wn.mainloop()