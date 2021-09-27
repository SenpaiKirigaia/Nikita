import turtle

def circle(n):
    turtle.shape('turtle')
    for i in range(1, 19):
        turtle.forward(10)
        turtle.left(20)
    turtle.forward(10)
    turtle.left(180)
    for i in range(1, 19):
        turtle.forward(10)
        turtle.left(20)

def lepest(n):
    for i in range(n // 2):
        circle(n)
        turtle.left(360 / n)

n = int(input('Сколько лепестков? '))
lepest(n)