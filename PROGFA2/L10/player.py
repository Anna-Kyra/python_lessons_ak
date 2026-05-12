from dae_progfa_lib import ProgfaEngine

class Player:
    def __init__(self, engine : ProgfaEngine):
        self.center_x = engine.width/2
        self.center_y = engine.height/2
        self.speed_x = 0
        self.speed_y = 0
        self.direction = 0

        self.size = 100

    def display(self, engine : ProgfaEngine):
        engine.color = 0, 0, 0
        engine.draw_square(self.center_x, self.center_y, self.size, 0)
        pass

    def move(self, key):
        self.center_x += self.speed_x
        self.center_y += self.speed_y

        if key == "RIGHT":
            self.direction = 0
            self.speed_x = 5
            self.speed_y = 0
        elif key == "LEFT":
            self.direction = 180
            self.speed_x = -5
            self.speed_y = 0
        elif key == "UP":
            self.direction = 270
            self.speed_x = 0
            self.speed_y = -5
        elif key == "DOWN":
            self.direction = 90
            self.speed_x = 0
            self.speed_y = 5
        pass

    def _is_out_of_bounds_horizontally(self, engine: ProgfaEngine) -> bool:
        """
        This function will return True if the x coordinate is out of bounds.
        """
        if self.center_x - self.size < 0:
            # Check the left if the window
            return True
        elif self.center_x + self.size > engine.width:
            # Check the right of the window
            return True
        else:
            return False

    def _is_out_of_bounds_vertically(self, engine: ProgfaEngine) -> bool:
        """
        This function will return True if the y coordinate is out of bounds.
        """
        if self.center_y - self.size < 0:
            # Check the left if the window
            return True
        elif self.center_y + self.size > engine.height:
            # Check the right of the window
            return True
        else:
            return False