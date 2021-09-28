import turtle as t

def do(digit, number):
    x = 40
    t.penup()
    t.goto(digit[0][0] + number * x, digit[0][1])
    t.pendown()
    for point in digit:
        t.goto(point[0] + number*x, point[1])

A1 = [0, 0]
A2 = [30, 0]
A3 = [0, 30]
A4 = [30, 30]
A5 = [0, 60]
A6 = [30, 60]
zero = (A1, A2, A6, A5, A1)
one = (A3, A6, A2)
two = (A2, A1, A4, A6, A5)
three = (A5, A6, A3, A4, A1)
four = (A2, A4, A6, A4, A3, A5)
five = (A1, A2, A4, A3, A5, A6)
six = (A3, A4, A2, A1, A3, A6)
seven = (A1, A3, A6, A5)
eight = (A1, A2, A4, A3, A1, A5, A6, A2)
nine = (A1, A4, A6, A5, A3, A4)
do(one, -4)
do(four, -3)
do(one, -2)
do(seven, -1)
do(zero, 0)
do(zero, 1)