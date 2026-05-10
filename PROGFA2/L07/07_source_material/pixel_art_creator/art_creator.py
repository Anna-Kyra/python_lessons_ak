#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 3/12/2025

@author: pinke
"""
import random
from os import mkdir
from time import sleep

import dae_progfa_lib as pfe
from dae_progfa_lib import ShapeMode, MouseButton
from dae_progfa_lib import MouseButton
import math
from pygame.math import Vector2

from typing import List
from pathlib import Path
import numpy

CELL_SIZE = 20
NUM_COLUMNS = 18
NUM_ROWS = 21

# TODO: list the colors you want to use in your pixel art
colors = [
    (1, 1, 1, 0),     # white
    (0.2, 0.2, 0.2),  # gray
    (0.2, 0.6, 0.2),  # green
    (0.8, 0.2, 0.2),  # red
    (0.2, 0.2, 0.8),  # blue
]
current_color = 1
show_values = True

# Create an instance of ProgfaEngine and set window size (width, height):
# TODO: change engine size based on cell size and number of rows / columns:
engine = pfe.ProgfaEngine(800, 600)

# Set the frame rate to x frames per second:
engine.set_fps(60)

# TODO: create a numpy grid full of zero values based on the number of rows and columns


def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """

    pass


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    engine.background_color = 1, 1, 1
    # TODO: Create/call function to render numpy grid (squares with black outline and fill based on grid value)
    pass


def evaluate():
    """
    This function is being executed over and over, as fast as the frame rate. Use to update (not draw).
    """
    if engine.mouse_pressed:
        # Check the row/col that the mouse cursor is currently in:
        row = engine.mouse_y // CELL_SIZE
        col = engine.mouse_x // CELL_SIZE

        # TODO on LEFT mouse button: save the current_color in the cell that was clicked
        # TODO on RIGHT mouse button: reset the color (value = 0) in the cell that was clicked

    pass


def mouse_pressed_event(mouse_x: int, mouse_y: int, mouse_button: MouseButton):
    """
    This function is only executed once each time a mouse button was pressed!
    """
    # Check the row/col that the mouse cursor is currently in:
    row = mouse_y // CELL_SIZE
    col = mouse_x // CELL_SIZE
    print(f"User clicked in row {row}, col {col}.")
    pass


def key_up_event(key: str):
    """
    This function is only executed once each time a key was released!
    Special keys have more than 1 character, for example ESCAPE, BACKSPACE, ENTER, ...
    """
    if key == 'ENTER':
        rnd = random.randint(0, 10000)
        dir_name = f"pixel_art_{rnd}"
        save_path = Path(dir_name)
        # TODO: create save path IF it does not exist yet
        # TODO: save the numpy grid to a pixels.csv file (on line of code!) in this path
        #   -> HINT: only one line of code! (see theory)
        # TODO: save the list of colors to a colors.csv file:
        #   -> HINT: we have a List now; no numpy grid! This means we need to write line by line (see theory topic 04)
        #   -> write a title row r,g,b
        #   -> next, write each color as r,g,b to a new line in hte file


    if key == ' ':
        # switch show values in grid state:
        global show_values
        show_values = not show_values
    elif key.isnumeric():
        # switch current color based on key that was pressed:
        number = int(key)
        if number < len(colors):  # check if valid color index for colors list
            global current_color
            current_color = number

    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
