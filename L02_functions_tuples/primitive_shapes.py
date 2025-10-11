#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 6-10-2025

@author: anna-
"""

import dae_progfa_lib as pfe
from dae_progfa_lib import MouseButton, ShapeMode

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(1200, 800)

# Set the frame rate to x frames per second:
engine.fps = 60


def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """

    pass

#EXCERCISES

#Excercise 1
def shape1():
    """
    NORMAL: Four black ellipses with a white square in it
    :return:
    """
    engine.background_color = (1, 1, 1)

    #Ellipses
    engine.color = (0, 0, 0)
    engine.shape_mode = ShapeMode.CORNER
    engine.draw_ellipse(0,0, engine.width/2, engine.height/2, 0)
    engine.draw_ellipse(engine.width/2, 0, engine.width/2, engine.height/2, 0)
    engine.draw_ellipse(0, engine.height/2, engine.width/2, engine.height/2, 0)
    engine.draw_ellipse(engine.width/2, engine.height/2, engine.width/2, engine.height/2, 0)

    #Rectangles
    engine.color = (1, 1, 1)
    engine.shape_mode = ShapeMode.CENTER
    engine.draw_rectangle(engine.width/2, engine.height/2, engine.width/2, engine.height/2, 0)

def shape2():
    """
    NORMAL: Quads with an ellipse inside
    :return:
    """
    engine.background_color = (0, 0, 0)

    #Quad
    engine.color = (1, 1, 1)
    engine.shape_mode = ShapeMode.CORNER
    engine.draw_quad(engine.width/2, 0, engine.width, engine.height/2, engine.width/2, engine.height, 0, engine.height/2, 0)

    #Ellipse
    engine.color = (0, 0, 0)
    engine.shape_mode = ShapeMode.CENTER
    engine.draw_ellipse(engine.width/2, engine.height/2, engine.width/2, engine.height/2,0)

def shape3():
    """
    MODERATE: triangles like a windmill
    :return:
    """
    engine.background_color = (1, 1, 1)
    #Triangles
    engine.color = (0, 0, 0)
    engine.shape_mode = ShapeMode.CORNER
    engine.draw_triangle(0, 0, engine.width/2, engine.height/2, 0, engine.height/2, 0)
    engine.draw_triangle(engine.width/2, 0, engine.width, 0, engine.width/2, engine.height/2, 0)
    engine.draw_triangle(engine.width/2, engine.height/2, engine.width/2, engine.height, 0, engine.height, 0)
    engine.draw_triangle(engine.width/2, engine.height/2, engine.width, engine.height/2, engine.width, engine.height, 0)

def shape4():
    """
    NORMAL: 2 triangles next to each-other
    :return:
    """
    engine.background_color = (1, 1, 1)
    # Triangles
    engine.color = (0, 0, 0)
    engine.shape_mode = ShapeMode.CORNER
    engine.draw_triangle(0, 0, engine.width/2, engine.height/2, 0, engine.height, 0)
    engine.draw_triangle(engine.width/2, 0, engine.width, engine.height/2, engine.width/2, engine.height, 0)

def shape5():
    """
    NORMAL: rectangles bottom and top, arcs in the middle with an inverted effect
    :return:
    """
    engine.background_color = (0, 0, 0)
    #rectangle
    engine.color = (1, 1, 1)
    engine.shape_mode = ShapeMode.CORNER
    engine.draw_rectangle(0, engine.height/2, engine.width, engine.height/2, 0)

    #Arcs
    engine.shape_mode = ShapeMode.CENTER
    engine.color = (1, 1, 1)
    engine.draw_arc(engine.width/2, engine.height/2, engine.width/2, engine.height/2, -180, 0, 0)
    engine.color = (0, 0, 0)
    engine.draw_arc(engine.width/2, engine.height/2, engine.width/2, engine.height/2, 0, 180, 0)

