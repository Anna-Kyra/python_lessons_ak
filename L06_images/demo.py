#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 10-11-2025

@author: anna-
"""

import dae_progfa_lib as pfe
from dae_progfa_lib import MouseButton

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 600)

# Set the frame rate to x frames per second:
engine.fps = 60

img_background = engine.load_image("Resources/demo/RetroComic.png")
# img_background.resize(engine.width, engine.height, False)

text = "POW!!"

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    print(f"width= {img_background.width} height= {img_background.height}")

    pass


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    # img_background.draw(0, 0)
    img_background.draw_fixed_size(0, 0, engine.width, engine.height, False)

    #FONT
    engine.set_font("Resources/demo/CrashLandingBB.ttf", 200)
    #Shadow
    engine.color = 0, 0, 0
    offset = 10
    engine.draw_text(text, engine.width/2 + offset, engine.height/2 + offset, True)
    #Text
    engine.color = 1, 0, 0
    engine.draw_text(text, engine.width / 2, engine.height / 2, True)
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

    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
