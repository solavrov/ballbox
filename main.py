from kivy.app import App
from kivy.clock import Clock
from box import *


class BallBoxApp(App):

    def build(self):

        print(Window.size)

        box = Box()
        box.add_ball().add_ball().add_ball().add_ball().add_ball()
        box.add_ball().add_ball().add_ball().add_ball().add_ball()
        Clock.schedule_interval(box.move, 1.0 / 60.0)

        return box


if __name__ == "__main__":
    BallBoxApp().run()

