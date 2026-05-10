import random


class NeonArc():
    class Shape(Enum):
        MOON = 0,
        CAKE = 1,
        RIBBON = 2
    def __init__(self, size : float, shape_type : str, max_x : int, max_y : int):
        self.size = size
        self.shape_type = shape_type

        self.x = random.uniform(0, max_x - size)
        self.y = random.uniform(0, max_y - size)

        self.angle = random.uniform(0, 360)

    # def _keep_in_bounds(self, bounds_right : float, bounds_bottom : float):
    #     if self.x < 0 or self.x + self.size > bounds_right:
    #
    #     if self.y < 0 or self.y + self.size > bounds_bottom:
