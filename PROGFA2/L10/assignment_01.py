#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 10-5-2026

@author: anna-
"""

import dae_progfa_lib as pfe
from dae_progfa_lib import MouseButton, ShapeMode
from enum import Enum

from player import Player

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 600)

# Set the frame rate to x frames per second:
engine.fps = 60

# GAME STATE
class GameState(Enum):
    START = 0,
    THEME = 1,
    GAMEPLAY = 2,
    END_SCREEN = 3,
current_state = GameState.START

# GAME MAP
class GameMap(Enum):
    CENTER = 0,
    RIGHT = 1,
    BOTTOM = 2,
    LEFT = 3,
    UP = 4,
current_map = GameMap.CENTER

# GAME THEME
class GameTheme(Enum):
    DAY = 0,
    NIGHT = 1,
current_theme = GameTheme.DAY

def load_level():
    pass

# SCREENS
def start_screen():
    engine.background_color = 1, 0, 1
    engine.shape_mode = ShapeMode.CORNER
    engine.color = 0, 0, 0

    engine.set_font_size(50)
    engine.draw_text("Sprout's Party", engine.width/2, engine.height/4, True)

    engine.set_font_size(30)
    engine.draw_text('_Press any key to play_', engine.width/2, engine.height*(3/4), True)

def theme_screen():
    engine.background_color = 1, 1, 0
    engine.draw_text("CHOOSE THEME", engine.width / 2, 50, True)
    engine.color = 0, 0, 0

    engine.draw_rectangle(engine.width / 2 - 310, 100, 300, engine.height - 200)
    engine.draw_rectangle(engine.width / 2 + 10, 100, 300, engine.height - 200)

def draw_player():
    engine.color = 0, 0, 0
    engine.draw_rectangle(engine.width / 2, engine.height / 2, 100, 100)

def gameplay_screen():
    engine.background_color = 1, 1, 0
    engine.draw_text("GAMEPLAY", engine.width/2, engine.height/4, True)

    # draw_player()
    player.display(engine)

# global speed_x, speed_y, direction_player
#
# def initialize_variables():
#     global speed_x, speed_y, direction_player
#     direction_player = 0
#     player_x = 0
#     player_y = 0
#     speed_x = 0
#     speed_y = 0

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    # initialize_variables()
    pass

player = Player(engine)


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    global current_state

    if current_state == GameState.START:
        start_screen()
    elif current_state == GameState.THEME:
        theme_screen()
    elif current_state == GameState.GAMEPLAY:
        gameplay_screen()


def evaluate():
    """
    This function is being executed over and over, as fast as the frame rate. Use to update (not draw).
    """
    key = engine.key
    if (current_state == GameState.GAMEPLAY and
            key == "RIGHT" or key == "LEFT" or key == "UP" or key == "DOWN" or
            key == "d" or key == "a" or key == "w" or key == "s"):
        player.move(key, engine)

    pass


def mouse_pressed_event(mouse_x: int, mouse_y: int, mouse_button: MouseButton):
    """
    This function is only executed once each time a mouse button was pressed!
    """
    global current_state, current_theme

    if current_state == GameState.THEME:
        engine.shape_mode = ShapeMode.CORNER

        on_day = engine.colliding_point_in_rect(mouse_x, mouse_y, engine.width / 2 - 310, 100, 300, engine.height - 200)
        on_night = engine.colliding_point_in_rect(mouse_x, mouse_y, engine.width / 2 + 10, 100, 300, engine.height - 200)

        if on_day:
            current_theme = GameTheme.DAY
            current_state = GameState.GAMEPLAY
        elif on_night:
            current_theme = GameTheme.NIGHT
            current_state = GameState.GAMEPLAY
    print(current_theme)


def key_up_event(key: str):
    """
    This function is only executed once each time a key was released!
    Special keys have more than 1 character, for example ESCAPE, BACKSPACE, ENTER, ...
    """
    global current_state
    if current_state == GameState.START and key:
        current_state = GameState.THEME


    # DEBUG
    if key == "1":
        current_state = GameState.START
    elif key == "2":
        current_state = GameState.THEME
    elif key == "3":
        current_state = GameState.GAMEPLAY
    elif key == "4":
        current_state = GameState.END_SCREEN

    # print(key)

    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
