#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2-12-2025

@author: anna-
"""
import random
import dae_progfa_lib as pfe
from dae_progfa_lib import MouseButton, ShapeMode
from enum import Enum

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 600)

# Set the frame rate to x frames per second:
engine.fps = 60

# GAME STATE
class GameState(Enum):
    START = 0,
    DIFFICULTY = 1,
    GAMEPLAY = 2,
    GAMEOVER = 3,
    HIGHSCORE = 4
current_state = GameState.START

class GameDifficulty(Enum):
    EASY = 0,
    MEDIUM = 1,
    HARD = 2
current_difficulty = GameDifficulty.HARD

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

# Word colored
word_colored_cow = ""
word_colored_chicken = ""
word_colored_horse = ""

# Current index
current_index_cow = 0
current_index_chicken = 0
current_index_horse = 0

print(f"Cow = {random_word_cow}")
print(f"Chicken = {random_word_chicken}")
print(f"Horse = {random_word_horse}")

# DIFFERENT ANIMALS
animals_easy = "cow"
animals_medium = "cow", "chicken"
animals_hard = "cow", "chicken", "horse"

random_animal_medium = random.choice(animals_medium)
random_animal_hard = random.choice(animals_hard)

# SCORE
score = 5
word_count = 0

def start_screen():
    engine.shape_mode = ShapeMode.CORNER
    engine.color = 0, 0, 0

    engine.set_font_size(50)
    engine.draw_text('Moo-ve your fingers', engine.width/2, engine.height/4, True)

    engine.set_font_size(30)
    engine.draw_text('_Press any key to play_', engine.width/2, engine.height*(3/4), True)

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """

    pass

def draw_word(animal: str, x: int | float, y: int | float, font_size: int = 10):
    engine.set_font_size(font_size)
    color_word = 0, 0, 0

    # COW
    if animal == "cow":
        # Word
        engine.shape_mode = ShapeMode.CORNER
        engine.color = color_word
        engine.set_font_size(50)
        engine.draw_text(f"{random_word_cow.upper()}", x, y, False)

        # Word colored
        engine.shape_mode = ShapeMode.CORNER
        engine.color = 0, 1, 0
        engine.set_font_size(50)
        engine.draw_text(f"{word_colored_cow.upper()}", x, y, False)
    # CHICKEN
    elif animal == "chicken":
        # Word
        engine.shape_mode = ShapeMode.CORNER
        engine.color = color_word
        engine.set_font_size(50)
        engine.draw_text(f"{random_word_chicken.upper()}", x, y, False)

        # Word colored
        engine.shape_mode = ShapeMode.CORNER
        engine.color = 0, 1, 0
        engine.set_font_size(50)
        engine.draw_text(f"{word_colored_chicken.upper()}", x, y, False)
    # HORSE
    elif animal == "horse":
        # Word
        engine.shape_mode = ShapeMode.CORNER
        engine.color = color_word
        engine.set_font_size(50)
        engine.draw_text(f"{random_word_horse.upper()}", x, y, False)

        # Word colored
        engine.shape_mode = ShapeMode.CORNER
        engine.color = 0, 1, 0
        engine.set_font_size(50)
        engine.draw_text(f"{word_colored_horse.upper()}", x, y, False)
    pass

def draw_score():
    engine.color = 0, 0, 0
    engine.draw_text(f"{score}", 20, 20)

def draw_word_count():
    engine.color = 0, 0, 0
    engine.draw_text(f"{word_count}", engine.width - 50, 20)

def draw_type_animal():
    engine.color = 0, 0, 0

    if current_difficulty == GameDifficulty.EASY:
        engine.draw_text(f"{animals_easy}", engine.width / 2, 10, True)
    elif current_difficulty == GameDifficulty.MEDIUM:
        engine.draw_text(f"{random_animal_medium}", engine.width / 2, 10, True)
    elif current_difficulty == GameDifficulty.HARD:
        engine.draw_text(f"{random_animal_hard}", engine.width / 2, 10, True)

def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    global current_difficulty, current_state
    if current_state == GameState.START:
        engine.background_color = 1, 0, 1
        start_screen()

    elif current_state == GameState.DIFFICULTY:
        engine.background_color = 1, 1, 0
        engine.draw_text("CHOOSE DIFFICULTY", engine.width / 2, 100, True)
        #EASY
        engine.draw_rectangle(100, 200, 100, 200, False)

        #MEDIUM
        engine.draw_rectangle(100 * 2 + 10, 200, 100, 200, False)
        #HARD
        engine.draw_rectangle(100 * 3 + 20, 200, 100, 200, False)

    elif current_state == GameState.GAMEPLAY:
        engine.background_color = 0, 1, 1

        draw_score()
        draw_word_count()
        draw_type_animal()

        # Number word change
        if current_difficulty == GameDifficulty.EASY:
            draw_word("cow", 100, 100)
        elif current_difficulty == GameDifficulty.MEDIUM:
            draw_word("cow", 100, 100)
            draw_word("chicken", 200, 200)
        elif current_difficulty == GameDifficulty.HARD:
            draw_word("cow", 100, 100)
            draw_word("chicken", 200, 200)
            draw_word("horse", 300, 300)

    elif current_state == GameState.GAMEOVER:
        engine.background_color = 1, 0, 0
        engine.shape_mode = ShapeMode.CENTER
        engine.draw_text("GAME OVER", engine.width/2, engine.height/2, True)
    elif current_state == GameState.HIGHSCORE:
        engine.background_color = 0, 1, 0
        engine.draw_text("HIGHSCORE", engine.width/2, engine.height/2, True)
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
    global current_difficulty, current_state

    if current_state == GameState.DIFFICULTY:
        #veranderen met variabelen
        on_easy = engine.colliding_point_in_rect(engine.mouse_x, engine.mouse_y, 100, 200, 100, 200)
        on_medium = engine.colliding_point_in_rect(engine.mouse_x, engine.mouse_y, 100 * 2 + 10, 200, 100, 200)
        on_hard = engine.colliding_point_in_rect(engine.mouse_x, engine.mouse_y, 100 * 3 + 20, 200, 100, 200)
        # EASY
        if on_easy:
            current_difficulty = GameDifficulty.EASY
            current_state = GameState.GAMEPLAY
        # MEDIUM
        elif on_medium:
            current_difficulty = GameDifficulty.MEDIUM
            current_state = GameState.GAMEPLAY
        elif on_hard:
            current_difficulty = GameDifficulty.HARD
            current_state = GameState.GAMEPLAY
    pass

