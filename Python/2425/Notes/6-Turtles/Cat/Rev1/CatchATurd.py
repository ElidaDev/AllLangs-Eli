import turtle as t
import random as r
import Leaderboard as lb

#---global var and objects and game configuration
wn = t.Screen()   #everything is clickable...
wn.bgcolor("black")
wn.setup(600,725)

turtle = t.Turtle(shape="turtle")
turtle.shapesize(2)
turtle.color("aquamarine")
turtle.speed(0)

scoreKeeper = t.Turtle()
scoreKeeper.speed(0)
scoreKeeper.teleport(100,315)
scoreKeeper.color("pink")
scoreKeeper.ht()

leaderBoardDrawer = t.Turtle()
leaderBoardDrawer.speed(0)
leaderBoardDrawer.teleport(100,315)
leaderBoardDrawer.color("pink")
leaderBoardDrawer.ht()

timeKeeper = t.Turtle()
timeKeeper.color("goldenrod3")
timeKeeper.teleport(-200,315)
timeKeeper.ht()

score=0
timer=5
interval=1000
fontSetup = ("Times New Roman", 30, "normal")

playerName = input("Please enter a name to use: ")
#---f(x)
#every command that is based on a mouse click MUST HAVE the x,y var passed in
def turtleClicked(mouseX,mouseY):  #add any features to this f(x) that trigger when turtle is clicked
    print(f"turtle was clicked at {mouseX},{mouseY}")
    moveturtle()
    updateScore()

def moveturtle():
    turtle.stamp()
    newX=r.randint(-290,290)
    newY=r.randint(-290,290)
    turtle.goto(newX,newY)

def updateScore():
    global score
    score+=1
    print(score)
    scoreKeeper.clear()   #clears ANYTHING it wrote..........................
    scoreKeeper.write(f"Score: {score}",font=("Times New Roman",30,"normal"))

def updateTimer():
    global timer
    timer-=1
    timeKeeper.clear()
    if timer<=0:
        timeKeeper.write("Time's Up!",font=fontSetup)
        manageLeaderBoard()
    else:
        timeKeeper.write(f"Time: {timer}",font=fontSetup)
        timeKeeper.getscreen().ontimer(updateTimer,interval)

def manageLeaderBoard(): #gameover/update HS
    global score
    highScorer = False
    if score > int(lb.getScores()[-1]):
        lb.updateLeaderboard(lb.getNames(),lb.getScores(),playerName,score)
        highScorer = True
    lb.drawLeaderboard(highScorer,lb.getNames(),lb.getScores(),leaderBoardDrawer,score)

#---events - event handlers
turtle.onclick(turtleClicked)
wn.ontimer(updateTimer,interval)

#---mainloop
wn.mainloop()

'''
    Features List:
        1. Click a turd
        2. Turd move randomly
        3. Score
        4. Timer
        5. High Score rev1 or tomorrow
'''
