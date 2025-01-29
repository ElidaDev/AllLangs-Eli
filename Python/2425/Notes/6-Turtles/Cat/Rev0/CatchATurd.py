import turtle as t
import random as r

#---global var and objects and game configuration
wn = t.Screen()   #everything is clickable...
wn.bgcolor("black")
wn.setup(600,725)

ruffis = t.Turtle(shape="turtle")
ruffis.shapesize(2)
ruffis.color("aquamarine")
ruffis.speed(1)

scoreKeeper = t.Turtle()
scoreKeeper.speed(0)
scoreKeeper.teleport(100,315)
scoreKeeper.color("pink")
scoreKeeper.ht()

timeKeeper = t.Turtle()
timeKeeper.color("goldenrod3")
timeKeeper.teleport(-200,315)
timeKeeper.ht()

score=0
timer=5
interval=1000
fontSetup = ("Times New Roman", 30, "normal")

#---f(x)
#every command that is based on a mouse click MUST HAVE the x,y var passed in
def ruffisClicked(mouseX,mouseY):  #add any features to this f(x) that trigger when ruffis is clicked
    print(f"ruffis was clicked at {mouseX},{mouseY}")
    moveRuffis()
    updateScore()

def moveRuffis():
    ruffis.stamp()
    newX=r.randint(-290,290)
    newY=r.randint(-290,290)
    ruffis.goto(newX,newY)

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
    else:
        timeKeeper.write(f"Time: {timer}",font=fontSetup)
        timeKeeper.getscreen().ontimer(updateTimer,interval)

#---events - event handlers
ruffis.onclick(ruffisClicked)
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
