#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 3/14/2025

@author: pinke
"""
from contextlib import nullcontext

import dae_progfa_lib as pfe
from dae_progfa_lib import ShapeMode, MouseButton
from dae_progfa_lib import MouseButton
import math
from pygame.math import Vector2

from enum import Enum
import numpy

# Create an instance of ProgfaEngine and set window size (width, height):

num_rows = 5
num_cols = 10
cell_size = 35

# TODO: change window size based on cell size and number of rows / columns
engine = pfe.ProgfaEngine(800, 600)

# Set the frame rate to x frames per second:
engine.set_fps(60)

class PacmanDirection(Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3

pacman_x = 0
pacman_y = 0
pacman_size = cell_size * 0.6
pacman_direction = PacmanDirection.RIGHT

class CellType(Enum):
    EMPTY = 0
    WALL = 1
    PICKUP = 2

grid : numpy.array

def draw_pacman():
    """Draws pacman based on its current direction."""
    angle = 90 * pacman_direction.value
    mouth_size = 55
    mouth_start = angle + mouth_size/2

    engine.color = 1, 0.92, 0.22
    engine.outline_color = None
    engine.shape_mode = ShapeMode.CENTER
    engine.draw_arc(pacman_x + cell_size/2, pacman_y + cell_size/2, pacman_size, pacman_size, mouth_start, mouth_start + 360 - mouth_size)
    pass

def draw_wall(x: float, y: float):
    """Draws a wall (transparent square with blue outline) in position x, y (left, top of a cell)."""
    engine.color = None
    engine.outline_color = 0, 0, 1
    engine.shape_mode = ShapeMode.CORNER

    engine.draw_square(x, y, cell_size)

def draw_pickup(x: float, y: float):
    """Draws a pickup item (yellow circle, no outline) in the center of a cell, based on x, y (left, top of a cell)."""
    engine.color = 1, 1, 0
    engine.outline_color = None
    engine.shape_mode = ShapeMode.CENTER

    engine.draw_circle(x + cell_size / 2, y + cell_size / 2, cell_size / 5)


def init_game_field():
    # TODO: create / fill the grid with random values of 0, 1 or 2
    # TODO: after that, make sure the top left cell is empty (as pacman starts there)
    pass


def render_game_field():
    # TODO: render the grid based on the value (you can use given draw_wall and draw_pickup functions)
    pass


def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    init_game_field()
    pass


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    engine.background_color = 0, 0, 0
    render_game_field()
    draw_pacman()
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

    pass


def key_up_event(key: str):
    """
    This function is only executed once each time a key was released!
    Special keys have more than 1 character, for example ESCAPE, BACKSPACE, ENTER, ...
    """
    global pacman_direction, pacman_x, pacman_y

    # determine the current row and column number that pacman is in
    pac_col = pacman_x // cell_size
    pac_row = pacman_y // cell_size

    # HINT: check theory use case slides for help with this part!
    if key == 'RIGHT':
        pacman_direction = PacmanDirection.RIGHT
        # TODO: increase pacman_x with cell size ONLY IF pacman can go right (no wall, still inside grid).
        #   if pacman could move and there is a pickup in the location it moves to, remove the pickup from the grid (0)

    elif key == 'LEFT':
        pacman_direction = PacmanDirection.LEFT
        # TODO: increase pacman_x with cell size ONLY IF pacman can go left (no wall, still inside grid).
        #   if pacman could move and there is a pickup in the location it moves to, remove the pickup from the grid (0)
    elif key == 'UP':
        pacman_direction = PacmanDirection.UP
        # TODO: increase pacman_x with cell size ONLY IF pacman can go up (no wall, still inside grid).
        #   if pacman could move and there is a pickup in the location it moves to, remove the pickup from the grid (0)
    elif key == 'DOWN':
        pacman_direction = PacmanDirection.DOWN
        # TODO: increase pacman_x with cell size ONLY IF pacman can go down (no wall, still inside grid).
        #   if pacman could move and there is a pickup in the location it moves to, remove the pickup from the grid (0)

    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
