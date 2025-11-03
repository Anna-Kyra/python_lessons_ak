#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 3-11-2025

@author: anna-
"""
import random
import string

import dae_progfa_lib as pfe
from dae_progfa_lib import MouseButton, ShapeMode

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 600)

# Set the frame rate to x frames per second:
engine.fps = 60

global center_x, center_y
global speed_x, speed_y
global size
global text_placeholder


def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    initialize_variables()
    pass

def initialize_variables():
    global center_x, center_y, speed_x, speed_y, size, text_placeholder
    center_x = engine.width / 2
    center_y = engine.height / 2
    speed_x = random.randint(-2, 3)
    speed_y = random.randint(-2, 3)
    size = 100
    text_placeholder = ""

def draw_ball(center_x: int, center_y: int, size: int):
    """
    This function draws a ball at a certain location
    :param center_x: x coordinate of center
    :param center_y: y coordinate of center
    :param size: size of ball
    :return:
    """

    engine.shape_mode = ShapeMode.CENTER
    engine.color = 1, 0, 1
    engine.draw_circle(center_x, center_y, size, 0)

    #On the ball, place the text
    engine.color = 1, 1, 1
    engine.draw_text(text_placeholder, center_x, center_y)


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    global center_x, center_y, size
    engine.background_color = 0, 0, 0
    draw_ball(center_x, center_y, size)

    pass


def evaluate():
    """
    This function is being executed over and over, as fast as the frame rate. Use to update (not draw).
    """
    move_ball()
    bounce_ball()
    pass

def move_ball():
    global center_x, center_y, speed_x, speed_y
    center_x += speed_x
    center_y += speed_y

def bounce_ball():
    """
    This function will take care of the bouncing of the ball
    """
    global center_x, center_y, speed_x, speed_y, size
    if is_out_of_bounds_horizontally(center_x, size/2):
        speed_x *= -1
    if is_out_of_bounds_vertically(center_y, size/2):
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
    global text_placeholder, speed_x
    allowed_characters = set(string.ascii_letters)

    if key == "ENTER":
        initialize_variables()
    elif key in allowed_characters:
        text_placeholder += key
        print(text_placeholder)
    elif key == "BACKSPACE":
        text_placeholder = text_placeholder[:-1]
    elif key == "UP":
        if speed_x > 0:
            speed_x -= 10
        elif speed_x < 0:
            speed_x += 10
    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
