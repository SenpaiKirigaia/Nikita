
import turtle as t

def line2(a, i):
    if i == 0:
        t.right(a)
    else:
        t.left(180 - a)
    t.forward(100)

def line(n, i):
    a = 180 / n
    if i == 0:
        b = a / 2
        line2(b, i)
    else:
        line2(a, i)

n = 0
n = int(input('Сколько вершин? '))
while n % 2 == 0:
    n = int(input('Вы ввели четное число, введите, пожалуйста, нечетное число '))
t.penup()
t.goto(0, 200)
t.pendown()
t.right(90)
for i in range(n):
    line(n, i)