#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 10-11-2025

@author: anna-
"""
import random
import dae_progfa_lib as pfe
from dae_progfa_lib import MouseButton, ShapeMode

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 600)

# Set the frame rate to x frames per second:
engine.fps = 60

global center_x, center_y, speed_x, speed_y, size, direction_pacman
global pickup_x, pickup_y, score


def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    initialize_variables()
    pass

def initialize_variables():
    global center_x, center_y, speed_x, speed_y, size, direction_pacman, pickup_x, pickup_y, score
    direction_pacman = 0
    speed_x = 0
    speed_y = 0
    center_x = engine.width/2
    center_y = engine.height/2
    size = 50

    pickup_x = random.randint(0, engine.width)
    pickup_y = random.randint(0, engine.height)

    score = 0

def draw_text():
    global score
    engine.shape_mode = ShapeMode.CORNER
    engine.color = 1, 1, 1
    engine.set_font_size(30)
    engine.draw_text(f"SCORE: {score}", 10, 10)

def draw_pacman(center_x: float, center_y: float, size: float, direction_angle: int):
    """
    Draws pacman on the window. The direction angle determines which side
    they look at.
    :param center_x: x position of pacman
    :param center_y: y position of pacman
    :param size: radius of pacman
    :param direction_angle: the direction angle that pacman draws to (0
    for right, for example) in degrees.
    :return:
    """
    engine.shape_mode = ShapeMode.CENTER
    engine.color = 1, 0.8, 0
    engine.outline_color = None
    start_mouth = direction_angle + 45
    pacman_arc_size = 270
    engine.draw_arc(center_x, center_y, size, size, start_mouth,
    start_mouth + pacman_arc_size)

def draw_pickup(pickup_x: float, pickup_y: float):
    engine.shape_mode = ShapeMode.CENTER
    engine.outline_color = 1, 1, 1
    engine.color = 1, 1, 1
    engine.draw_dot(pickup_x, pickup_y, 4)


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    engine.background_color = 0, 0, 0
    draw_pickup(pickup_x, pickup_y)
    draw_pacman(center_x, center_y, size, direction_pacman)
    draw_text()
    pass


def evaluate():
    """
    This function is being executed over and over, as fast as the frame rate. Use to update (not draw).
    """
    global center_x, center_y
    center_x += speed_x
    center_y += speed_y
    bounce_pacman()
    pickup_change_location()
    pass

def bounce_pacman():
    """
    This function will take care of the bouncing of the ball
    """
    global center_x, center_y, speed_x, speed_y, size, direction_pacman, score
    if is_out_of_bounds_horizontally(center_x, size/2 -50):
        center_x = engine.width / 2
        # direction_pacman += 180
        score -= 10
    if is_out_of_bounds_vertically(center_y, size/2 -50):
        center_y = engine.height / 2
        # direction_pacman += 180
        score -= 10

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

def pickup_change_location():
    global pickup_x, pickup_y, score
    engine.shape_mode = ShapeMode.CENTER
    on_pacman = engine.colliding_point_in_circle(pickup_x, pickup_y, center_x, center_y, size)

    if on_pacman:
        pickup_x = random.randint(0, engine.width)
        pickup_y = random.randint(0, engine.height)

        score += 10

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
    global speed_x, speed_y,direction_pacman

    if key == "RIGHT":
        direction_pacman = 0
        speed_x = 5
        speed_y = 0
    elif key == "LEFT":
        direction_pacman = 180
        speed_x = -5
        speed_y = 0
    elif key == "UP":
        direction_pacman = 270
        speed_x = 0
        speed_y = -5
    elif key == "DOWN":
        direction_pacman = 90
        speed_x = 0
        speed_y = 5

    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
