import turtle
colors =['red','orange','yellow','green','light blue','blue','purple']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range (360) :
    t.pencolor(colors[x%7])
    t.width(x/100+1)
    t.forward(x)
    t.left(100)