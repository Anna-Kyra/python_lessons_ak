#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 9-11-2025

@author: anna-
"""

import dae_progfa_lib as pfe
from dae_progfa_lib import MouseButton, ShapeMode

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 800)

# Set the frame rate to x frames per second:
engine.fps = 60

global center_x, center_y, center_a, center_b
global speed_x, speed_y
global size
global outline


def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    initialize_variables()

    pass

def initialize_variables():
    global center_x, center_y, center_a, center_b, speed_x, speed_y, size, outline
    size = engine.width/4
    center_x = engine.width/2
    center_b = engine.width/2
    center_y = engine.height/2
    center_a = engine.height/2
    speed_x = 2
    speed_y = 2
    outline = 3
    pass

def draw_ball(center_x: float, center_y: float, color: tuple):
    engine.shape_mode = ShapeMode.CENTER
    engine.color = color
    engine.outline_color = 0, 0, 0
    engine.draw_circle(center_x, center_y, size, outline)
    pass

def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    global center_x, center_y, speed_x, speed_y
    engine.background_color = 1, 1, 1
    draw_ball(engine.width/2, center_y, (0, 1, 1, 0.5))
    draw_ball(engine.width/2, center_a, (1, 1, 1, 0.5))
    draw_ball(center_b, engine.height/2, (1, 0, 1, 0.5))
    draw_ball(center_x, engine.height/2, (1, 1, 0, 0.5))
    pass

def evaluate():
    """
    This function is being executed over and over, as fast as the frame rate. Use to update (not draw).
    """
    move_ball()
    bounce_ball()
    pass

def move_ball():
    global center_x, center_y, center_a, center_b, speed_y, speed_x
    center_y += speed_y
    center_a -= speed_y
    center_x += speed_x
    center_b -= speed_x
    pass

def bounce_ball():
    """
    This function will take care of the bouncing of the ball
    """
    global center_x, center_y, speed_x, speed_y
    if is_out_of_bounds_horizontally(center_x, size/2 - size - outline):
        speed_x *= -1
    if is_out_of_bounds_vertically(center_y, size/2 - size - outline):
        speed_y *= -1

def is_out_of_bounds_horizontally(x: int, size: int) -> bool:
    """
    This function will return True if the x coordinate is out of bounds.
    :param x: x coordinate of ball
    :param size: size of ball
    :return: True or False
    """
    if x - size < 0:
        # Check the left if the window
        return True
    elif x + size > engine.width:
        #Check the right of the window
        return True
    else:
        return False

def is_out_of_bounds_vertically(y: int, size: int) -> bool:
    """
    This function will return True if the y coordinate is out of bounds.
    :param y: y coordinate of ball
    :param size: size of ball
    :return: True or False
    """
    if y - size < 0:
        # Check the left if the window
        return True
    elif y + size > engine.height:
        #Check the right of the window
        return True
    else:
        return False

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

    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
