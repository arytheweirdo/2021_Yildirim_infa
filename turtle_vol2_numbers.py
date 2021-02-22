import turtle as t

t.shape("turtle")
t.pencolor("blue")
t.pensize(7)


def position_control(position_1, position_2):
    t.penup()
    t.goto(position_1, position_2)
    t.pendown()
    delta = 90 - t.heading()
    t.left(delta)


def turtle_0(position_1, position_2):
    position_control(position_1, position_2)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(100)


def turtle_1(position_1, position_2):
    position_control(position_1, position_2)
    t.right(45)
    t.forward(70.7)
    t.right(135)
    t.forward(100)


def turtle_2(position_1, position_2):
    position_control(position_1, position_2)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(45)
    t.forward(70.7)
    t.left(135)
    t.forward(50)


def turtle_3(position_1, position_2):
    position_control(position_1, position_2)
    t.right(90)
    t.forward(50)
    t.right(135)
    t.forward(70.7)
    t.left(135)
    t.forward(50)
    t.right(135)
    t.forward(70.7)


def turtle_4(position_1, position_2):
    position_control(position_1, position_2)
    t.right(180)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.left(180)
    t.forward(100)


def turtle_5(position_1, position_2):
    position_control(position_1, position_2)
    t.right(180)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.penup()
    t.goto(position_1, position_2)
    t.right(180)
    t.pendown()
    t.forward(50)


def turtle_6(position_1, position_2):
    position_control(position_1, position_2)
    t.left(45)
    t.forward(70.7)
    t.left(45)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)


def turtle_7(position_1, position_2):
    position_control(position_1, position_2)
    t.right(90)
    t.forward(50)
    t.right(135)
    t.forward(70.7)
    t.left(45)
    t.forward(50)


pos_1 = [-150, 50]
pos_2 = [-80, 100]
pos_3 = [-10, 50]
pos_4 = [60, 100]
pos_5 = [130, 100]
pos_6 = [200, 100]

turtle_1(*pos_1)
turtle_4(*pos_2)
turtle_1(*pos_3)
turtle_7(*pos_4)
turtle_0(*pos_5)
turtle_0(*pos_6)

out = open('output.txt', 'w')
print(pos_1, pos_3, pos_4, file=out)
out.close()
