#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 5-1-2026

@author: anna-kyra
"""

# Anna-Kyra Strik, 22N, V1

import dae_progfa_lib as pfe
from dae_progfa_lib import MouseButton, ShapeMode

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(900, 540)

# Set the frame rate to x frames per second:
engine.fps = 60

animal_names = ["Buddy", "Quacky", "Snork", "Clucky", "Flopsy", "Snickers"]
animal_images = []
animal_width = 83
animal_height = 117

adoption_list = []

hit_detection = -1

# for animal_name in animal_names:
#     animal_images.append(f"{animal_name.lower()}.png")
for animal_name in animal_names:
    animal_images.append(f"images/{animal_name.lower()}.png")

print(animal_images)


animal_position_x = [765, 42, 764, 134, 35, 129]
animal_position_y = [44, 41, 205, 43, 208, 213]

adoption_phrases = [
    "I promise to be your best buddy!",
    "I’ll be your feathered friend forever!",
    "Let’s have mud baths together!",
    "I lay eggs of love, adopt me!",
    "I’m soft, fluffy, and ready to cuddle!",
    "I’ll purr my way into your heart!"]

chosen_phrase = ""

# LOAD IMAGES
background = engine.load_image("images/adopt.png")

for index, image in enumerate(animal_images):
    animal_images[index] = engine.load_image(image)

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """

    pass


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    background.draw_fixed_size(0, 0, engine.width, engine.height, False)

    for index, (x, y) in enumerate(zip(animal_position_x, animal_position_y)):
        animal_images[index].draw(x, y)

    for index, animal in enumerate(adoption_list):
        animal_images[index].draw_fixed_size(40 + (40 * index),engine.height- 40, 40, 40)

    engine.set_font_size(32)
    engine.color = 1, 1, 1
    engine.draw_text(f"{chosen_phrase}", engine.width / 2, engine.height / 2 - 100, True)
    if hit_detection == -1:
        print("geen dier gekozen")
    else:
        animal_images[hit_detection].draw(engine.width/2, animal_position_y[4])
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
    global chosen_phrase, hit_detection

    for index, (button_x, button_y, animal, phrase) in enumerate(zip(animal_position_x, animal_position_y, animal_names, adoption_phrases)):
        if engine.colliding_point_in_rect(mouse_x, mouse_y, button_x, button_y, animal_width, animal_height):
            print(f"clicked {animal}")
            chosen_phrase = phrase
            print(chosen_phrase)
            hit_detection = index


    pass


def key_up_event(key: str):
    """
    This function is only executed once each time a key was released!
    Special keys have more than 1 character, for example ESCAPE, BACKSPACE, ENTER, ...
    """
    if key == "ENTER" and hit_detection >= 0:
        adoption_list.append(animal_names[hit_detection])
        print(adoption_list)

    if key == "BACKSPACE":
        adoption_list.clear()

    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
