#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 8-12-2025

@author: anna-
"""

import dae_progfa_lib as pfe
from dae_progfa_lib import MouseButton, ShapeMode
import random

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 600)

# Set the frame rate to x frames per second:
engine.fps = 60

# SPAWNING WORDS
# Lists
word_list_cow = ["cow", "cheese", "milk", "leather", "meat", "four stomachs", "strong smell", "peripheral vision", "zoomies", "mooo"]

# Randomise
random_word_cow = random.choice(word_list_cow)

# Chosen word lists
random_word_list_cow = list(random_word_cow)
word_colored_cow = ""

# Current index
current_index_cow = 0

print(f"Cow = {random_word_cow}")

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """

    pass

def draw_word(word_cow: str):
    engine.shape_mode = ShapeMode.CORNER
    engine.color = 1, 1, 1
    engine.set_font_size(50)
    engine.draw_text(f"{word_cow}", engine.width/2, engine.height/2, False)
    pass

def draw_word_color(word_colored: str):
    engine.shape_mode = ShapeMode.CORNER
    engine.color = 0, 1, 0
    engine.set_font_size(50)
    engine.draw_text(f"{word_colored}", engine.width / 2, engine.height / 2, False)
    pass

def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    engine.background_color = 0, 0, 0
    draw_word(random_word_cow.upper())
    draw_word_color(word_colored_cow.upper())
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
    global current_index_cow, random_word_cow, random_word_list_cow, word_colored_cow

    prefix = f"\033[32m"
    suffix = f"\033[0m"

    correct = False  # om te weten of er minstens 1 match was

    # COW
    if key.lower() == random_word_list_cow[current_index_cow]:
        correct = True
        current_index_cow += 1

        colored_word_cow = ""
        for index, letter in enumerate(random_word_list_cow):
            if index < current_index_cow:
                colored_word_cow += f"{prefix}{letter}{suffix}"
                word_colored_cow += letter
            else:
                colored_word_cow += letter
        print(f"Cow = {colored_word_cow}")

        if current_index_cow == len(random_word_list_cow):
            print("Cow word complete!")
            random_word_cow = random.choice(word_list_cow)
            random_word_list_cow = list(random_word_cow)
            current_index_cow = 0
            print(f"Cow = {random_word_cow}")
    if not correct:
        print("Wrong:", key)

    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
