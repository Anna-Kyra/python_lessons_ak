#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 1-12-2025

@author: anna-
"""

import dae_progfa_lib as pfe
from dae_progfa_lib import MouseButton

from L06_images.demo import img_background

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(1000, 600)

# Set the frame rate to x frames per second:
engine.fps = 60

img_background = engine.load_image("Resources/mario/background.png")

# MARIO
mario_spritesheet = engine.load_image("Resources/mario/mario-spritesheet.png")
mario_frames = mario_spritesheet.cut_all_frames(10, 6)
mario_size = 100

# GOOMBA
goomba_spritesheet = engine.load_image("Resources/mario/goomba_spritesheet.png")
goomba_frames = goomba_spritesheet.cut_all_frames(1, 8)
goomba_size = 80

timer = 0


def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """

    pass

def draw_mario():
    mario_frames[0].draw_fixed_size(engine.width / 2 , 546 - mario_size, mario_size, mario_size)
    pass

def draw_timer():
    engine.color = 1, 1, 1
    engine.set_font("Resources/mario/supermario.ttf", 20)
    engine.draw_text('TIME', engine.width - 200, 40)
    engine.draw_text(f'{timer}', engine.width - 200, 40 + 20)
    pass

def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    img_background.draw_fixed_size(0, 0, engine.width, engine.height, False)
    # spritesheet_mario.draw_fixed_size(0, 0, engine.width, engine.height)
    draw_mario()
    goomba_frames[0].draw_fixed_size(engine.width / 4, 556 - goomba_size, goomba_size, goomba_size)
    draw_timer()

    pass

def evaluate():
    """
    This function is being executed over and over, as fast as the frame rate. Use to update (not draw).
    """

    pass

def change_timer():
    global


def mouse_pressed_event(mouse_x: int, mouse_y: int, mouse_button: MouseButton):
    """
    This function is only executed once each time a mouse button was pressed!
    """
    print(f"x = {mouse_x} y = {mouse_y}")

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
