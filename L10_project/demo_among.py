#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 9-12-2025

@author: anna-
"""
import random

import dae_progfa_lib as pfe
from dae_progfa_lib import MouseButton
from dae_progfa_lib.progfa_image import ProgfaImage

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(1200, 600)

# Set the frame rate to x frames per second:
engine.fps = 60

sprite_columns = 12
sprite_rows = 15
spritesheet = engine.load_image("images/among_us_hats.png")
spritesheet.resize(1300, 1300)

# getallen : list[int] = [] # dan weet je wat er in de lege lijst moet zitten

# Opties voor crewmates:
crew_mates : list[ProgfaImage] = []
crew_button_x : list[float] = [] # posities van crewmate knoppen
crew_button_y : list[float] = [] # posities van crewmate knoppen

hats : list[ProgfaImage] = []

ghost : ProgfaImage
timer = 0

# De crewmates gekozen door de gebruiker:
chosen_crew_mates : list[ProgfaImage] = []
chosen_crew_x : list[float] = []
chosen_crew_y : list[float] = []
chosen_crew_hat : list[ProgfaImage] = []

def init_collections():
    """
    Knipt de juiste crewmates uit de spritesheets en stopt dit in crew_mates.
    Knipt de hoedjes uit dezelfde spritesheet en stopt die in hats.
    """
    global crew_mates, crew_button_x, crew_button_y, hats, ghost
    all_frames = spritesheet.cut_all_frames(sprite_rows, sprite_columns)
    crew_mates = all_frames[0:12:1]
    hats = all_frames[12:(11+9*12):1]
    ghost = all_frames[-18]
    distance = crew_mates[0].width + 3
    # Plaats alle crewmate buttons naast elkaar
    for index in range(0, len(crew_mates)):
        crew_button_x.append(index * distance)
        crew_button_y.append(10)

def draw_crew_buttons():
    """
    Tekent alle crewmate button opties in mijn scherm.
    """
    for x, y, image in zip(crew_button_x, crew_button_y, crew_mates):
        image.draw(x, y)

def draw_chosen_crewmates():
    """
    Tekent de crewmates die gekozen zijn door de gebruiker.
    :return:
    """
    for x, y, image, hat in zip(chosen_crew_x, chosen_crew_y, chosen_crew_mates, chosen_crew_hat):
        image.draw(x, y)
        hat.draw(x, y - image.height * 0.4)

def move_chosen_crewmates():
    """
    Beweegt alle crewmates richting de rechterkant.
    Als een crewmate buiten beeld gaat, keert hij links terug.
    :return:
    """
    # Om crwemate te verplaatsen / restten: index, x breedte
    for index, (x, image) in enumerate(zip(chosen_crew_x, chosen_crew_mates)):
        chosen_crew_x[index] += 4
        if chosen_crew_x[index] > engine.width:
            chosen_crew_x[index] = - image.width

def kill_random_crewmate():
    """
    Laat een timer lopen. Om de twee seconden, kiest hij een random index.
    De crewmate afbeelding in die index wordt een geest.
    :return:
    """
    global timer
    timer += 1
    if timer > 2 * engine.fps: # wacht 2 seconden
        if len(chosen_crew_mates) > 0: # Is er wel al een crewmate
            index_to_kill = random.randint(0, len(chosen_crew_mates) - 1)
            chosen_crew_mates[index_to_kill] = ghost
        timer = 0 # begin terug vanaf 0 te tellen/wachten




def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    init_collections()
    pass


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    # crew_mates[0].draw(0, 0)
    # crew_mates[-1].draw(0, 0)
    # hats[-1].draw(0,0)
    engine.background_color = 1, 1, 1
    draw_crew_buttons()
    draw_chosen_crewmates()




    pass


def evaluate():
    """
    This function is being executed over and over, as fast as the frame rate. Use to update (not draw).
    """
    move_chosen_crewmates()
    kill_random_crewmate()

    pass


def mouse_pressed_event(mouse_x: int, mouse_y: int, mouse_button: MouseButton):
    """
    This function is only executed once each time a mouse button was pressed!
    """
    # ik controleer of er op een crewmate button geklikt werd,
    #     zoja: voeg hem to aan de chosen lijst + geef random positie
    for button_x, button_y, button_image in zip(crew_button_x, crew_button_y, crew_mates):
        if engine.colliding_point_in_rect(mouse_x, mouse_y, button_x, button_y, button_image.width, button_image.height):
            # op deze knop geklikt -> image toevoegen + positie genereren
            chosen_crew_mates.append(button_image)
            chosen_crew_x.append(random.uniform(0, engine.width - button_image.width))
            chosen_crew_y.append(random.uniform(100, engine.height - button_image.height))
            chosen_crew_hat.append(random.choice(hats))
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
