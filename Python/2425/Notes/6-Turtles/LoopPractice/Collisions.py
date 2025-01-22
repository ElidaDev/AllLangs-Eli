import turtle as trtl
# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []
# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]
tloc = 50
for s in turtle_shapes:
  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)
  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  
  tloc += 50
# TODO: move turtles across and down screen, stopping for collisions

def checkForCollison(t1,t2,distance):
    if (abs(t1.xcor()-t2.xcor()) < distance )and (abs(t1.ycor()-t2.ycor()) < distance) :
        t1.color("gray")
        t2.color("gray")
        return True
    return False

for step in range(50):
    for i in range(len(vert_turtles)):
        vert_turtles[i].fd(5)
        horiz_turtles[i].fd(5)
        if checkForCollison(horiz_turtles[i],vert_turtles[i],20):
            # Stop the 2 turtles in question...
            pass
    


        

wn = trtl.Screen()
wn.mainloop()