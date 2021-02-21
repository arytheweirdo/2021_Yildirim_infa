import turtle

turtle.shape("turtle")


def five():
    turtle.penup()
    turtle.goto(-50, -68)
    turtle.pendown()
    turtle.goto(80, 26)
    turtle.goto(-80, 26)
    turtle.goto(50, -68)
    turtle.goto(0, 80)
    turtle.goto(-50, -68)

# при нечетных n
def star(n, d):
    phi = 180 - (180 / n)
    turtle.left(180 / n)
    for i in range(n):
        turtle.forward(d)
        turtle.left(phi)


star(11, 200)
