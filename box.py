from kivy.uix.widget import Widget
from ball import *


class Box(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.balls = []
        self.is_ball_bounce = True

    def add_ball(self):
        b = Ball()
        b.draw(self.canvas)
        self.balls.append(b)
        return self

    def add_balls(self, n):
        for i in range(n):
            self.add_ball()

    def set_color(self, color):
        for b in self.balls:
            b.color = color

    def set_radius(self, r):
        for b in self.balls:
            b.r = r
            b.image.size = (2 * r, 2 * r)

    def set_gravity(self, g):
        for b in self.balls:
            b.g = Vector(0, -g)

    def set_energy_loss(self, loss):
        for b in self.balls:
            b.loss = loss

    def move(self, dt):
        n = self.balls.__len__()
        for i in range(n):
            self.balls[i].bounce_box()
            if self.is_ball_bounce:
                for j in range(i + 1, n):
                    self.balls[i].bounce_ball(self.balls[j])
        for b in self.balls:
            b.move(dt)


if __name__ == "__main__":
    pass