def type_word(key: str):
    global current_index_cow, random_word_cow, random_word_list_cow, word_colored_cow
    global current_index_chicken, random_word_chicken, random_word_list_chicken, word_colored_chicken
    global current_index_horse, random_word_horse, random_word_list_horse, word_colored_horse

    global score, current_state, word_count
    global random_animal_medium, random_animal_hard

    correct = False

    # COW
    word_colored_cow = random_word_cow[:current_index_cow]

    if key.lower() == random_word_list_cow[current_index_cow]:
        correct = True
        current_index_cow += 1
        word_colored_cow = random_word_cow[:current_index_cow]
    if current_index_cow == len(random_word_list_cow):
        if current_difficulty == GameDifficulty.MEDIUM:
            if score < 5 and random_animal_medium == "cow":
                score += 1
            elif random_animal_medium == "cow":
                random_animal_medium = random.choice(animals_medium)
                word_count += 1
            elif random_animal_medium != "cow":
                score -= 1
                print("not cow")
        elif current_difficulty == GameDifficulty.HARD:
            if score < 5 and random_animal_hard == "cow":
                score += 1
            elif random_animal_hard == "cow":
                random_animal_hard = random.choice(animals_hard)
                word_count += 1
            elif random_animal_hard != "cow":
                score -= 1
                print("not cow")

        print("Cow word complete!")
        random_word_cow = random.choice(word_list_cow)
        random_word_list_cow = list(random_word_cow)
        current_index_cow = 0
        word_colored_cow = ""

    # CHICKEN
    word_colored_chicken = random_word_chicken[:current_index_chicken]

    if key.lower() == random_word_list_chicken[current_index_chicken]:
        correct = True
        current_index_chicken += 1
        word_colored_chicken = random_word_chicken[:current_index_chicken]
    if current_index_chicken == len(random_word_list_chicken):
        if current_difficulty == GameDifficulty.MEDIUM:
            if score < 5 and random_animal_medium == "chicken":
                score += 1
            elif random_animal_medium == "chicken":
                random_animal_medium = random.choice(animals_medium)
                word_count += 1
            elif random_animal_medium != "chicken":
                score -= 1
                print("not chicken")
        elif current_difficulty == GameDifficulty.HARD:
            if score < 5 and random_animal_hard == "chicken":
                score += 1
            elif random_animal_hard == "chicken":
                random_animal_hard = random.choice(animals_hard)
                word_count += 1
            elif random_animal_hard != "chicken":
                score -= 1
                print("not chicken")

        print("Chicken word complete!")
        random_word_chicken = random.choice(word_list_chicken)
        random_word_list_chicken = list(random_word_chicken)
        current_index_chicken = 0
        word_colored_chicken = ""

    # HORSE
    word_colored_horse = random_word_horse[:current_index_horse]

    if key.lower() == random_word_list_horse[current_index_horse]:
        correct = True
        current_index_horse += 1
        word_colored_horse = random_word_horse[:current_index_horse]
    if current_index_horse == len(random_word_list_horse):
        if current_difficulty == GameDifficulty.MEDIUM:
            if score < 5 and random_animal_medium == "horse":
                score += 1
            elif random_animal_medium == "horse":
                random_animal_medium = random.choice(animals_medium)
                word_count += 1
            elif random_animal_medium != "horse":
                score -= 1
                print("not horse")
        elif current_difficulty == GameDifficulty.HARD:
            if score < 5 and random_animal_hard == "horse":
                score += 1
            elif random_animal_hard == "horse":
                random_animal_hard = random.choice(animals_hard)
                word_count += 1
            elif random_animal_hard != "horse":
                score -= 1
                print("not horse")

        print("Horse word complete!")
        random_word_horse = random.choice(word_list_horse)
        random_word_list_horse = list(random_word_horse)
        current_index_horse = 0
        word_colored_horse = ""

    if not correct:
        print("Wrong:", key)

        if score > 0:
            score -= 1
        else:
            current_state = GameState.GAMEOVER


def key_up_event(key: str):
    """
    This function is only executed once each time a key was released!
    Special keys have more than 1 character, for example ESCAPE, BACKSPACE, ENTER, ...
    """
    global current_state, score
    if current_state == GameState.START and key:
        current_state = GameState.DIFFICULTY

    if current_state == GameState.GAMEPLAY:
        type_word(key)

    # DEBUG
    if key == "1":
        score = 5
        current_state = GameState.START
    elif key == "2":
        score = 5
        current_state = GameState.DIFFICULTY
    elif key == "3":
        score = 5
        current_state = GameState.GAMEPLAY
    elif key == "4":
        score = 5
        current_state = GameState.GAMEOVER
    elif key == "5":
        score = 5
        current_state = GameState.HIGHSCORE
    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
