#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2/21/2025

@author: pinke
"""
import dae_progfa_lib as pfe
from dae_progfa_lib import ShapeMode, MouseButton
from dae_progfa_lib import MouseButton


# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 450)

# Set the frame rate to x frames per second:
engine.set_fps(60)

img_bg = engine.load_image("Resources/background.jpg")
img_bg.resize(engine.width, engine.height)


def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """

    pass


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    img_bg.draw(0, 0)

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


def key_down_event(key: str):
    """
    This function is only executed once each time a key goes down.
    Special keys have more than 1 character, for example ESCAPE, BACKSPACE, ENTER, ...
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
engine._key_down_event = key_down_event

# Start the game loop:
engine.play()
