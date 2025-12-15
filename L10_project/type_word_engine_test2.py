#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 15-12-2025

@author: anna-
"""
import random
import dae_progfa_lib as pfe
from dae_progfa_lib import MouseButton, ShapeMode

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
new_word = ""
next_letter = ""

# Current index
current_index_cow = 0

print(f"Cow = {random_word_cow}")

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """

    pass

def draw_word(word_cow: str, x: int | float, y: int | float, font_size: int):
    global current_index_cow, new_word, next_letter, random_word_cow, random_word_list_cow
    engine.shape_mode = ShapeMode.CORNER
    engine.color = 1, 1, 1
    engine.set_font_size(50)
    engine.draw_text(f"{word_cow}", x, y)

    #new word
    engine.set_font_size(font_size)
    engine.color = 0, 1, 0
    engine.draw_text(f"{new_word}", x, y)

    if engine.key == random_word_list_cow[current_index_cow]:
        print(current_index_cow)
        new_word = new_word + random_word_list_cow[current_index_cow]
        next_letter = random_word_list_cow[current_index_cow]
        current_index_cow += 1

    if current_index_cow == len(random_word_list_cow):
        print("Cow word complete!")
        new_word = ""
        random_word_cow = random.choice(word_list_cow)
        random_word_list_cow = list(random_word_cow)
        current_index_cow = 0
        print(f"Cow = {random_word_cow}")
    pass

def type_word(word: str, color,new_color, x_word_pos: float, y_word_pos: float, font_size: int):
    """
    Displays a word on screen and tracks user typing progress.

    The function shows the target word in black and the correctly typed letters
    in white overlaid on top. When the user types the correct letter, it's added
    to the display. Once the entire word is typed correctly (marked by a '.'
    terminator), the game state transitions to GAMEPLAY.

    :param word: The target word that the user needs to type
    :param color: The color of the text
    :param new_color: The new color of the text
    :param y_word_pos: The y-coordinate position where the word will be drawn
    :param x_word_pos: The x-coordinate position where the word will be drawn
    :param font_size: The size of the font for displaying the word
    :return: None
    """
    global word_list_index, new_word, next_letter

    engine.set_font_size(font_size)
    engine.color = color
    engine.draw_text(f"{word}", x_word_pos, y_word_pos)

    word = word.lower()
    word_list = list(word)
    word_list.append(".")

    engine.set_font_size(font_size)
    engine.color = new_color
    engine.draw_text(f"{new_word}", x_word_pos, y_word_pos)

    if engine.key == word_list[word_list_index]:
        new_word = new_word + word_list[word_list_index]
        next_letter = word_list[word_list_index]
        word_list_index += 1

def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    draw_word(f"{random_word_cow}", 100, 100, 50)

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
