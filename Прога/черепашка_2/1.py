import turtle as t
from random import *

def rand(a, b):
    x = randint(a, b)
    y = randint(0, 180)
    t.forward(x)
    t.left(y)

a = 20
b = 60
for i in range(50):
    rand(a, b)