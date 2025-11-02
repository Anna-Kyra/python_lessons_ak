#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 29-10-2025

@author: Anna-Kyra
"""

import dae_progfa_lib as pfe
from dae_progfa_lib import MouseButton, ShapeMode

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 600)

# Set the frame rate to x frames per second:
engine.fps = 60


def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    pass

def draw_ghost(x: float, y: float, scale: float = 1.0, color: tuple[float,float, float] = (1, 1, 1)) -> None:
    width = 90 * scale
    height = width * 1.5
    engine.shape_mode = ShapeMode.CORNER

    on_ghost = engine.colliding_point_in_rect(engine.mouse_x, engine.mouse_y, x, y, width, height)

    if on_ghost and engine.mouse_button == MouseButton.LEFT:
        engine.color = color
        engine.outline_color = None

        engine.shape_mode = ShapeMode.CORNER
        engine.draw_arc(x, y, width, width, 180, 360)
        engine.draw_rectangle(x, y + width / 2, width, height - width / 2)

        eye_size = 28 * scale
        engine.color = 0, 0, 0
        engine.shape_mode = ShapeMode.CENTER
        distance = width / 2.5
        engine.draw_circle(x + width / 2 - distance / 2, y + width / 3, eye_size)
        engine.draw_circle(x + width / 2 + distance / 2, y + width / 3, eye_size)

        mouth_size = eye_size * 1.3
        engine.draw_ellipse(x + width / 2, y + width / 1.4, mouth_size,
                            mouth_size * 1.2)
        # BOO
        engine.color = 1, 1, 1
        engine.draw_text("BOO!", x + width / 2, y + height + 10, centered=True)

def flashlight():
    if engine.mouse_button == MouseButton.LEFT:
        engine.shape_mode = ShapeMode.CENTER
        engine.color = (1, 1, 0, 0.2)
        engine.draw_circle(engine.mouse_x, engine.mouse_y, 200, 0)

def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    engine.background_color = 0, 0, 0
    draw_ghost(engine.width/2, engine.height/4, .5)
    draw_ghost(engine.width*(3/4), engine.height*(3/4), 1.0)
    draw_ghost(engine.width*0.2, engine.height*(3/5), 1.0)
    draw_ghost(engine.width/8, engine.height/8, 1.0)

    flashlight()
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
    if key == 'f':
        print("-> Find the ghosts!")
    elif key == 'h':
        print("-> HAPPY HALLOWEEN!")
    else:
        print(f"[HAUNTED KEY] {key}")
    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
