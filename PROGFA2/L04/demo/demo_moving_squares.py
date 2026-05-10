#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 3-3-2026

@author: anna-
"""

import dae_progfa_lib as pfe
from dae_progfa_lib import MouseButton
from square import Square

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 600)

# Set the frame rate to x frames per second:
engine.fps = 60

img_bg = engine.load_image("resources/background.jpg")

my_square = Square(40, engine.width, engine.height)
my_greenSquare = Square(60, engine.width, engine.height)
my_greenSquare.color = 0, 1, 0

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
    my_square.render(engine)
    my_greenSquare.render(engine)

def evaluate():
    """
    This function is being executed over and over, as fast as the frame rate. Use to update (not draw).
    """
    my_square.update(engine.width, engine.height)
    my_greenSquare.update(engine.width, engine.height)

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
