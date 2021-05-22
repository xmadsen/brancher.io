import time


class Game:
    def __init__(self, view):
        self.view = view

    def tick(self, tick_seconds=1):
        time.sleep(tick_seconds)

    def run(self):
        while 1:
            self.tick()
            self.view.draw()
