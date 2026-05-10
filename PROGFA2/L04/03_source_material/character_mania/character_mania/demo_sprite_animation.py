#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2/21/2025

@author: pinke
"""
import random

import dae_progfa_lib as pfe
from dae_progfa_lib import ShapeMode, MouseButton
from dae_progfa_lib import MouseButton
import math
from pygame.math import Vector2
# TODO 0: import given class
from sprite_animation import SpriteAnimation

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 600)

# Set the frame rate to x frames per second:
engine.set_fps(60)

# TODO 1: Create the instance
sprite_sheet = engine.load_image("Resources/fantasy_dreamland/Char_001.png")
animated_sprite = SpriteAnimation(sprite_sheet)

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
    # TODO 2: Draw the instance
    animated_sprite.display(engine.width / 2, engine.height / 2)
    pass


def evaluate():
    """
    This function is being executed over and over, as fast as the frame rate. Use to update (not draw).
    """
    # TODO 3: Animate (walking)
    animated_sprite.walk()
    pass


def mouse_pressed_event(mouse_x: int, mouse_y: int, mouse_button: MouseButton):
    """
    This function is only executed once each time a mouse button was pressed!
    """
    # TODO 4: Change directions (here: goes to next direction each time, down->left->right->up)
    animated_sprite.row += 1
    if animated_sprite.row > 3:
        animated_sprite.row = 0
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
