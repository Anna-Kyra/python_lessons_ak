import random
from dae_progfa_lib import ProgfaEngine, ShapeMode


class NPC:
    def __init__(self, name : str, engine: ProgfaEngine):
        self.engine = engine
        self.name = name
        self.x = random.randint(0, int(self.engine.width))
        self.y = random.randint(0, int(self.engine.height))

        self.size = 25
        self.color = random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)

        print(self.x)

    def display(self):
        self.engine.shape_mode = ShapeMode.CENTER
        self.engine.color = self.color
        self.engine.draw_square(self.x, self.y, self.size, 0)

    def dialogue(self):
        pass