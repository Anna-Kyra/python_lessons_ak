from dae_progfa_lib import ProgfaEngine, ShapeMode
from dae_progfa_lib.progfa_image import ProgfaImage

from chicken import Chicken
import random

from enum import Enum

class Nest:
    def __init__(self, x : float, y : float, name: str, nest_image : ProgfaImage, egg_image : ProgfaImage, engine : ProgfaEngine):
        self.engine = engine
        self.x = x
        self.y = y
        self.name = name
        self.nest_image = nest_image
        self.egg_image = egg_image
        self.chicken : Chicken = Chicken(self.engine)
        self.egg_number = 0

        self.has_egg = random.randrange(0, 2)
        if self.has_egg == 0:
            # print(f"niet: {self.has_egg}")
            self.has_egg = False
        else:
            # print(f"wel: {self.has_egg}")
            self.has_egg = True

        # print(self.has_egg)
        self.onthuld = False

        # print(self.chicken.current_activity.value)

    def display(self):
        self.nest_image.draw_fixed_size(self.x, self.y, 100, 100)

        if self.has_egg:
            self.egg_image.draw_fixed_size(self.x, self.y, 100, 100)

        if self.onthuld:
            self.chicken.display(self.x - 20 - 80, self.y - 20 + 24)
        else:
            self.chicken.display(self.x - 20, self.y - 20)

    def reveal(self):
        self.onthuld = True

        self.chicken.current_activity = Chicken.Activity.STARE
        # print(self.chicken.current_activity.value)

    def cover(self):
        self.onthuld = False
        self.has_egg = random.randrange(0, 2)
        self.chicken.current_activity = Chicken.Activity.IDLE
        # print(f"Two: {self.has_egg}")
