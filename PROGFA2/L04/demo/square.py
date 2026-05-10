import random
from dae_progfa_lib import ProgfaEngine, ShapeMode


class Square():
    def __init__(self, size : float, max_x : int, max_y : int):
        self.size = size
        self.x = random.uniform(0, max_x - size)
        self.y = random.uniform(0, max_y - size)

        self.color = 1, 0, 0
        self.speed = 5
        self.velocity_x = 1
        self.velocity_y = 1

        self.max_x = max_x
        self.max_y = max_y

    def render(self, engine : ProgfaEngine):
        engine.outline_color = self.color
        engine.color = None
        engine.shape_mode = ShapeMode.CORNER
        engine.draw_square(self.x, self.y, self.size, 5)

    def update(self, bounds_right : float, bounds_bottom : float):
        self.x += self.velocity_x * self.speed
        self.y += self.velocity_y * self.speed
        self._keep_in_bounds(bounds_right, bounds_bottom)

    def _keep_in_bounds(self, bounds_right : float, bounds_bottom : float):
        if self.x < 0 or self.x + self.size > bounds_right:
            self.velocity_x *= -1

        if self.y < 0 or self.y + self.size > bounds_bottom:
            self.velocity_y *= -1