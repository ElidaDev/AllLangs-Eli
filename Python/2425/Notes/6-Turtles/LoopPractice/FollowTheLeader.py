import turtle as trtl
# create an empty list of turtles
my_turtles = []
# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in range(len(turtle_shapes)):
  t = trtl.Turtle(shape=turtle_shapes[s])
  t.color(turtle_colors[s])
  my_turtles.append(t)
wn = trtl.Screen()
startx = 0
starty = 0
currentHeading = 90
while True:
    for t in my_turtles:
        t.teleport(startx, starty)
        t.setheading(currentHeading)
        t.right(45)     
        t.forward(50)
        currentHeading += 45
        startx = t.xcor()
        starty = t.ycor()
        currentHeading = t.heading()

wn.mainloop()