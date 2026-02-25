#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 24-2-2026

@author: anna-
"""
import random

import dae_progfa_lib as pfe
from dae_progfa_lib import MouseButton, ShapeMode
from typing import List

from star import Star

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(750, 500)

# Set the frame rate to x frames per second:
engine.fps = 60

star_img = engine.load_image("Resources/star.png")
background = engine.load_image("Resources/starry_night.png")

constellation = [
    Star(316, 63, 23),
    Star(312, 106, 16),
    Star(379, 162, 23),
    Star(372, 260, 23),
    Star(343, 311, 23),
    Star(358, 339, 16),
    Star(347, 360, 23),
    Star(356, 380, 23),
]

constellations = {
    "lynx" : [
        Star(316, 63, 23),
        Star(312, 106, 16),
        Star(379, 162, 23),
        Star(372, 260, 23),
        Star(343, 311, 23),
        Star(358, 339, 16),
        Star(347, 360, 23),
        Star(356, 380, 23),
    ],
    "draco" : [
        Star(538, 316, 23),
        Star(495, 311, 23),
        Star(415, 329, 23),
        Star(329, 309, 30),
        Star(304, 278, 23),
        Star(314, 248, 30),
        Star(331, 197, 30),
        Star(371, 142, 23),
        Star(393, 114, 13),
        Star(377, 85, 23),
        Star(349, 102, 23),
        Star(281, 104, 13),
        Star(257, 165, 23),
        Star(246, 191, 13),
        Star(224, 194, 30),
        Star(215, 161, 30),
        Star(257, 165, 23),
    ],
    "ursa minor": [
        Star(398, 180, 30),
        Star(368, 188, 23),
        Star(336, 206, 23),
        Star(318, 238, 23),
        Star(314, 276, 30),
        Star(287, 275, 23),
        Star(296, 233, 13),
        Star(318, 238, 23),
    ],
    "lacerta": [
        Star(375, 135, 23),
        Star(414, 166, 16),
        Star(406, 192, 16),
        Star(425, 197, 16),
        Star(422, 215, 16),
        Star(436, 216, 23),
        Star(430, 235, 16),
    ],
    "cassiopeia": [
        Star(322, 182, 30),
        Star(357, 164, 30),
        Star(365, 179, 23),
        Star(368, 199, 30),
        Star(397, 205, 23),
        Star(412, 242, 23),
    ],
    "triangulum": [
        Star(363, 166, 16),
        Star(339, 194, 23),
        Star(359, 196, 23),
        Star(373, 173, 16),
    ],
    "canes venatici": [
        Star(351, 233, 30),
        Star(395, 234, 23),
    ],
    "cepheus": [
        Star(417, 206, 23),
        Star(466, 288, 30),
        Star(381, 264, 30),
        Star(335, 220, 30),
        Star(360, 164, 23),
        Star(417, 206, 23),
        Star(381, 264, 30),
    ],
    "hercules": [
        Star(447, 275, 23),
        Star(410, 264, 23),
        Star(380, 261, 23),
        Star(328, 286, 30),
        Star(312, 250, 23),
        Star(348, 210, 23),
        Star(380, 261, 23),
        Star(348, 210, 23),
        Star(414, 159, 23),
    ]
}
random_constellation = random.choice(list(constellations.keys()))

def draw_constellation(name : str, stars : List[Star]):
    engine.color = 1, 1, 1
    engine.outline_color = 1, 1, 1
    engine.draw_text(f"{name}", engine.width/2, engine.height - 20, True)
    for index, star in enumerate(stars):
        engine.shape_mode = ShapeMode.CENTER
        star_img.draw_fixed_size(star.x, star.y, star.size, star.size)

        if index < len(stars) - 1:
            next_star = stars[index+1]
            engine.draw_line(star.x, star.y, next_star.x, next_star.y)

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """

    pass


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    engine.shape_mode = ShapeMode.CORNER
    background.draw_fixed_size(0, 0, engine.width, engine.height, False)


    name = random_constellation  # dit is al de key
    stars = constellations[random_constellation]  # dit is de lijst

    draw_constellation(f"{name}", stars)

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
    global random_constellation
    random_constellation = random.choice(list(constellations.keys()))

    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
