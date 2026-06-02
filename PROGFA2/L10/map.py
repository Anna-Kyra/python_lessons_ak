from dae_progfa_lib import ProgfaEngine, ShapeMode
import numpy as np
from pathlib import Path
import csv
import random

class Map:
    def __init__(self, theme: str, map_dir : str, engine : ProgfaEngine):
        self.engine = engine
        self.map = map_dir
        print(self.map)

        if theme == "GameTheme.DAY":
            self.theme = "day_theme"
        elif theme == "GameTheme.NIGHT":
            self.theme = "night_theme"

        self._load_csv(self.map)

    def change_map(self, new_map):
        self.map = new_map
        self._load_csv(self.map)
        # print(f"change to: {self.map}")
    def _load_csv(self, map:str):
        #WALK GRID
        self.CELL_SIZE = 600 * 1.5 / 32

        folder = Path("resources/csv_files/walking")

        self.path = Path("resources/csv_files/walking") / f"{map}_map_walk.csv"

        # print(self.path)

        if not self.path.exists():
            print("File not found!")
            return
        # for path in folder.glob(f"{map}_map_walk.csv"):
        #     self.path = path

        self.walk_grid = np.loadtxt(self.path, delimiter=",", dtype=int)
        self.walk_grid[self.walk_grid == 213] = 1
        self.walk_grid[self.walk_grid == -1] = 0

        self.num_rows, self.num_cols = self.walk_grid.shape
        self._draw_csv()

    def _draw_csv(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.engine.shape_mode = ShapeMode.CORNER
                self.value = self.walk_grid[row][col]
                cell_x = col * self.CELL_SIZE
                cell_y = row * self.CELL_SIZE

                self.engine.color = 0, 0, 0, 0
                self.engine.outline_color = 1, 0, 1
                self.engine.draw_square(cell_x, cell_y, self.CELL_SIZE, 1)

                self.engine.color = 0, 0, 0
                self.engine.draw_text(str(self.value), cell_x, cell_y)

    def get_random_walkable_tile(self):
        valid_tiles = []

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.walk_grid[row][col] == 0:
                    valid_tiles.append((row, col))

        return random.choice(valid_tiles)

    def display(self):
        self._draw_csv()