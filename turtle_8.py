import turtle

turtle.shape('turtle')
n = 10
turtle.goto(0, 0)

for i in range(20):
    turtle.forward(n)
    turtle.left(90)
    n = n + 10