def shape6():
    """
    CHALLENGE: Same as last one but with one more arc/ellipse
    :return:
    """
    engine.background_color = (0, 0, 0)
    # rectangle
    engine.color = (1, 1, 1)
    engine.shape_mode = ShapeMode.CORNER
    engine.draw_rectangle(0, engine.height / 2, engine.width, engine.height / 2, 0)

    #Bigger circle
    engine.shape_mode = ShapeMode.CENTER
    engine.color = (0, 0, 0)
    engine.draw_ellipse(engine.width / 2, engine.height / 2, engine.width / 2, engine.height / 2, 0)
    engine.color = (1, 1, 1)
    engine.draw_arc(engine.width / 2, engine.height / 2, engine.width / 2, engine.height / 2, -180, 0, 0)

    #Smaller circle
    engine.color = (1, 1, 1)
    engine.draw_ellipse(engine.width / 2, engine.height / 2, engine.width / 4, engine.height / 4, 0)
    engine.color = (0, 0, 0)
    engine.draw_arc(engine.width / 2, engine.height / 2, engine.width / 4, engine.height / 4, -180, 0, 0)

def shape7():
    """
    NORMAL: Rotating duo arc
    :return:
    """
    engine.background_color = (0, 0, 0)
    #Rectangle
    engine.shape_mode = ShapeMode.CORNER
    engine.color = (1, 1, 1)
    engine.draw_rectangle(0, engine.height/2, engine.width, engine.height/2, 0)

    #Circle duo
    engine.shape_mode = ShapeMode.CENTER
    engine.color = (1, 1, 1)
    engine.draw_arc(engine.width/2, engine.height/2, engine.width/2, engine.height/2, -225, 45, 0)
    engine.color = (0, 0, 0)
    engine.draw_arc(engine.width/2, engine.height/2, engine.width/2, engine.height/2, 45, 225, 0)

def shape8():
    """
    NORMAL: Big half ellipses
    :return:
    """
    engine.background_color = (0, 0, 0)
    #Big ellipses white
    engine.shape_mode = ShapeMode.CENTER
    engine.color = (1, 1, 1)
    engine.draw_ellipse(engine.width/2, 0, engine.width, engine.height, 0)
    engine.draw_ellipse(engine.width/2, engine.height, engine.width, engine.height, 0)

    #Small ellipses black
    engine.color = (0, 0, 0)
    engine.draw_ellipse(engine.width/2, 0, engine.width/4, engine.height/4, 0)
    engine.draw_ellipse(engine.width/2, engine.height, engine.width/4, engine.height/4, 0)

def shape9():
    """
    MODERATE: Tiny black ellipses
    :return:
    """
    engine.background_color = (1, 1, 1)
    engine.shape_mode = ShapeMode.CENTER
    engine.color = (0, 0, 0)
    engine.draw_ellipse(engine.width/2, engine.height/4, engine.width/8, engine.height/8, 0)
    engine.draw_ellipse(engine.width/4, engine.height/2, engine.width/8, engine.height/8, 0)
    engine.draw_ellipse(engine.width*(3/4), engine.height/2, engine.width/8, engine.height/8, 0)
    engine.draw_ellipse(engine.width/2, engine.height*(3/4), engine.width/8, engine.height/8, 0)

def shape10():
    """
    NORMAL: black ellipses 1/4 of window size
    :return:
    """
    engine.background_color = (1, 1, 1)
    engine.shape_mode = ShapeMode.CENTER
    engine.color = (0, 0, 0)
    engine.draw_ellipse(engine.width/2, 0, engine.width/4, engine.height/4, 0)
    engine.draw_ellipse(engine.width, engine.height/2, engine.width/4, engine.height/4, 0)
    engine.draw_ellipse(engine.width/2, engine.height, engine.width/4, engine.height/4, 0)
    engine.draw_ellipse(0, engine.height/2, engine.width/4, engine.height/4, 0)
    engine.draw_ellipse(engine.width/2, engine.height/2, engine.width/4, engine.height/4, 0)

