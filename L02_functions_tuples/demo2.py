#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 6-10-2025

@author: anna-
"""

import dae_progfa_lib as pfe
from dae_progfa_lib import MouseButton, ShapeMode

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 600)

# Set the frame rate to x frames per second:
engine.fps = 60


def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """

    pass

def draw_sun():
    """
    Draws a sun in the middle of the screen
    :return:
    """
    engine.shape_mode = ShapeMode.CENTER
    engine.color = 1, 1, 0
    engine.draw_circle(engine.width/2, engine.height/2, 100, 0)

def draw_background():
    engine.shape_mode = ShapeMode.CORNER
    engine.color = 0, 0, 1
    engine.outline_color = 1, 0, 0
    engine.draw_rectangle(0, 0, engine.width, engine.height, 5)

def draw_mouse_circle():
    engine.color = (1, 1, 1, 0)
    engine.shape_mode = ShapeMode.CENTER
    engine._outline_color = (52, 235, 164)
    engine.draw_circle(engine.mouse_x, engine.mouse_y, 40)

def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    engine.background_color = (0,0,0)
    draw_background()
    draw_sun()
    draw_mouse_circle()



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

    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
