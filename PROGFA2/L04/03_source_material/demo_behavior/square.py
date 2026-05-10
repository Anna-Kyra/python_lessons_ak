class Square:
    def __init__(self, size: float):
        self.size = size
        self.x = 0      # TODO: random location (within bounds!)
        self.y = 0      # TODO: random location (within bounds!)

        self.color = 0, 0.4, 1
        self.speed = 5
        self.velocity_x = 0
        self.velocity_y = 0