#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 24-11-2025

@author: anna-
"""
import random

import dae_progfa_lib as pfe
from dae_progfa_lib import MouseButton, ShapeMode

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 600)

# Set the frame rate to x frames per second:
engine.fps = 60

crew_spirit = engine.load_image("resources/crewmates/crew_green_sprite.png")
frames = crew_spirit.cut_all_frames(3, 3)
crew_frame_counter = 0
window_frame_counter = 0

star_x = [engine.width]
star_y = [engine.height / 2]
speed = -2



def init_stars():
    number_stars = 20
    for index in range(0, number_stars):
        star_x.append(random.randint(0, engine.width))
        star_y.append(random.randint(0, engine.height))

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    init_stars()
    pass

def draw_stars():
    engine.outline_color = 1, 1, 1
    for index in range(0, len(star_x)):
        engine.draw_dot(star_x[index], star_y[index], 4)
    pass

def move_stars():
    global  star_x
    for index in range(0, len(star_x)):
        star_x[index] += speed
        if star_x[index] < 0:
            star_x[index] = engine.width
    pass



def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    engine.background_color = 0, 0, 0
    draw_stars()
    frames[crew_frame_counter].draw(0, 0)

    pass

def animate_crew():
    global window_frame_counter, crew_frame_counter

    window_frame_counter += 1
    if (window_frame_counter > 15):
        window_frame_counter = 0
        crew_frame_counter += 1
        if crew_frame_counter >= 8:
            crew_frame_counter = 0

def evaluate():
    """
    This function is being executed over and over, as fast as the frame rate. Use to update (not draw).
    """
    animate_crew()
    move_stars()

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
