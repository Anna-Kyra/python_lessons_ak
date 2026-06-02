from dae_progfa_lib import ProgfaEngine, ShapeMode
from dae_progfa_lib.progfa_image import ProgfaImage
import numpy as np
from pathlib import Path
import csv

from map import Map


class Player:
    def __init__(self, map: Map, theme: str, map_dir : str, engine : ProgfaEngine):
        """"
        :param theme: chose either day_them or night_theme
        :param map_dir: chose either center, right, left, top, bottom
        """
        self.engine = engine
        self.map = map
        #placement
        self.x = engine.width/2
        self.y = engine.height/2
        #movement
        self.speed_x = 0
        self.speed_y = 0
        self.direction = 0

        if theme == "GameTheme.DAY":
            self.theme = "day_theme"
        elif theme == "GameTheme.NIGHT":
            self.theme = "night_theme"

        print(self.theme)
        self.size = 100

        #Spritesheet
        spritesheet_path = f"resources/{self.theme}/charakter_spritesheet.png"
        spritesheet : ProgfaImage
        spritesheet = engine.load_image(spritesheet_path)
        self.spritesheet_columns = 8
        spritesheet_rows = 24
        spritesheet.resize(self.spritesheet_columns * self.size, spritesheet_rows * self.size)
        spritesheet_frames = spritesheet.cut_all_frames(spritesheet_rows, self.spritesheet_columns)
        ##movements
        self.idle_front = spritesheet_frames[0:self.spritesheet_columns:1]
        self.idle_up = spritesheet_frames[self.spritesheet_columns:self.spritesheet_columns*2:1]
        self.idle_right = spritesheet_frames[self.spritesheet_columns*2:self.spritesheet_columns*3:1]
        self.idle_left = spritesheet_frames[self.spritesheet_columns*3:self.spritesheet_columns*4:1]
        self.move_down = spritesheet_frames[self.spritesheet_columns*4:self.spritesheet_columns*5:1]
        self.move_up = spritesheet_frames[self.spritesheet_columns*5:self.spritesheet_columns*6:1]
        self.move_right = spritesheet_frames[self.spritesheet_columns*6:self.spritesheet_columns*7:1]
        self.move_left = spritesheet_frames[self.spritesheet_columns*7:self.spritesheet_columns*8:1]

        self.current_pose = self.idle_front
        self.frame_counter = 0

        self.window_frame_counter = 0

    def display(self):
        """

        :param engine:
        :return:
        """
        self.engine.shape_mode = ShapeMode.CENTER
        self.engine.color = 0, 0, 0
        self.engine.shape_mode = ShapeMode.CENTER
        self.current_pose[self.frame_counter].draw(self.x, self.y)


        if self.direction == "RIGHT":
            self.current_pose = self.idle_right
        elif self.direction == "LEFT":
            self.current_pose = self.idle_left
        elif self.direction == "UP":
            self.current_pose = self.idle_up
        else:
            self.current_pose = self.idle_front


        self._check_hitbox()
        pass

    def animate(self):
        self.window_frame_counter += 1
        if self.window_frame_counter > 3:
            self.window_frame_counter = 0
            self.frame_counter += 1
            if self.frame_counter >= self.spritesheet_columns:
                self.frame_counter = 0
        pass

    def move(self, key : str):
        self.speed_x = 0
        self.speed_y = 0


        if key in ("RIGHT", "d"):
            self.current_pose = self.move_right
            self.direction = "RIGHT"
            # self.speed_x = 5
            next_x = self.x + 5
            next_y = self.y

            col = int(next_x // self.map.CELL_SIZE)
            row = int(next_y // self.map.CELL_SIZE)

            if row < 0 or row >= self.map.num_rows or col < 0 or col >= self.map.num_cols:
                return
            if self.map.walk_grid[row][col] == 0:
                self.speed_x = 5
            else:
                self.speed_x = 0

        elif key == "LEFT" or key == "a":
            self.current_pose = self.move_left
            self.direction = "LEFT"
            self.speed_x = -5
            next_x = self.x - 5
            next_y = self.y

            col = int(next_x // self.map.CELL_SIZE)
            row = int(next_y // self.map.CELL_SIZE)

            if self.map.walk_grid[row][col] == 0:
                self.speed_x = -5
            else:
                self.speed_x = 0
        elif key == "UP" or key == "w":
            self.current_pose = self.move_up
            self.direction = "UP"
            next_x = self.x
            next_y = self.y - 5

            col = int(next_x // self.map.CELL_SIZE)
            row = int(next_y // self.map.CELL_SIZE)

            if self.map.walk_grid[row][col] == 0:
                self.speed_y = -5
            else:
                self.speed_y = 0
        elif key == "DOWN" or key == "s":
            self.current_pose = self.move_down
            self.direction = "DOWN"
            next_x = self.x
            next_y = self.y + 5

            col = int(next_x // self.map.CELL_SIZE)
            row = int(next_y // self.map.CELL_SIZE)

            if self.map.walk_grid[row][col] == 0:
                self.speed_y = 5
            else:
                self.speed_y = 0
        print("player map:", self.map.map)

        self.x += self.speed_x
        self.y += self.speed_y
        self.current_pose[self.frame_counter].draw(self.x, self.y)




    def collision(self, object_x, object_y, object_width, object_height):
        self._check_hitbox()
        self.engine.shape_mode = ShapeMode.CENTER
        on_checkbox = self.engine.colliding_rects(
            object_x,
            object_y,
            object_width,
            object_height,
            self.x-self.hitbox_size/2,
            self.y-self.hitbox_size/2,
            self.hitbox_size,
            self.hitbox_size
        )

        if on_checkbox:
            print("hit")
            self.engine.draw_square(self.x-self.hitbox_size/2,
            self.y-self.hitbox_size/2,
            self.hitbox_size,)
        pass

    def _check_hitbox(self):
        self.engine.shape_mode = ShapeMode.CENTER
        self.hitbox_size = self.size/2
        self.engine.color = 0, 0, 0, 0
        self.engine.outline_color = 0, 0, 1
        # self.engine.draw_square(self.x, self.y, self.hitbox_size, 2)
        pass

    def is_out_of_bounds_left(self) -> bool:
        """
        This function will return True if the x coordinate is out of bounds.
        """
        if self.x <= 0:
            # Check the left if the window
            self.x = self.engine.width - self.size/2

            print("left")
            return True
        else:
            return False

    def is_out_of_bounds_right(self) -> bool:
        """
        This function will return True if the x coordinate is out of bounds.
        """
        if self.x + self.size/4>= self.engine.width:
            # Check the right of the window
            self.x = self.size/4
            print("right")
            return True
        else:
            return False

    def is_out_of_bounds_down(self) -> bool:
        """
        This function will return True if the y coordinate is out of bounds.
        """
        if self.y + self.size/4 > self.engine.height:
            # Check the bottom of the window
            self.y = self.size/4
            print("down")
            return True
        else:
            return False

    def is_out_of_bounds_up(self) -> bool:
        """
        This function will return True if the y coordinate is out of bounds.
        """
        if self.y - self.size/4 < 0:
            # Check the top if the window
            self.y = self.engine.height - self.size/4
            print("up")
            return True
        else:
            return False