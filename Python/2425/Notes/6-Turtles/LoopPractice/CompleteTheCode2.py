import turtle as trtl
painter = trtl.Turtle()
wn=trtl.Screen() #Fixed trtl.Turtle
painter.speed(0)
# stem
painter.color("green")
painter.pensize(15)
painter.goto(0, -150)
painter.setheading(90)
painter.forward(100)
#  leaf
painter.setheading(270)
painter.circle(20, 120, 20)
painter.setheading(90)
painter.goto(0, -60)
# rest of stem
painter.forward(60)
painter.setheading(0)
# change pen
painter.penup()
painter.shape("circle")
painter.turtlesize(2)
# draw flower
painter.color("darkorchid")
painter.goto(20,180)
for i in range(18): # Added to complete flower pedals
    painter.stamp() # Added to complete flower pedals
    painter.right(20) # Added to complete flower pedals
    painter.fd(30) # Added to complete flower pedals
   
wn.mainloop()