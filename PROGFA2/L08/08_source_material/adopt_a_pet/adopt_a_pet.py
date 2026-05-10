#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 3/28/2025

@author: pinke
"""

import dae_progfa_lib as pfe
from dae_progfa_lib import ShapeMode, MouseButton
from dae_progfa_lib import MouseButton
import math
from pygame.math import Vector2
from pet_owner import PetOwner
from pet import Pet

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(900, 500)

# Set the frame rate to x frames per second:
engine.fps = 60


# TODO 1: Create a pet owner called "Jenny", they do not have a pet
#   -> print() Jenny
#   -> display() Jenny in render() on the LEFT SIDE of the window

# TODO 2: Create a pet with a name of your choice (use image located in "Resources/pets/)
#   -> print() the Pet
#   -> display() the Pet in render() on the RIGHT SIDE of the window (hint: window width - width of the pet image)

# TODO 3: Create a PetOwner class in pet_owner.py, make it adopt a pet, then create / print / render it here in the center of the window


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
