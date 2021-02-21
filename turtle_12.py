import turtle
import math



turtle.shape("turtle")
rho = 20
def prujina(rho, x_0, y_0):
    d_phi = 360 / 200
    for i in range(3):
        turtle.penup()
        #turtle.goto(-50, 0)
        delta = 90 - turtle.heading()
        turtle.left(delta)
        turtle.pendown()
        for phi_index in range(201):
            phi = phi_index / 200 * 2 * 3.1415926535
            x = rho * phi - rho * 1.5 * math.sin(phi)
            y = rho - rho * 1.5 * math.cos(phi)
            turtle.goto(x, y)
            turtle.right(phi)
turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
turtle.left(90)
for k in range(6):
    turtle.circle(-50, 180)
    turtle.circle(-20,180)