def shape11():
    """
    NORMAL: Making a star
    :return:
    """
    engine.background_color = (0, 0, 0)
    engine.shape_mode = ShapeMode.CENTER
    engine.color = (1, 1, 1)
    engine.draw_ellipse(0, 0, engine.width, engine.height, 0)
    engine.draw_ellipse(engine.width, 0, engine.width, engine.height, 0)
    engine.draw_ellipse(engine.width, engine.height, engine.width, engine.height, 0)
    engine.draw_ellipse(0, engine.height, engine.width, engine.height, 0)

def shape12():
    """
    NORMAL: Black zandloper in het midden
    :return:
    """
    engine.background_color = (1, 1, 1)
    engine.shape_mode = ShapeMode.CORNER
    engine.color = (0, 0, 0)
    engine.draw_quad(0, 0, engine.width, 0, 0, engine.height, engine.width, engine.height, 0)

def shape13():
    """
    MODERATE: cubes rotated
    :return:
    """
    engine.background_color = (0, 0, 0)
    engine.shape_mode = ShapeMode.CORNER
    engine.color = (1, 1, 1)
    engine.draw_quad(engine.width/4, 0, engine.width/2, engine.height/4, engine.width/4, engine.height/2, 0, engine.height/4, 0)
    engine.draw_quad(engine.width*(3/4), 0, engine.width, engine.height/4, engine.width*(3/4), engine.height/2, engine.width/2, engine.height/4, 0)
    engine.draw_quad(engine.width*(3/4), engine.height/2, engine.width, engine.height*(3/4), engine.width*(3/4), engine.height, engine.width/2, engine.height*(3/4), 0)
    engine.draw_quad(engine.width/4, engine.height/2, engine.width/2, engine.height*(3/4), engine.width/4, engine.height, 0, engine.height*(3/4),0)

def shape14():
    """
    NORMAL: Rectangel triangle 4 shapes
    :return:
    """
    engine.background_color = (1, 1, 1)
    engine.shape_mode = ShapeMode.CORNER
    engine.color = (0, 0, 0)

    engine.draw_rectangle(0, 0, engine.width/2, engine.height/2, 0)
    engine.draw_triangle(0, engine.height/2, engine.width/2, engine.height/2, 0, engine.height, 0)
    engine.draw_triangle(engine.width/2, engine.height/2, engine.width, engine.height/2, engine.width, engine.height, 0)

def shape15():
    """
    CHALLENGE: Skewed rectangle duos
    :return:
    """
    engine.background_color = (0, 0, 0)
    engine.shape_mode = ShapeMode.CORNER
    #Rectangles white
    engine.color = (1, 1, 1)
    engine.draw_rectangle(0, engine.height/2, engine.width, engine.height/2, 0)
    engine.draw_quad(0, 0, engine.width/4, 0, engine.width*(3/4), engine.height/2, engine.width/2, engine.height/2, 0)

    #Rectangle black
    engine.color = (0, 0, 0)
    engine.draw_quad(engine.width/2, engine.height/2, engine.width*(3/4), engine.height/2, engine.width/4, engine.height, 0, engine.height, 0)

def shape16():
    """
    NORMAL: ellipses and triangle
    :return:
    """
    engine.background_color = (0, 0, 0)
    #Ellipses
    engine.shape_mode = ShapeMode.CENTER
    engine.color = (1, 1, 1)
    engine.draw_ellipse(0, 0, engine.width/4, engine.height/4, 0)
    engine.draw_ellipse(engine.width, 0, engine.width/4, engine.height/4, 0)

    #Triangle
    engine.shape_mode = ShapeMode.CORNER
    engine.draw_triangle(engine.width/2, engine.height/2, engine.width, engine.height, 0, engine.height, 0)

def shape17():
    """
    CHALLENGE: Little ellipse 3 under each other + 2 big ones
    :return:
    """
    engine.background_color = (0, 0, 0)
    engine.shape_mode = ShapeMode.CENTER
    engine.color = (1, 1, 1)

    #Big ellipses
    engine.draw_ellipse(0, engine.height/2, engine.width/2, engine.height/2, 0)
    engine.draw_ellipse(engine.width, engine.height/2, engine.width/2, engine.height/2, 0)

    #Tiny ellipses
    engine.draw_ellipse(engine.width/2, engine.height/4, engine.width/8, engine.height/8, 0)
    engine.draw_ellipse(engine.width/2, engine.height/2, engine.width/8, engine.height/8, 0)
    engine.draw_ellipse(engine.width/2, engine.height*(3/4), engine.width/8, engine.height/8, 0)

