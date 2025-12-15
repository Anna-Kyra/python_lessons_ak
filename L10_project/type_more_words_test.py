#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 8-12-2025

@author: anna-
"""

import dae_progfa_lib as pfe
from dae_progfa_lib import MouseButton
import random

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 600)

# Set the frame rate to x frames per second:
engine.fps = 60

# SPAWNING WORDS
# Lists
word_list_cow = ["cow", "cheese", "milk", "leather", "meat", "four stomachs", "strong smell", "peripheral vision", "zoomies", "mooo"]
word_list_chicken = ["chicken", "hen", "egg", "seeds", "bird", "rooster", "feathers", "chick"]
word_list_horse = ["horse", "neh", "carrot", "sugar cube", "saddle", "cowboy", "equipment", "helmet", "riding"]

# Randomise
random_word_cow = random.choice(word_list_cow)
random_word_chicken = random.choice(word_list_chicken)
random_word_horse = random.choice(word_list_horse)

# Chosen word lists
random_word_list_cow = list(random_word_cow)
random_word_list_chicken = list(random_word_chicken)
random_word_list_horse = list(random_word_horse)

# Current index
current_index_cow = 0
current_index_chicken = 0
current_index_horse = 0

print(f"Cow = {random_word_cow}")
print(f"Chicken = {random_word_chicken}")
print(f"Horse = {random_word_horse}")

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


def key_up_event(key: str):
    """
    This function is only executed once each time a key was released!
    Special keys have more than 1 character, for example ESCAPE, BACKSPACE, ENTER, ...
    """
    global current_index_cow, random_word_cow, random_word_list_cow
    global current_index_chicken, random_word_chicken, random_word_list_chicken
    global current_index_horse, random_word_horse, random_word_list_horse
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
            else:
                colored_word_cow += letter
        print(f"Cow = {colored_word_cow}")

        if current_index_cow == len(random_word_list_cow):
            print("Cow word complete!")
            random_word_cow = random.choice(word_list_cow)
            random_word_list_cow = list(random_word_cow)
            current_index_cow = 0
            print(f"Cow = {random_word_cow}")

    # CHICKEN
    if key.lower() == random_word_list_chicken[current_index_chicken]:
        correct = True
        current_index_chicken += 1

        colored_word_chicken = ""
        for index, letter in enumerate(random_word_list_chicken):
            if index < current_index_chicken:
                colored_word_chicken += f"{prefix}{letter}{suffix}"
            else:
                colored_word_chicken += letter
        print(f"Chicken = {colored_word_chicken}")

        if current_index_chicken == len(random_word_list_chicken):
            print("Chicken word complete!")
            random_word_chicken = random.choice(word_list_chicken)
            random_word_list_chicken = list(random_word_chicken)
            current_index_chicken = 0
            print(f"Chicken = {random_word_chicken}")

    # HORSE
    if key.lower() == random_word_list_horse[current_index_horse]:
        correct = True
        current_index_horse += 1

        colored_word_horse = ""
        for index, letter in enumerate(random_word_list_horse):
            if index < current_index_horse:
                colored_word_horse += f"{prefix}{letter}{suffix}"
            else:
                colored_word_horse += letter
        print(f"Horse = {colored_word_horse}")

        if current_index_horse == len(random_word_list_horse):
            print("Horse word complete!")
            random_word_horse = random.choice(word_list_horse)
            random_word_list_horse = list(random_word_horse)
            current_index_horse = 0
            print(f"Horse = {random_word_horse}")

    print(correct)
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
