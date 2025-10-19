#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 19-10-2025

@author: anna-
"""

import dae_progfa_lib as pfe
from dae_progfa_lib import MouseButton, ShapeMode

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 800)

# Set the frame rate to x frames per second:
engine.fps = 60


def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """

    pass

def mural1():
    engine.background_color = (1, 1, 1)

    def draw_tile(x: int | float, y: int | float, rotation: int | float, color1: tuple, color2: tuple):
        """
        Drawing a tile width two triangle shapes with different colors
        :param x: The x position of the tile (center or top left, determined by shape mode)
        :param y: The y position of the tile (center or top left, determined by shape mode)
        :param rotation: rotation of triangle (left or right)
        :param color1: fill triangle 1
        :param color2: fill triangle 2
        :return:
        """
        engine.shape_mode = ShapeMode.CORNER
        tile_width = engine.width/2
        tile_height = engine.height/2

        engine.color = color1
        engine.draw_rectangle(x, y, tile_width, tile_height,  0)
        engine.color = color2
        engine.draw_triangle(float(rotation) + x, 0 + y, tile_width + x, tile_height + y, 0 + x, tile_height + y, 0)
        pass

    #Colors
    teal = (0.33, 0.54, 0.50)
    mustard = (0.87, 0.70, 0.31)
    coral = (0.95, 0.60, 0.50)

    #Rotation triangle
    left = engine.width / 2
    right = 0

    #Tiles
    draw_tile(0, 0, left, mustard, teal)
    draw_tile(engine.width/2, 0, right, mustard, coral)
    draw_tile(0, engine.height/2, right, coral, mustard)
    draw_tile(engine.width/2, engine.height/2, left, teal, mustard)
    pass

def calculate_color(r: int, g: int, b: int) -> tuple:
    r = r / 255
    g = g / 255
    b = b / 255
    return r, g, b

def mural2():
    engine.shape_mode = ShapeMode.CORNER

    #Colors
    red = tuple(calculate_color(255, 53, 57))
    silver = tuple(calculate_color(224, 230, 230))
    black = tuple(calculate_color(30, 30, 30))
    yellow = tuple(calculate_color(255, 173, 15))
    blue = tuple(calculate_color(0, 81, 108))
    white = tuple(calculate_color(255, 255, 255))

    #Tile size
    tile_width = engine.width/4
    tile_height = engine.height/4

    #RECTANGLES
    def rectangle_vertical(x: int | float, y: int | float, color1: tuple, color2: tuple):
        engine.color = color1
        engine.draw_rectangle(x, y, tile_width, tile_height, 0)

        engine.color = color2
        engine.draw_rectangle(x, y, tile_width/2, tile_height, 0)

    def rectangle_horizontal(x: int | float, y: int | float, color1: tuple, color2: tuple):
        engine.color = color1
        engine.draw_rectangle(x, y, tile_width, tile_height, 0)

        engine.color = color2
        engine.draw_rectangle(x, y, tile_width, tile_height/2, 0)

    #TRIANGLES
    def triangles_left(x: int | float, y: int | float, color1: tuple, color2: tuple):
        engine.color = color1
        engine.draw_rectangle(x, y, tile_width, tile_height,  0)
        engine.color = color2
        engine.draw_triangle(0 + x, 0 + y, tile_width + x, tile_height + y, 0 + x, tile_height + y, 0)
        pass

    def triangles_right(x: int | float, y: int | float, color1: tuple, color2: tuple):
        engine.color = color1
        engine.draw_rectangle(x, y, tile_width, tile_height,  0)
        engine.color = color2
        engine.draw_triangle(tile_width + x, 0 + y, tile_width + x, tile_height + y, 0 + x, tile_height + y, 0)
        pass

    def circle(x: int | float, y: int | float, background_color: tuple, color_circle: tuple):
        engine.color = background_color
        engine.draw_rectangle(x, y, tile_width, tile_height, 0)
        engine.color = color_circle
        engine.draw_ellipse(x, y, tile_width, tile_height, 0)
        pass

    #DRAWING
    rectangle_vertical(0, 0, silver, red)
    triangles_left(engine.width / 4, 0, blue, black)
    circle(engine.width/2, 0, yellow, black)
    rectangle_horizontal(engine.width*(3/4), 0, silver, red)

    triangles_left(0, engine.height / 4, yellow, white)
    triangles_right(engine.width / 4, engine.height / 4, black, red)
    triangles_left(engine.width / 2, engine.height / 4, white, black)
    rectangle_vertical(engine.width*(3 / 4), engine.height / 4, blue, yellow)

    rectangle_horizontal(0, engine.height/2, silver, black)
    triangles_right(engine.width/4, engine.height/2, yellow, blue)
    triangles_left(engine.width/2, engine.height/2, black, blue)
    circle(engine.width * (3/4), engine.height / 2, red, silver)

    circle(0, engine.height * (3 / 4), black, blue)
    triangles_left(engine.width / 4, engine.height * (3 / 4), white, red)
    triangles_right(engine.width / 2, engine.height * (3 / 4), silver, black)
    rectangle_horizontal(engine.width * (3 / 4), engine.height * (3 / 4), yellow, black)
    pass

def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    # mural1()
    mural2()
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
