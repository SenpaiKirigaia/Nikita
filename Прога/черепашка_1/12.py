import turtle

def circle(n):
    turtle.shape('turtle')
    for i in range(1, 10):
        turtle.forward(20)
        turtle.left(20)
    turtle.forward(20)
    for i in range(1, 10):
        turtle.forward(2)
        turtle.left(20)

def lepest(n):
    for j in range(n):
        circle(n)

n = int(input('Сколько дуг? '))
turtle.penup()
turtle.forward(200)
turtle.left(90)
turtle.pendown()
lepest(n)