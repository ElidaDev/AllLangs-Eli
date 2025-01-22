import turtle
painter = turtle.Turtle(shape="square")
wn = turtle.Screen()

def Pattern(vertical,length,sx,sy, color1,color2,distance):
    startx = sx 
    for i in range(vertical):
        sx = startx
        painter.teleport(sx,sy)
        for j in range(length):
            if i % 2 == 0:
                painter.color(color1)
            else:
                painter.color(color2)
            painter.teleport(sx+distance)
            painter.stamp() 
            sx += distance
            i+=1
        sy -= distance

Pattern(8,8,-250,250,"red","black",20)


wn.mainloop()