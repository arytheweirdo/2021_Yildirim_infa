import turtle
import math

d_phi = 360 / 13
turtle.shape("turtle")
rho = 100
turtle.penup()
turtle.goto(0, 0)
for i in range(12):
    phi = 2 * 3.1415926535 / 12 * i
    x = rho * math.cos(phi)
    y = rho * math.sin(phi)
    turtle.pendown()
    # угол поворота черепашки!!!
    turtle.goto(x, y)
    turtle.left(d_phi)
    turtle.stamp()
    turtle.goto(0, 0)


