from typing import Tuple, List

import numpy as np
from dae_progfa_lib import ProgfaEngine, ShapeMode
from pygame.gfxdraw import pixel


class PixelArt:
    def __init__(self, name: str,
                 colors: List[Tuple[float,float,float]],
                 pixel_grid,
                 pixel_size: int,
                 transparent: bool = True):
        """
        :param name: preferred name for the pixel art
        :param colors:
        :param pixel_grid:
        :param pixel_size:
        :param transparent:
        """
        self.name = name
        self.color_list = colors
        self.pixel_size = pixel_size
        self.transparent = transparent

        self.pixel_grid = pixel_grid
        num_rows, num_columns = pixel_grid.shape
        self.num_rows = num_rows     # TODO: count number of rows in pixel grid
        self.num_columns = num_columns  # TODO: count number of columns in pixel grid

    def __str__(self):
        print(self.color_list)
        print(self.pixel_grid)
        # TODO: print pixel grid
        return "test"

    def width(self) -> float:
        return self.pixel_size * self.num_columns

    def height(self) -> float:
        return self.pixel_size * self.num_rows

    def flip_horizontal(self):
        # TODO: flip the pixel grid horizontally
        self.pixel_grid = np.flip(self.pixel_grid, axis=1)
        pass

    def flip_vertical(self):
        # TODO: flip the pixel grid vertically
        self.pixel_grid = np.flip(self.pixel_grid, axis=0)
        pass

    def rotate(self):
        # TODO: rotate the grid 90 degrees clockwise
        self.pixel_grid = np.rot90(self.pixel_grid, k=-1)
        # rows become columns!
        self.num_rows, self.num_columns = self.num_columns, self.num_rows

    def render(self, engine: ProgfaEngine, x_pos: float, y_pos: float):
        # TODO: loop over the pixel grid
        #   -> draw a square in the color according to the color code in the grid cell (no outline)
        #   -> if transparent mode (see attributes) is set to True, cells with value 0 are NOT drawn
        for row in range(self.num_rows):
            for column in range(self.num_columns):
                value = self.pixel_grid[row][column]
                # print(value)

                engine.color = self.color_list[value]

                cell_x = column * self.pixel_size
                cell_y = row * self.pixel_size

                engine.draw_square(cell_x, cell_y, self.pixel_size, 3)

        engine.outline_color = None
        engine.shape_mode = ShapeMode.CORNER

