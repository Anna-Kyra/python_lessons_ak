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

normal_font = "resources/font/PixeloidSans.ttf"
title_font = "resources/font/AnalogWhispers.ttf"

engine.set_font(title_font)

theme_path = "day_theme"
center_background = engine.load_image(f"resources/{theme_path}/background_center.png")
right_background = engine.load_image(f"resources/{theme_path}/background_right.png")
left_background = engine.load_image(f"resources/{theme_path}/background_left.png")
bottom_background = engine.load_image(f"resources/{theme_path}/background_bottom.png")
top_background = engine.load_image(f"resources/{theme_path}/background_top.png")

start_screen_background = engine.load_image("resources/start_screen_background.png")
theme_screen_background = engine.load_image("resources/theme_background.png")

inventory = engine.load_image(f"resources/{theme_path}/inventory.png")
scroll = engine.load_image(f"resources/{theme_path}/scroll.png")

number_invites = 7


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
    engine.color = (0.15, 0.19, 0.18)
    start_screen_background.draw_fixed_size(0, 0, engine.width, engine.height, False)

    engine.set_font(title_font)
    engine.set_font_size(120)
    engine.draw_text("Sprout's", engine.width/2-100, engine.height/4+100, True)
    engine.draw_text("Party", engine.width/2+100, engine.height/4+250, True)

    engine.set_font_size(30)
    engine.draw_text('_Press any key to play_', engine.width-200, engine.height-50, True)

def theme_screen():
    engine.shape_mode = ShapeMode.CORNER
    engine.background_color = 1, 1, 0
    theme_screen_background.draw_fixed_size(0, 0, engine.width, engine.height, False)
    engine.set_font_size(75)
    engine.color = (0.15, 0.19, 0.18)
    engine.draw_text("CHOOSE THEME", engine.width / 2, 100, True)
    engine.color = (0.15, 0.19, 0.18, 0.7)

    engine.draw_rectangle(engine.width / 2 - 370, 200, 350, engine.height - 400, 0)
    engine.color = 1,1,1
    engine.set_font_size(50)
    engine.draw_text("Day", engine.width / 2 - (370/2)-10, engine.height/2-25, True)
    engine.draw_text("Theme", engine.width / 2 - (370/2)-10, engine.height/2+25, True)
    engine.color = (0.15, 0.19, 0.18, 0.7)
    engine.draw_rectangle(engine.width / 2 + 20, 200, 350, engine.height - 400, 0)
    engine.set_font_size(50)
    engine.color = 0, 0, 0
    engine.draw_text("Night", engine.width / 2 + (370 / 2) + 10, engine.height / 2 - 25, True)
    engine.draw_text("Theme", engine.width / 2 + (370 / 2) + 10, engine.height / 2 + 25, True)

def draw_player():
    engine.color = 0, 0, 0
    engine.draw_rectangle(engine.width / 2, engine.height / 2, 100, 100)

def draw_inventory():
    engine.color = 0, 0, 0
    engine.shape_mode = ShapeMode.CORNER
    inventory.draw_fixed_size(engine.width - 304-25, engine.height - 100, 304, 75)
    if number_invites>0:
        scroll.draw_fixed_size(engine.width - 304-10, engine.height - 85, 30, 30)

        engine.color = (0.15, 0.19, 0.18)
        engine.draw_circle(engine.width - 300+7, engine.height - 85+20, 20, 0)
        engine.set_font(title_font)
        engine.set_font_size(15)
        engine.color = 1, 1, 1
        engine.draw_text(f"{number_invites}", engine.width - 300+12, engine.height - 85+24, False)

def draw_todo():
    engine.shape_mode = ShapeMode.CORNER
    engine.color = (0.15, 0.19, 0.18, 0.7)
    engine.draw_rectangle(engine.width- 250-25, 25, 250, 150, 0)
    engine.set_font_size(30)
    engine.color = 1, 1, 1
    engine.set_font(title_font)
    engine.draw_text("TODO:", engine.width- 250-15, 35, False)

    engine.set_font(normal_font)
    engine.set_font_size(15)
    engine.draw_text(f"Hand out invites for", engine.width- 250-15, 75, False)
    engine.draw_text(f"sprouts party.", engine.width- 250-15, 75+20, False)
    engine.draw_text(f"INVITES:    {7-number_invites}/7", engine.width- 250-15, 75+20 + 40, False)

