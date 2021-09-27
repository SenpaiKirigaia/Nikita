import turtle

for i in range (10):
    turtle.penup()
    turtle.backward(10)
    turtle.left(90)
    turtle.backward(10)
    turtle.right(90)
    turtle.pendown()
    for j in range(4):
        turtle.forward(10 + i * 20)
        turtle.left(90)