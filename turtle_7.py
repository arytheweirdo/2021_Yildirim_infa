import turtle
import math


def spiral(x_0, y_0, alpha):
    d_phi = 360 / 40
    turtle.penup()
    turtle.goto(x_0, y_0)
    delta = 90 - turtle.heading()
    turtle.left(delta)
    turtle.pendown()
    for phi_index in range(401):
        phi = phi_index / 40 * 2 * 3.1415926535
        rho = alpha * phi
        x = rho * math.cos(phi) + x_0
        y = rho * math.sin(phi) + y_0
        turtle.goto(x, y)
        turtle.left(d_phi)

spiral(0, 0, 1)
