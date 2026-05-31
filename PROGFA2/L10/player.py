from dae_progfa_lib import ProgfaEngine, ShapeMode
from dae_progfa_lib.progfa_image import ProgfaImage
import numpy as np
from pathlib import Path
import csv

class Player:
    def __init__(self, theme: str, map_dir : str, engine : ProgfaEngine):
        """"
        :param theme: chose either day_them or night_theme
        :param map_dir: chose either center, right, left, top, bottom
        """
        #placement
        self.x = engine.width/2
        self.y = engine.height/2
        #movement
        self.speed_x = 0
        self.speed_y = 0
        self.direction = 0

        self.map = map_dir
        print(self.map)

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
        self._load_csv(engine)


    def display(self, engine : ProgfaEngine):
        """

        :param engine:
        :return:
        """
        engine.shape_mode = ShapeMode.CENTER
        engine.color = 0, 0, 0
        # engine.draw_rectangle(self.x, self.y, self.size / 2, self.size / 2)
        # engine.draw_square(self.x, self.y, self.size, 0)
        self._draw_csv(engine)
        engine.shape_mode = ShapeMode.CENTER
        self.current_pose[self.frame_counter].draw(self.x, self.y)


        if self.direction == "RIGHT":
            self.current_pose = self.idle_right
        elif self.direction == "LEFT":
            self.current_pose = self.idle_left
        elif self.direction == "UP":
            self.current_pose = self.idle_up
        else:
            self.current_pose = self.idle_front


        self._check_hitbox(engine)
        pass

    def animate(self):
        self.window_frame_counter += 1
        if self.window_frame_counter > 15:
            self.window_frame_counter = 0
            self.frame_counter += 1
            if self.frame_counter >= self.spritesheet_columns:
                self.frame_counter = 0
        pass

    def move(self, key : str, engine : ProgfaEngine):
        self.speed_x = 0
        self.speed_y = 0

        if key == "RIGHT" or key == "d":
            self.current_pose = self.move_right
            self.direction = "RIGHT"
            self.speed_x = 3
        elif key == "LEFT" or key == "a":
            self.current_pose = self.move_left
            self.direction = "LEFT"
            self.speed_x = -3
        elif key == "UP" or key == "w":
            self.current_pose = self.move_up
            self.direction = "UP"
            self.speed_y = -3
        elif key == "DOWN" or key == "s":
            self.current_pose = self.move_down
            self.direction = "DOWN"
            self.speed_y = 3


        self.x += self.speed_x
        self.y += self.speed_y
        self.current_pose[self.frame_counter].draw(self.x, self.y)


    def _load_csv(self, engine : ProgfaEngine):
        #WALK GRID
        walk_grid : np.ndarray
        self.CELL_SIZE = 600/32
        self.path: Path
        self.path = "resources/csv_files/walking"
        for path in Path(self.path).glob(f"{self.map}*"):
            self.path = path
            # with self.path.open("r") as file:
            #     reader = csv.DictReader(file)
            #     print(reader)
            print(self.path)

    def _draw_csv(self, engine : ProgfaEngine):
        walk_grid = np.loadtxt(self.path, delimiter=",", dtype=int)
        # print(walk_grid)
        num_rows, num_cols = walk_grid.shape
        # print(num_rows, num_cols)
        for row in range(num_rows):
            for col in range(num_cols):
                engine.shape_mode = ShapeMode.CORNER
                value = walk_grid[row][col]
                cell_x = col * self.CELL_SIZE
                cell_y = row * self.CELL_SIZE

                if value == 213:
                    value = 1
                elif value == -1:
                    value = 0
                engine.color = 0, 0, 0, 0
                engine.outline_color = 1, 0, 1
                engine.draw_square(cell_x, cell_y, self.CELL_SIZE, 1)

                engine.color = 0, 0, 0
                engine.draw_text(str(value), cell_x, cell_y)

    def _collision(self, engine):

        pass

    def _check_hitbox(self, engine : ProgfaEngine):
        # on_checkbox = engine.colliding_point_in_rect(mouse_x, mouse_y, self.x, self.y, self.size/2, self.size/2)
        engine.shape_mode = ShapeMode.CENTER
        engine.color = 0, 0, 0, 0
        engine.outline_color = 0, 0, 1
        engine.draw_square(self.x, self.y, self.size/2, 2)
        pass

    def is_out_of_bounds_left(self, engine: ProgfaEngine) -> bool:
        """
        This function will return True if the x coordinate is out of bounds.
        """
        if self.x - self.size/4 < 0:
            # Check the left if the window
            self.x = engine.width - self.size/4
            print("left")
            return True
        else:
            return False

    def is_out_of_bounds_right(self, engine: ProgfaEngine) -> bool:
        """
        This function will return True if the x coordinate is out of bounds.
        """
        if self.x >= engine.width:
            # Check the right of the window
            self.x = self.size/4
            print("right")
            return True
        else:
            return False

    def is_out_of_bounds_down(self, engine: ProgfaEngine) -> bool:
        """
        This function will return True if the y coordinate is out of bounds.
        """
        if self.y + self.size/4 > engine.height:
            # Check the bottom of the window
            self.y = self.size/4
            print("down")
            return True
        else:
            return False

    def is_out_of_bounds_up(self, engine: ProgfaEngine) -> bool:
        """
        This function will return True if the y coordinate is out of bounds.
        """
        if self.y - self.size/4 < 0:
            # Check the top if the window
            self.y = engine.height - self.size/4
            print("up")
            return True
        else:
            return False