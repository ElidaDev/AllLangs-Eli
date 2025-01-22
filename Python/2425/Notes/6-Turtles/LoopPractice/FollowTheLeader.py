import turtle as trtl
# create an empty list of turtles
my_turtles = []
# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

#adds turtles to my_turtles
for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  newColor=turtle_colors.pop()
  t.color(newColor)
  my_turtles.append(t)

startx,starty = 0,0
direction = 90
#moves the individual turtles
for t in my_turtles:
    t.speed(0)
    t.teleport(startx, starty)
    t.setheading(direction) #point up and to the right
    t.right(45)     
    t.forward(50)
    
    #reset startx,starty,direction for the next turtle
    startx = t.xcor() #grabbing the previous turtle's x coordinate
    starty = t.ycor() 
    direction = t.heading()  
while True:
  for i in range(len(my_turtles)-1):
    nextx,nexty= my_turtles[i+1].xcor(),my_turtles[i+1].ycor()
    my_turtles[i].teleport(nextx,nexty)
wn.mainloop()