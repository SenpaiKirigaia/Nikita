import turtle as t
import numpy as np

t.shape('turtle')
vx = 15
vy = 65
g = 10
n = 0
t.goto(300, 0)
t.goto(-350, 0)
for i in np.arange(0, 45, 0.03):
    x = vx * i
    y = vy * (i - n) - 0.5 * g * (i - n) ** 2
    t.goto(x - 350, y)
    if y < 0:
        n = i
        vy = vy * 0.8