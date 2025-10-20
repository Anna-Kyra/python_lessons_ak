#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 20-10-2025

@author: anna-
"""

import dae_progfa_lib as pfe
from dae_progfa_lib import MouseButton, ShapeMode
import random

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 600)

# Set the frame rate to x frames per second:
engine.fps = 60


def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """

    pass

def draw_angry(x: float, y: float, diameter: float, color: tuple, mouth_x, mouth_y):
    engine.color = color
    engine.draw_circle(x, y, diameter, 0)
    engine.color = 0, 0, 0
    engine.draw_circle(mouth_x, mouth_y, 40, 0)
    pass


def draw_kid():
    color = 1, 0, 0
    engine.shape_mode = ShapeMode.CENTER
    center_x = engine.width / 2
    center_y = engine.height / 2
    mouth_x = center_x
    mouth_y = center_y + 50
    diameter = 200
    # engine.draw_circle(center_x, center_y, diameter, 0)
    draw_angry(center_x, center_y, diameter, color, mouth_x, mouth_y)

    mouse_in_face = engine.colliding_point_in_circle(engine.mouse_x, engine.mouse_y, center_x, center_y, diameter)
    mouse_in_mouth = engine.colliding_point_in_circle(engine.mouse_x, engine.mouse_y, mouth_x, mouth_y, 40)

    if not mouse_in_face: # MUIS NIET IN GEZICHT
        draw_angry(center_x, center_y, diameter, color, 0, 0)
    elif mouse_in_mouth: # MUIS IN MOND
        color = 0, 1, 0
        draw_angry(center_x, center_y, diameter, color, mouth_x, mouth_y)
    else: # ALLE ANDERE GEVALLEN (LEES: MUIS WEL IN GEZICHT, NIET MOND)
        color = 1, 1, 0
        draw_angry(center_x, center_y, diameter, color, 0, 0)


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    draw_kid()

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
    print(f"x={mouse_x} y={mouse_y}")
    if mouse_button == MouseButton.LEFT:
        engine.background_color = 1, 1, 1
    else:
        engine.background_color = 0, 0, 0


def key_up_event(key: str):
    """
    This function is only executed once each time a key was released!
    Special keys have more than 1 character, for example ESCAPE, BACKSPACE, ENTER, ...
    """
    if key == 'r' or key == 'R':
        r = random.randint(0, 255) / 255
        g = random.randint(0, 255) / 255
        b = random.randint(0, 255) / 255
        # random.uniform(0, 1)
        engine.background_color = r, g, b

    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