def gameplay_screen():
    global map_dir
    engine.shape_mode = ShapeMode.CORNER
    if current_state == GameState.GAMEPLAY:
        if current_map == GameMap.CENTER:
            engine.background_color = 1, 1, 0
            center_background.draw_fixed_size(0, 0, engine.width, engine.height, False)
            map_dir = "center"
            npc_Heidi.display()
            npc_Max.display()
            npc_Arthur.display()

            if player.collision(npc_Heidi.x, npc_Heidi.y, npc_Heidi.size, npc_Heidi.size):
                engine.set_font(title_font)
                npc_Heidi.draw_dialogue()
                npc_Heidi.start_dialogue()
        elif current_map == GameMap.LEFT:
            engine.background_color = 1, 0, 0

            left_background.draw_fixed_size(0, 0, engine.width, engine.height, False)
            map_dir = "left"
            npc_Mia.display()
            npc_Liam.display()

        elif current_map == GameMap.RIGHT:
            engine.background_color = 0, 1, 0
            map_dir = "right"
            right_background.draw_fixed_size(0, 0, engine.width, engine.height, False)

        elif current_map == GameMap.UP:
            engine.background_color = 0, 0, 1
            map_dir = "top"
            top_background.draw_fixed_size(0, 0, engine.width, engine.height, False)
            npc_Ryda.display()

        elif current_map == GameMap.BOTTOM:
            engine.background_color = 0, 1, 1
            map_dir = "bottom"
            bottom_background.draw_fixed_size(0, 0, engine.width, engine.height, False)
            npc_Olivia.display()

    engine.draw_text("GAMEPLAY", engine.width/2, engine.height/4, True)
    draw_inventory()
    draw_todo()
    player.display()

def end_screen():
    engine.shape_mode = ShapeMode.CORNER
    engine.background_color = 1, 1, 0
    theme_screen_background.draw_fixed_size(0, 0, engine.width, engine.height, False)
    engine.set_font(title_font)
    engine.set_font_size(100)
    engine.draw_text("PARTY TIME", engine.width / 2, 300,True)
    engine.set_font_size(50)
    engine.draw_text("Nice you helped Sprout", engine.width / 2, 500-50, True)
    engine.draw_text("getting people to to his party!", engine.width / 2, 570-50, True)

    engine.set_font(normal_font)
    engine.set_font_size(30)
    engine.draw_text('_Press any key to go back to start', engine.width/2, engine.height - 50, True)

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    # initialize_variables()

    pass

map_dir = "center"
game_map = Map(str(current_theme), map_dir, engine)
player = Player(game_map, str(current_theme), "center", engine)
npc_Heidi = NPC("Heidi", game_map, engine)
npc_Max = NPC("Max", game_map, engine)
npc_Arthur = NPC("Arthur", game_map, engine)
npc_Mia = NPC("Mia", Map(str(current_theme), "left", engine), engine)
npc_Liam = NPC("Liam", Map(str(current_theme), "left", engine), engine)
npc_Ryda = NPC("Ryda", Map(str(current_theme), "top", engine), engine)
npc_Olivia = NPC("Olivia", Map(str(current_theme), "bottom", engine), engine)

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
    elif current_state == GameState.END_SCREEN:
        end_screen()
    game_map.change_map(map_dir)

def evaluate():
    """
    This function is being executed over and over, as fast as the frame rate. Use to update (not draw).
    """
    global number_invites
    key = engine.key
    if (current_state == GameState.GAMEPLAY and
            key == "RIGHT" or key == "LEFT" or key == "UP" or key == "DOWN" or
            key == "d" or key == "a" or key == "w" or key == "s"):
        if npc_Heidi.can_move():
            if player.collision(npc_Heidi.x, npc_Heidi.y, npc_Heidi.size, npc_Heidi.size):
                npc_Heidi.start_dialogue()
            player.move(key)

        else: return
    if current_state == GameState.GAMEPLAY:
        player.animate()
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
    global current_state, number_invites
    if current_state == GameState.START and key:
        current_state = GameState.THEME
    elif current_state == GameState.GAMEPLAY:
        npc_Heidi.progress_dialogue(key)
        number_invites -= npc_Heidi.minus_invite()
    elif current_state == GameState.END_SCREEN and key:
        current_state = GameState.START


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
