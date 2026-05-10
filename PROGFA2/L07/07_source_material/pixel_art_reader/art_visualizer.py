#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 3/12/2025

@author: pinke
"""
import csv

import dae_progfa_lib as pfe
import numpy
from dae_progfa_lib import ShapeMode, MouseButton
from dae_progfa_lib import MouseButton
import math
from pygame.math import Vector2
from typing import List, Tuple
from pathlib import Path
from csv import DictReader
from pixel_art import PixelArt
import random
import numpy as np

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(1000, 800)

# Set the frame rate to x frames per second:
# engine.set_fps(60)

# grid_color = np.loadtxt("art/mew/colors.csv", delimiter=",", dtype=int)
# num_rows, num_cols = grid_color.shape

# grid = PixelArt(grid_color, grid_color.shape, 10)
path = "art"
for path in Path(path).glob("*"):
    path = path
    def load_colors(csv_file: Path) -> List[Tuple[float, float, float]]:
        colors = []

        path = Path(csv_file / "colors.csv")

        with path.open("r") as file:
            reader = csv.DictReader(file)
            # print(reader.fieldnames)
            for row in reader:
                r = float(row["r"])
                g = float(row["g"])
                b = float(row["b"])

                color = (r, g ,b)
                colors.append(color)


        # print(colors)
        return colors

    clrs = load_colors(path)
    print(clrs)

    grid_path = path / "pixels.csv"

    grid_mew_path = np.loadtxt(grid_path, delimiter=",", dtype=int)

    grid_mew = PixelArt("mew", load_colors(path), grid_mew_path, 10)

    print(grid_mew)


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
    grid_mew.render(engine, 1, 1)
    pass


def evaluate():
    """
    This function is being executed over and over, as fast as the frame rate. Use to update (not draw).
    """

    pass


def mouse_pressed_event(mouse_x: int, mouse_y: int, mouse_button: MouseButton):
    """
    This function is only executed once each time a mouse button was pressed!
    """
    # TODO: flip (all) artwork(s):
    #   -> horizontally on left mouse button
    #   -> vertically on right mouse button

    pass


def key_up_event(key: str):
    """
    This function is only executed once each time a key was released!
    Special keys have more than 1 character, for example ESCAPE, BACKSPACE, ENTER, ...
    """
    # TODO: UP key increases pixel_size of (all) artwork(s) with 1
    # TODO: DOWN key decreases pixel_size of (all) artwork(s) with 1, but minimum size is 1
    # TODO: r key rotates (all) artwork(s) with 90 degreens
    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
