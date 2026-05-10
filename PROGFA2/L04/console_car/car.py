import random

class Car():
    def __init__(self, road_length : int = 100):
        car_options = ['🚗', '🚙', '🚕', '🚓', '🚛', '🛻']
        self.car_symbol = random.choice(car_options)
        self.road_length = road_length
        self.speed = 0

    def __str__(self):
        return f"{"." * (self.road_length - self.speed)}{self.car_symbol}{"." * self.speed}"

    def vroom(self):
        random_int = random.randint(1, 3)
        if self.road_length <= 0:
            self.speed -= random_int
        else:
            self.speed += random_int


