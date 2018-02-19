from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Color
from kivy.core.window import Window
from kivy.vector import Vector
from random import random as random


class Ball:

    def __init__(self):
        self.color = random()
        self.radius = 25
        self.p = Vector((Window.size[0] - 2 * self.radius) * random() + self.radius,
                        (Window.size[1] - 2 * self.radius) * random() + self.radius)
        self.v = Vector(200 * (random() - 0.5), 200 * (random() - 0.5))
        self.image = None

    def get_pos(self):
        return self.p.x - self.radius, self.p.y - self.radius

    def draw(self, canvas):
        with canvas:
            Color(self.color, 1, 1, mode="hsv")
            self.image = Ellipse(pos=self.get_pos(),
                                 size=(2 * self.radius, 2 * self.radius))

    def bounce_box(self):
        if self.p.x < self.radius:
            self.v.x = abs(self.v.x)
            self.p.x = self.radius
        if self.p.x > Window.size[0] - self.radius:
            self.v.x = - abs(self.v.x)
            self.p.x = Window.size[0] - self.radius
        if self.p.y < self.radius:
            self.v.y = abs(self.v.y)
            self.p.y = self.radius
        if self.p.y > Window.size[1] - self.radius:
            self.v.y = - abs(self.v.y)
            self.p.y = Window.size[1] - self.radius

    # def get_dist(self, ball):
    #     return sqrt((self.x - ball.x)**2 + (self.y - ball.y)**2)

    # def bounce_balls(self, balls):
    #     for b in balls:
    #         if self.get_dist(b) < self.radius + b.radius:
    #             self.

    def move(self, dt):
        self.bounce_box()
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
        for b in self.balls:
            b.move(dt)
