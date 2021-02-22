import turtle

turtle.shape('turtle')
n = 0
for k in range(10):
    n = n + 20
    for i in range(4):
        turtle.forward(n)
        turtle.left(90)
    turtle.right(90)
    turtle.penup()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(180)
    turtle.pendown()
