from random import randint
import turtle

def square(x):
    unit.penup()
    unit.goto(x, -y)
    unit.pendown()
    for i in range(4):
        unit.left(90)
        unit.forward(x * 2)

number_of_turtles = 30
steps_of_time_number = 300
x = 300
y = 300

pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
i = 0
for unit in pool:
    if i == 0:
        square(x)
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-x, x), randint(-y, y))
    unit.left(randint(0, 360))
    i = 1


for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(5)
        if unit.xcor() < -x or unit.xcor() > x:
            a = unit.heading()
            unit.right(180 + 2 * a)
        if unit.ycor() < -y or unit.ycor() > y:
            a = unit.heading()
            unit.right(2 * a)