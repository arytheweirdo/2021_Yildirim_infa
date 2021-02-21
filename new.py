import turtle as t
import random as r

t.shape("turtle")
for i in range(30):
    dist = r.randint(5, 80)
    angle = r.randint(0, 181)
    if r.randint(1, 3) == 2:
        t.left(angle)
    else:
        t.right(angle)
    t.forward(dist)
