#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2-12-2025

@author: anna-
"""

import dae_progfa_lib as pfe
from dae_progfa_lib import MouseButton, ShapeMode
from enum import Enum

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 600)

# Set the frame rate to x frames per second:
engine.fps = 60

class GameState(Enum):
    START = 0
    PLAY = 1
    END = 2

current_state = GameState.START

def start_screen():
    engine.shape_mode = ShapeMode.CORNER
    engine.color = 0, 0, 0

    engine.set_font_size(50)
    engine.draw_text('Moo-ve your fingers', engine.width/2, engine.height/4, True)

    engine.set_font_size(30)
    engine.draw_text('_Press any key to start_', engine.width/2, engine.height*(3/4), True)

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """

    pass


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    if current_state == GameState.START:
        engine.background_color = 1, 0, 1
        start_screen()
    if current_state == GameState.PLAY:
        engine.background_color = 0, 1, 0

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
    global current_state
    if current_state == GameState.START and key:
        current_state = GameState.PLAY

    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
