#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GIVEN:
------
- global variables in capitals to set parameters for window
- list of color options
- SPACE BAR switches show_values mode on/off

=================================================

DEMO (see todo's):
------------------
- fill grid with zero values
- manually change some cell values
- print grid
- display grid (values)
- randomize grid every frame
"""

import dae_progfa_lib as pfe
from dae_progfa_lib import ShapeMode, MouseButton
from dae_progfa_lib import MouseButton
import numpy as np


NUM_ROWS = 5
NUM_COLUMNS = 9
CELL_SIZE = 100

# TODO 0: calculate window size based on cell size and number of rows / cols
# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(NUM_COLUMNS * CELL_SIZE, NUM_ROWS * CELL_SIZE)

# Set the frame rate to x frames per second:
engine.fps = 2

color_list = [
    (0.1, 0.6, 1),  # Electric Blue
    (0.1, 1, 0),    # Neon Green
    (1, 0.2, 0.6),  # Hot Pink
    (1, 1, 0),      # Bright Yellow
    (0.5, 0, 1),    # Purple
    (1, 0.6, 0)     # Bright Orange
]

disco_grid : np.ndarray

show_values = True
# TODO 1: add type indication for numpy array
# disco_grid


def init_disco():
    """
    Fills the entire numpy grid with 0 values, then manually sets these cells to a color code:
    - top left = 1
    - bottom right = 2
    - bottom left = 3
    - top right = 4
    - center = 5
    Finally, the grid is printed to the console.
    """
    # TODO 1a: fill disco grid with values (see docstring)
    # TODO 1b: print grid to console
    global disco_grid
    disco_grid = np.zeros((NUM_ROWS, NUM_COLUMNS), dtype=int)
    disco_grid[0][0] = 1 #top left
    disco_grid[NUM_ROWS-1][NUM_COLUMNS-1] = 5 #bottom right
    print(disco_grid)
    pass


def display_disco():
    """
    Draws disco cells based on the content of the disco grid.
    Each cell is a square with a black outline and a fill according to its color code.
    If show_values is set to True, the actual values are displayed in black.
    """
    engine.outline_color = 0, 0, 0
    # TODO 2a: visualize grid cells + values (see docstring)
    # TODO 2b: change grid cell based on color index (-> color_list)
    num_rows, num_cols = disco_grid.shape
    for row in range(num_rows):
        for col in range(num_cols):
            value = disco_grid[row][col]

            engine.color = color_list[value]
            cell_x = col*CELL_SIZE
            cell_y = row*CELL_SIZE

            engine.draw_square(cell_x, cell_y, CELL_SIZE, 3)

            if show_values:
                engine.color = 0,0,0
                engine.draw_text(str(value), cell_x, cell_y)
    pass


def randomize_disco():
    # TODO 2: make disco tiles random every frame (frame rate is set to 2 fps)
    global disco_grid
    max_color = len(color_list)
    disco_grid = np.random.default_rng().integers(0, max_color, (NUM_ROWS, NUM_COLUMNS))
    print(disco_grid)
    pass


def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    engine.set_font_size(50)
    init_disco()
    randomize_disco()
    pass


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    display_disco()
    pass


def evaluate():
    """
    This function is being executed over and over, as fast as the frame rate. Use to update (not draw).
    """
    randomize_disco()   # TODO 2: disco time!
    pass


def mouse_pressed_event(mouse_x: int, mouse_y: int, mouse_button: MouseButton):
    """
    This function is only executed once each time a mouse button was pressed!
    """
    pass


def key_up_event(key: str):
    """
    This function is only executed once each time a key was released!
    Special keys have more than 1 character, for example ESCAPE, BACKSPACE, ENTER, ...
    """
    if key == ' ':
        global show_values
        show_values = not show_values  # switch showing values on/of
        print(f"Showing values in grid: {show_values}.")
    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
