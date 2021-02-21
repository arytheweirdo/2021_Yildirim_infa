import turtle
import math

deg = 3.1415926535 / 180

turtle.shape('turtle')


def mnogougolnik(n, a):
    d_phi = 360 / n
    delta = 90 - turtle.heading()
    turtle.left(delta)
    alpha = d_phi / 2
    turtle.left(alpha)
    for i in range(1, n + 1):
        x = a * math.cos(d_phi * i * deg)
        y = a * math.sin(d_phi * i * deg)
        turtle.goto(x, y)
        turtle.left(d_phi)
    delta = 90 - turtle.heading()
    turtle.left(delta)


turtle.left(90)
a = 50
b = 10
turtle.penup()
turtle.goto(a, 0)
turtle.pendown()
for k in range(3, 9):
    mnogougolnik(k, a)
    a = a + 20
    turtle.right(90)
    turtle.penup()
    turtle.goto(a, 0)
    turtle.pendown()

