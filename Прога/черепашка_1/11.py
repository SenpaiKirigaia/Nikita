import turtle

def circle(n, j):
    turtle.shape('turtle')
    for i in range(1, 19):
        turtle.forward(10 + j * 3)
        turtle.left(20)
    turtle.forward(10+ j * 3)
    turtle.left(180)
    for i in range(1, 19):
        turtle.forward(10 + 3 * j)
        turtle.left(20)

def lepest(n):
    for j in range(n):
        circle(n, j)

n = int(input('Сколько крыльев? '))
lepest(n)