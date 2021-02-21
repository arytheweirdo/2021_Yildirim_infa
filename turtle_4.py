import turtle
import math

turtle.shape("turtle")
rho = 100
d_phi = 360 / 200
turtle.left(90)
for phi_index in range(201):
    phi = phi_index / 200 * 2 * 3.1415926535
    x = rho * math.cos(phi) - rho
    y = rho * math.sin(phi)
    turtle.goto(x, y)
    turtle.left(d_phi)

def circle_left(x_0, y_0, rho):
    turtle.penup()
    turtle.goto(x_0 + rho, y_0)
    delta = 90 - turtle.heading()
    turtle.left(delta)
    turtle.pendown()
    for phi_index in range(201):
        phi = phi_index / 200 * 2 * 3.1415926535
        x = rho * math.cos(phi) + x_0
        y = rho * math.sin(phi) + y_0
        turtle.goto(x, y)
        turtle.left(d_phi)

def circle_right(x_0, y_0, rho):
    turtle.penup()
    turtle.goto(x_0 - rho, y_0)
    delta = 90 - turtle.heading()
    turtle.left(delta)
    turtle.pendown()
    for phi_index in range(201):
        phi = - (phi_index / 200 * 2 * 3.1415926535 - 3.1415926535)
        x = rho * math.cos(phi) + x_0
        y = rho * math.sin(phi) + y_0
        turtle.goto(x, y)
        turtle.right(d_phi)


