from dae_progfa_lib import ProgfaEngine
from enum import Enum

class Chicken:
    class Activity(Enum):
        IDLE = 0
        BLINK = 1
        LOOK_RIGHT = 4
        WALK_1 = 5
        STARE = 6
        WALK_2 = 7

    def __init__(self, engine: ProgfaEngine):
        spritesheet = engine.load_image('Resources/Free Chicken Sprites.png')
        self.sprites = spritesheet.cut_all_frames(2, 4)
        self.current_activity = Chicken.Activity.IDLE

    def display(self, x: float, y: float):
        """
        Draws the current frame of the chicken spritesheet,
        according to the current activity.
        :param x: x position to draw the frame in.
        :param y: y position to draw the frame in.
        """
        frame_number = self.current_activity.value
        self.sprites[frame_number].draw(x, y)
