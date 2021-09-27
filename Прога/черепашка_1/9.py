import turtle

def ris(n):
    turtle.shape('turtle')
    a = (n-2) * 180 / n
    turtle.left(180 - a / 2)
    turtle.forward(20 + n * 8)
    for i in range(n - 1):
        turtle.left(180 - a)
        turtle.forward(20 + n * 8)
    turtle.right(a / 2)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

for i in range(3, 13):
    ris(i)