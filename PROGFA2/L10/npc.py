import random
from dae_progfa_lib import ProgfaEngine, ShapeMode
from map import Map

class NPC:
    def __init__(self, name : str, map : Map, engine: ProgfaEngine):
        self.engine = engine
        self.map = map
        self.name = name
        row, col = self.map.get_random_walkable_tile()

        self.x = col * self.map.CELL_SIZE
        self.y = row * self.map.CELL_SIZE

        self.size = self.map.CELL_SIZE
        self.color = random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)

        print(self.x)

    def display(self):
        # self.engine.shape_mode = ShapeMode.CENTER
        self.engine.color = self.color
        self.engine.draw_square(self.x, self.y, self.size, 0)

    def dialogue(self):
        pass