from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Color
from kivy.core.window import Window
from kivy.vector import Vector
from random import random as random


class Ball:

    def __init__(self):
        self.color = random()
        self.r = 25
        self.p = Vector((Window.size[0] - 2 * self.r) * random() + self.r,
                        (Window.size[1] - 2 * self.r) * random() + self.r)
        self.v = Vector(200 * (random() - 0.5), 200 * (random() - 0.5))
        self.image = None

    def get_pos(self):
        return self.p.x - self.r, self.p.y - self.r

    def draw(self, canvas):
        with canvas:
            Color(self.color, 1, 1, mode="hsv")
            self.image = Ellipse(pos=self.get_pos(),
                                 size=(2 * self.r, 2 * self.r))

    def bounce_box(self):
        if self.p.x < self.r:
            self.v.x = abs(self.v.x)
            self.p.x = self.r
        if self.p.x > Window.size[0] - self.r:
            self.v.x = - abs(self.v.x)
            self.p.x = Window.size[0] - self.r
        if self.p.y < self.r:
            self.v.y = abs(self.v.y)
            self.p.y = self.r
        if self.p.y > Window.size[1] - self.r:
            self.v.y = - abs(self.v.y)
            self.p.y = Window.size[1] - self.r

    def bounce_ball(self, ball): #clinging is still possible
        d = self.p.distance(ball.p)
        if d < self.r + ball.r:
            e = (ball.p - self.p).normalize()
            self.v -= 2 * e.dot(self.v) * e
            ball.v -= 2 * e.dot(ball.v) * e
            self.p -= (self.r + ball.r - d) / 2 * e
            ball.p += (self.r + ball.r - d) / 2 * e

    def move(self, dt):
        self.p += self.v * dt
        self.image.pos = self.get_pos()


class Box(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.balls = []

    def add_ball(self):
        b = Ball()
        b.draw(self.canvas)
        self.balls.append(b)
        return self

    def move(self, dt):
        n = self.balls.__len__()
        for i in range(n):
            self.balls[i].bounce_box()
            for j in range(i + 1, n):
                self.balls[i].bounce_ball(self.balls[j])
        for b in self.balls:
            b.move(dt)

