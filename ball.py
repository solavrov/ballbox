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
        self.g = Vector(0, 0)
        self.loss = 0
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
            self.v *= (1 - self.loss)
        if self.p.x > Window.size[0] - self.r:
            self.v.x = - abs(self.v.x)
            self.p.x = Window.size[0] - self.r
            self.v *= (1 - self.loss)
        if self.p.y < self.r:
            self.v.y = abs(self.v.y)
            self.p.y = self.r
            self.v *= (1 - self.loss)
        if self.p.y > Window.size[1] - self.r:
            self.v.y = - abs(self.v.y)
            self.p.y = Window.size[1] - self.r
            self.v *= (1 - self.loss)

    def bounce_ball(self, ball): #clinging is still possible
        d = self.p.distance(ball.p)
        if d < self.r + ball.r:
            e = (ball.p - self.p).normalize()
            self.v -= 2 * e.dot(self.v) * e
            ball.v -= 2 * e.dot(ball.v) * e
            self.p -= (self.r + ball.r - d) / 2 * e
            ball.p += (self.r + ball.r - d) / 2 * e
            self.v *= (1 - self.loss)
            ball.v *= (1 - ball.loss)

    def move(self, dt):
        self.v += self.g * dt
        self.p += self.v * dt
        self.image.pos = self.get_pos()


if __name__ == "__main__":
    pass
