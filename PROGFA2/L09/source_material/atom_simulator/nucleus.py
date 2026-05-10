from dae_progfa_lib import ProgfaEngine, ShapeMode

from atom_part import AtomPart
import random
import math

class Nucleus:
    def __init__(self, center_x: float, center_y: float, num_protons: int, num_neutrons: int):
        self.atom_parts = []
        self.center_x = center_x
        self.center_y = center_y
        self.radius = 50

        # TODO: Create a loop that loops num_protons times.
        #  => In this loop, add PROTON atom parts in a random position (use given _get_random_position with above radius)
        #  => add these protons to self.atom_parts (see above) -> composition
        for proton in range(num_protons):
            x, y = self._get_random_position(self.radius)
            self.atom_parts.append(proton)

        # TODO: Create a loop that loops num_neutrons times.
        #  => In this loop, add NEUTRON atom parts in a random position (use given _get_random_position with above radius)
        #  => add these neutrons to self.atom_parts (see above) -> composition

    def _get_random_position(self, radius: float) -> tuple[float, float]:
        angle = random.uniform(0, 3.14159 * 2)
        rnd_radius = random.uniform(0, radius) - 13
        x = self.center_x + math.cos(angle) * rnd_radius
        y = self.center_y + math.sin(angle) * rnd_radius
        return (x, y)

    def display(self, engine: ProgfaEngine):
        engine.outline_color = 1, 1, 1
        engine.color = None
        engine.shape_mode = ShapeMode.CENTER
        # TODO: draw a white circle outline in self's center position
        engine.draw_circle(self.center_x, self.center_y, self.radius, 1)

        # TODO: loop over all atom_parts in the collection and display them (composition)
