import ball as b
import turtle as t
import court as c

wn = t.Screen()
# wn.onkeypress(b.resetBall,"r")
wn.onkeypress(lambda: b.up(b.leftPlayer),"w")
wn.onkeypress(lambda: b.down(b.leftPlayer),"s")
wn.onkeypress(lambda: b.up(b.rightPlayer),"Up")
wn.onkeypress(lambda: b.down(b.rightPlayer),"Down")

b.updateScores()
c.drawCourt()
b.moveBall()
#Foreshadowing is a narrative device used as a warning or indication of (a future event).
wn.listen()
wn.mainloop()
