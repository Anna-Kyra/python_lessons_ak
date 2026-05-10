import random
from dae_progfa_lib import ProgfaEngine, ShapeMode
import math
from enum import Enum


class AtomPart:
    class Kind(Enum):
        NEUTRON = 0
        PROTON = 1
        ELECTRON = 2

    def __init__(self, x: float, y: float, kind: Kind):
        self.x = x
        self.y = y
        self.kind = kind
        self.size = 26
        # make atoms go in random directions
        angle = random.uniform(0, 3.14159 * 2)
        self.speed_x = math.cos(angle) * 5
        self.speed_y = math.sin(angle) * 5
        print(kind)

    def display(self, engine: ProgfaEngine):
        """Displays a circle (without an outline) based on the kind of part:
        - neutron: the color is blue and half transpartent.
        - proton: the color is red and shows a black '+' text in the center.
        - electron: the color is yellow and shows a black '-' text in the center."""
        engine.shape_mode = ShapeMode.CENTER
        engine.set_font_size(35)

        # TODO: Draw the atom part according to the docstring / its kind
        if self.kind == self.Kind.NEUTRON:
            engine.color = 0, 0, 1, 0.5
            engine.draw_circle(self.x, self.y, self.size, 0)
            print("neutron")
        elif self.kind == self.Kind.PROTON:
            engine.color = 1, 0, 0
            engine.draw_circle(self.x, self.y, self.size, 0)
            engine.color = 0, 0, 0
            engine.draw_text("+", self.x, self.y, True)
            print("proton")
        elif self.kind == self.Kind.ELECTRON:
            engine.color = 1, 1, 0
            engine.draw_circle(self.x, self.y, self.size, 0)
            engine.color = 0, 0, 0
            engine.draw_text("-", self.x, self.y, True)
            print("electron")

    def move(self):
        # TODO: Move the atom part with its own speed. Do not bounce here.
        self.x += self.speed_x
        self.y += self.speed_y
        pass

    def bounce(self, right_bounds: float, bottom_bounds: float):
        # TODO: Bounce on all sides.
        pass
