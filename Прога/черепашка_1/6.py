import turtle

n = int(input('Введите число лапок '))
for i in range(n):
    turtle.forward(150)
    turtle.stamp()
    turtle.backward(150)
    turtle.left(360 / n)