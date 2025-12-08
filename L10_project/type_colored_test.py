#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 8-12-2025

@author: anna-
"""
import random

import dae_progfa_lib as pfe
from dae_progfa_lib import MouseButton

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 600)

# Set the frame rate to x frames per second:
engine.fps = 60

# SPAWNING WORDS
word_list = ["cow", "horse", "test", "pig", "chicken"]

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """

    pass


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """

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

random_word = random.choice(word_list)
random_word_list = list(random_word)
print(random_word)

current_index = 0

def key_up_event(key: str):
    """
    This function is only executed once each time a key was released!
    Special keys have more than 1 character, for example ESCAPE, BACKSPACE, ENTER, ...
    """
    # if key.lower() in random_word:
    #     print("yes")
    # else:
    #     print("no")
    # for index in range(0, len(random_word_list)):
    #     print(index)

    # for index, letter in enumerate(random_word_list):
    #     # index = range(0, len(random_word_list))
    #     print(index)
    #     if key.lower() == letter:
    #         print("yes")
    #     else:
    #         print("no")

    # for index, letter in enumerate(random_word_list):
    #     # index = range(0, len(random_word_list))
    #     if key.lower() == letter:
    #         print(f"Matched at index {index}")
    #         break

    global current_index, random_word, random_word_list
    prefix = f"\033[32m"
    suffix = f"\033[0m"

    if key.lower() == random_word_list[current_index]:
        current_index += 1

        colored_word = ""
        for index, letter in enumerate(random_word_list):
            if index < current_index:
                colored_word += f"{prefix}{letter}{suffix}"
            else:
                colored_word += letter
        print(colored_word)

        if current_index == len(random_word_list):
            print("Word Complete!")
            random_word = random.choice(word_list)
            random_word_list = list(random_word)
            current_index = 0
            print(random_word)

    else:
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
