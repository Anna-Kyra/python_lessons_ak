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

# GAME STATE
class GameState(Enum):
    INTRO = 0,
    GAMEPLAY = 1,
    GAMEOVER = 2,
    HIGHSCORE = 3
current_state = GameState.INTRO

# SPAWNING WORDS
# word_list =

def start_screen():
    engine.shape_mode = ShapeMode.CORNER
    engine.color = 0, 0, 0

    engine.set_font_size(50)
    engine.draw_text('Moo-ve your fingers', engine.width/2, engine.height/4, True)

    engine.set_font_size(30)
    engine.draw_text('_Press any key to play_', engine.width/2, engine.height*(3/4), True)

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """

    pass

def draw_words():
    pass

def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    if current_state == GameState.INTRO:
        engine.background_color = 1, 0, 1
        start_screen()
    elif current_state == GameState.GAMEPLAY:
        engine.background_color = 0, 1, 1
        draw_words()
    elif current_state == GameState.GAMEOVER:
        engine.background_color = 1, 0, 0
        engine.shape_mode = ShapeMode.CENTER
        engine.draw_text("GAMEOVER", engine.width/2, engine.height/2, True)
    elif current_state == GameState.HIGHSCORE:
        engine.background_color = 0, 1, 0
        engine.draw_text("HIGHSCORE", engine.width/2, engine.height/2, True)
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
    if current_state == GameState.INTRO and key:
        current_state = GameState.GAMEPLAY

    # DEBUG
    if key == "1":
        current_state = GameState.INTRO
    elif key == "2":
        current_state = GameState.GAMEPLAY
    elif key == "3":
        current_state = GameState.GAMEOVER
    elif key == "4":
        current_state = GameState.HIGHSCORE

    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
