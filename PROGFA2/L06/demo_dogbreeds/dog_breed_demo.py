#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This demo
"""

import dae_progfa_lib as pfe
from dae_progfa_lib import ShapeMode, MouseButton
from dae_progfa_lib import MouseButton

from dog_breed import DogBreed
from pathlib import Path
from typing import  List
import csv

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(1000, 300)

# Set the frame rate to x frames per second:
# engine.set_fps(60)

dog_breeds: List[DogBreed] = []

def load_breeds():
    """Loads all dog breeds from the given csv files (content folder)."""
    file_path = Path("content/dogbreeds.csv")
    file_path = Path("content/dogbreeds_error.csv")

    with file_path.open("r") as file:
        reader = csv.DictReader(file)
        print(reader.fieldnames)

        for dobreed_row in reader:
            try:
                name = dobreed_row["Name"]
                lifespan = int(dobreed_row["Lifespan"])
                image_name = f"Resources/dogs/{dobreed_row["Image"]}"
                image = engine.load_image(image_name)
                varieties = dobreed_row["Varieties"].split('/')

                dog_breed = DogBreed(name, image, lifespan, varieties)
                dog_breeds.append(dog_breed)
            except ValueError as error:
                print(f"! ERROR in values on line: {dobreed_row}")
            except TypeError as error:
                print(f"! ERROR - incomplete line: {dobreed_row}")


def print_breeds():
    """Prints all dog breeds (auto calls given __str__)"""
    for breed in dog_breeds:
        print(breed)

def render_breeds():
    """Displays all dog breeds in the window, next to each other."""
    for index, breed in enumerate(dog_breeds):
        breed.display(160 * index, 20)


def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    load_breeds()
    print_breeds()

    pass


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    engine.background_color = 1, 1, 1
    render_breeds()
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
