import random
from dae_progfa_lib import ProgfaEngine, ShapeMode


class NPC:
    def __init__(self, name : str, engine: ProgfaEngine):
        self.name = name
        self.x = random.randint(0, engine.width)
        self.y = random.randint(0, engine.height)

        self.size = 25
        self.color = random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)

        print(self.x)

    def display(self, engine : ProgfaEngine):
        engine.shape_mode = ShapeMode.CENTER
        engine.color = self.color
        engine.draw_square(self.x, self.y, self.size, 0)
