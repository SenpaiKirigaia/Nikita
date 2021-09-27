import turtle

def picture(f, l):
    for i in range(f):
        turtle.forward(l)
        turtle.left(10)
    turtle.forward(l)
    turtle.end_fill()

def circle(f, l, color, n):
    turtle.shape('turtle')
    turtle.pendown()
    turtle.fillcolor(color)
    if n == 1:
        turtle.begin_fill()
    if f == 36:
        picture(36, l)
    else:
        picture(18, l)
    turtle.penup()


circle(36, 20, "yellow", 1)
turtle.goto(-30, 180)
turtle.left(180)
circle(36, 3, "blue", 1)
turtle.goto(50, 180)
circle(36, 3, "blue", 1)
turtle.left(90)
turtle.goto(10, 150)
turtle.fillcolor("black")
turtle.pendown()
turtle.width(10)
turtle.forward(50)
turtle.penup()
turtle.forward(60)
turtle.goto(-50, 100)
turtle.pencolor("red")
circle(18, 10, "red", 0)