#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 10-5-2026

@author: anna-
"""

import dae_progfa_lib as pfe
from dae_progfa_lib import MouseButton, ShapeMode
from enum import Enum

from map import Map
from player import Player
from npc import NPC

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(600*1.5, 600*1.5)

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

theme_path = "day_theme"
center_background = engine.load_image(f"resources/{theme_path}/background_center.png")
right_background = engine.load_image(f"resources/{theme_path}/background_right.png")
left_background = engine.load_image(f"resources/{theme_path}/background_left.png")
bottom_background = engine.load_image(f"resources/{theme_path}/background_bottom.png")
top_background = engine.load_image(f"resources/{theme_path}/background_top.png")

inventory = engine.load_image(f"resources/{theme_path}/inventory.png")

def load_backgrounds():
    global center_background, right_background, left_background, bottom_background, top_background,theme_path

    if current_theme == GameTheme.DAY:
        theme_path = "day_theme"
    else:
        theme_path = "night_theme"

    if current_state == GameState.GAMEPLAY:
        center_background = engine.load_image(
            f"resources/{theme_path}/background_center.png")
        right_background = engine.load_image(
            f"resources/{theme_path}/background_right.png"
        )
        left_background = engine.load_image(f"resources/{theme_path}/background_left.png")
        bottom_background = engine.load_image(f"resources/{theme_path}/background_bottom.png")
        top_background = engine.load_image(f"resources/{theme_path}/background_top.png")

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
    engine.shape_mode = ShapeMode.CORNER
    engine.background_color = 1, 1, 0
    engine.draw_text("CHOOSE THEME", engine.width / 2, 50, True)
    engine.color = 0, 0, 0

    engine.draw_rectangle(engine.width / 2 - 310, 100, 300, engine.height - 200)
    engine.draw_rectangle(engine.width / 2 + 10, 100, 300, engine.height - 200)

def draw_player():
    engine.color = 0, 0, 0
    engine.draw_rectangle(engine.width / 2, engine.height / 2, 100, 100)

def draw_inventory():
    engine.color = 0, 0, 0
    engine.shape_mode = ShapeMode.CORNER
    inventory.draw_fixed_size(engine.width - 304-25, engine.height - 100, 304, 75)

def gameplay_screen():
    global map_dir
    engine.shape_mode = ShapeMode.CORNER
    if current_state == GameState.GAMEPLAY:
        if current_map == GameMap.CENTER:
            engine.background_color = 1, 1, 0
            center_background.draw_fixed_size(0, 0, engine.width, engine.height, False)
            map_dir = "center"
            npc_Heidi.display()
        elif current_map == GameMap.LEFT:
            engine.background_color = 1, 0, 0
            map_dir = "left"
            left_background.draw_fixed_size(0, 0, engine.width, engine.height, False)
        elif current_map == GameMap.RIGHT:
            engine.background_color = 0, 1, 0
            map_dir = "right"
            right_background.draw_fixed_size(0, 0, engine.width, engine.height, False)
        elif current_map == GameMap.UP:
            engine.background_color = 0, 0, 1
            map_dir = "top"
            top_background.draw_fixed_size(0, 0, engine.width, engine.height, False)
        elif current_map == GameMap.BOTTOM:
            engine.background_color = 0, 1, 1
            map_dir = "bottom"
            bottom_background.draw_fixed_size(0, 0, engine.width, engine.height, False)

    engine.draw_text("GAMEPLAY", engine.width/2, engine.height/4, True)
    draw_inventory()
    player.display()

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    # initialize_variables()

    pass

map_dir = "center"
game_map = Map(str(current_theme), "center", engine)
player = Player(game_map, str(current_theme), "center", engine)
npc_Heidi = NPC("Heidi", game_map, engine)
npc_Max = NPC("Max", game_map, engine)

def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    global current_state, current_map, map_dir

    # map.change_map(map_dir)
    if current_state == GameState.START:
        start_screen()
    elif current_state == GameState.THEME:
        theme_screen()
    elif current_state == GameState.GAMEPLAY:
        gameplay_screen()
        #print(engine.width, player.center_x + player.size/2)

        if current_map == GameMap.CENTER or current_map == GameMap.LEFT:
            if player.is_out_of_bounds_right():
                if current_map == GameMap.CENTER:
                    current_map = GameMap.RIGHT
                    map_dir = "right"
                elif current_map == GameMap.LEFT:
                    current_map = GameMap.CENTER
                    map_dir = "center"
        if current_map == GameMap.CENTER or current_map == GameMap.RIGHT:
            if player.is_out_of_bounds_left():
                if current_map == GameMap.CENTER:
                    current_map = GameMap.LEFT
                    map_dir = "left"
                elif current_map == GameMap.RIGHT:
                    current_map = GameMap.CENTER
                    map_dir = "center"
        if current_map == GameMap.CENTER or current_map == GameMap.BOTTOM:
            if player.is_out_of_bounds_up():
                if current_map == GameMap.CENTER:
                    current_map = GameMap.UP
                    map_dir = "top"
                elif current_map == GameMap.BOTTOM:
                    current_map = GameMap.CENTER
                    map_dir = "center"
        if current_map == GameMap.CENTER or current_map == GameMap.UP:
            if player.is_out_of_bounds_down():
                if current_map == GameMap.CENTER:
                    current_map = GameMap.BOTTOM
                    map_dir = "bottom"
                elif current_map == GameMap.UP:
                    current_map = GameMap.CENTER
                    map_dir = "center"
        game_map.change_map(map_dir)

def evaluate():
    """
    This function is being executed over and over, as fast as the frame rate. Use to update (not draw).
    """
    key = engine.key
    if (current_state == GameState.GAMEPLAY and
            key == "RIGHT" or key == "LEFT" or key == "UP" or key == "DOWN" or
            key == "d" or key == "a" or key == "w" or key == "s"):
        player.move(key)
    if current_state == GameState.GAMEPLAY:
        player.animate()
        player.collision(npc_Heidi.x, npc_Heidi.y, npc_Heidi.size, npc_Heidi.size)
        engine.draw_square(0, 0, 200)
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

        load_backgrounds()
        print(current_theme)
    else:
        pass



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