def shape18():
    """
    MODERATE: Triangles everywhere!!
    :return:
    """
    engine.background_color = (1, 1, 1)
    engine.shape_mode = ShapeMode.CORNER
    engine.color = (0, 0, 0)
    engine.draw_triangle(0, 0, engine.width/2, 0, 0, engine.height/2, 0)
    engine.draw_triangle(engine.width/2, 0, engine.width, engine.height/2, engine.width/2, engine.height/2, 0)
    engine.draw_triangle(0, engine.height/2, engine.width/2, engine.height/2, engine.width/2, engine.height, 0)
    engine.draw_triangle(engine.width, engine.height/2, engine.width, engine.height, engine.width/2, engine.height, 0)

def shape19():
    """
    NORMAL: Pointy arc
    :return:
    """
    engine.background_color = (0, 0, 0)
    engine.shape_mode = ShapeMode.CORNER
    engine.color = (1, 1, 1)
    engine.draw_quad(engine.width/2, 0, engine.width/2, engine.height/2, engine.width/4, engine.height, 0, engine.height, 0)
    engine.draw_quad(engine.width/2, 0, engine.width, engine.height, engine.width*(3/4), engine.height, engine.width/2, engine.height/2, 0)

def shape20():
    """
    NORMAL: Ellipses
    :return:
    """
    engine.background_color = (1, 1, 1)
    engine.shape_mode = ShapeMode.CENTER
    #Big black ellipse
    engine.color = (0, 0, 0)
    engine.draw_ellipse(engine.width/2, engine.height/2, engine.width*(9/10), engine.height*(9/10), 0)

    #Small white ellipses
    engine.color = (1, 1, 1)
    engine.draw_ellipse(engine.width/2, 0, engine.width/2, engine.height/2, 0)
    engine.draw_ellipse(engine.width, engine.height/2, engine.width/2, engine.height/2, 0)
    engine.draw_ellipse(engine.width/2, engine.height, engine.width/2, engine.height/2, 0)
    engine.draw_ellipse(0, engine.height/2, engine.width/2, engine.height/2, 0)

def shape21():
    """
    NORMAL: big black quad and two ellipses under
    :return:
    """
    engine.background_color = (1, 1, 1)
    #Quad
    engine.shape_mode = ShapeMode.CORNER
    engine.color = (0, 0, 0)
    engine.draw_quad(engine.width/2, 0, engine.width, engine.height/2, engine.width/2, engine.height, 0, engine.height/2, 0)
    #Ellipses
    engine.shape_mode = ShapeMode.CENTER
    engine.color = (1, 1, 1)
    engine.draw_ellipse(engine.width/2, engine.height, engine.width/2, engine.height/2, 0)
    engine.color = (0, 0, 0)
    engine.draw_ellipse(engine.width/2, engine.height, engine.width/3, engine.height/3, 0)

def shape22():
    """
    NORMAL: 2 rectangles and an ellipse in 4 corners
    :return:
    """
    engine.background_color = (1, 1, 1)
    engine.shape_mode = ShapeMode.CORNER
    engine.color = (0, 0, 0)
    engine.draw_rectangle(0, 0, engine.width/2, engine.height/2, 0)
    engine.draw_ellipse(0, engine.height/2, engine.width/2, engine.height/2, 0)
    engine.draw_rectangle(engine.width/2, engine.height/2, engine.width/2, engine.height/2, 0)

def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    # shape1()
    # shape2()
    # shape3()
    # shape4()
    # shape5()
    # shape6()
    # shape7()
    # shape8()
    # shape9()
    # shape10()
    # shape11()
    # shape12()
    # shape13()
    # shape14()
    # shape15()
    # shape16()
    # shape17()
    # shape18()
    # shape19()
    # shape20()
    # shape21()
    shape22()
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
