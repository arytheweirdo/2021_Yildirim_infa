from random import randrange as rnd, choice
import tkinter as tk
import math
import time

print(dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=1)
score = 0


class Ball:
    def __init__(self, x=40, y=450, vx=0, vy=0):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = vx
        self.vy = vy
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canvas.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canvas.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        g = 20
        t = 0.03
        k = 0.01
        m = 0.8
        if self.x - self.r < 0:
            self.vx = -self.vx * m
        if self.x - self.r > 800:
            self.vx = -self.vx * m
        if self.y + self.r > 600:
            self.vy = -self.vy * m
            self.y -= self.vy
        if self.y - self.r < 0:
            self.vy = -self.vy * m
        self.vx -= k * self.vx
        self.x += self.vx
        self.vy -= g * t + k * self.vy
        self.y -= self.vy
        self.live += 1

    def draw(self):
        canvas.delete(self.id)
        self.id = canvas.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        if self.live > 200:
            canvas.delete(self.id)

    def hitting(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        global flag
        flag = True
        if (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= (obj.r + self.r) ** 2:
            return flag
        else:
            return not flag


class Gun:
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canvas.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """
        Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        self.f2_on = 0
        self.f2_power = 10
        balls += [new_ball]

    def targeting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canvas.itemconfig(self.id, fill='orange')
        else:
            canvas.itemconfig(self.id, fill='black')
        canvas.coords(self.id, 20, 450,
                      20 + max(self.f2_power, 20) * math.cos(self.an),
                      450 + max(self.f2_power, 20) * math.sin(self.an)
                      )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canvas.itemconfig(self.id, fill='orange')
        else:
            canvas.itemconfig(self.id, fill='black')


class Target:
    global score

    def __init__(self):
        global score
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(20, 50)
        self.vx = rnd(2, 10)
        self.vy = rnd(2, 10)
        self.color = 'red'
        self.points = 0
        self.live = 1
        self.id = canvas.create_oval(0, 0, 0, 0)
        self.id_points = canvas.create_text(30, 30, text=score, font='28')
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(20, 50)
        self.vx = rnd(-10, 10)
        self.vy = rnd(-10, 10)
        color = self.color = 'red'
        canvas.coords(self.id, x - r, y - r, x + r, y + r)
        canvas.itemconfig(self.id, fill=color)

    def outbound(self):
        x = self.x = -100
        self.vx = 0
        self.vy = 0
        y = self.y
        r = self.r
        color = self.color = 'red'
        canvas.coords(self.id, x - r, y - r, x + r, y + r)
        canvas.itemconfig(self.id, fill=color)

    def draw(self):
        x = self.x
        y = self.y
        r = self.r
        color = self.color
        canvas.coords(self.id, x - r, y - r, x + r, y + r)
        canvas.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canvas.coords(self.id, -10, -10, -10, -10)
        self.points += points
        return self.points

    def draw_hit(self):
        canvas.itemconfig(self.id_points, text=self.points)

    def move(self):
        if self.x - self.r < 0:
            self.vx = -self.vx
        if self.x - self.r > 800:
            self.vx = -self.vx
        if self.y + self.r > 600:
            self.vy = -self.vy
            self.y -= self.vy
        if self.y - self.r < 0:
            self.vy = -self.vy
        self.x += self.vx
        self.y -= self.vy


t1 = Target()
t2 = Target()
screen1 = canvas.create_text(400, 300, text='', font='28')
g1 = Gun()
bullet = 0
balls = []
targets = [t1, t2]


def new_game(event=''):
    global Gun, t1, screen1, balls, bullet, t2, score, targets
    canvas.itemconfig(screen1, text='')
    t2.new_target()
    t1.new_target()
    score = 0
    bullet = 0
    balls = []
    canvas.bind('<Button-1>', g1.fire2_start)
    canvas.bind('<ButtonRelease-1>', g1.fire2_end)
    canvas.bind('<Motion>', g1.targeting)
    z = 0.03
    t1.live = 1
    t2.live = 1
    while t1.live or t2.live:
        for b in balls:
            b.move()
            if b.hitting(t1) and t1.live:
                t1.live = 0
                score += t1.hit()
                b.live = 201
                t1.outbound()
            if b.hitting(t2) and t2.live:
                t2.live = 0
                score += t2.hit()
                b.live = 201
                t2.outbound()
            if t1.live + t2.live == 0:
                for b in balls:
                    b.live = 201
                canvas.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                canvas.bind('<Button-1>', '')
                canvas.bind('<ButtonRelease-1', '')
                t1.draw_hit()
                t2.draw_hit()
                root.after(1000, new_game)
        for t in targets:
            t.move()
            t.draw()
        for b in balls:
            b.draw()
        canvas.update()
        time.sleep(z)
        g1.targeting()
        g1.power_up()
    canvas.delete(Gun)


new_game()


tk.mainloop()
