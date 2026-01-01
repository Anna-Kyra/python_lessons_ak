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

# -----------------
# Globals
# -----------------

# SPAWNING WORDS
# Lists
word_list_cow = ["cow", "calf", "bull", "ox", "milk", "udder", "teat", "moo", "beef", "hide", "horn", "past", "grass", "hay", "farm", "cud", "stall", "brand", "steer", "dairy", "steak", "roast", "rib", "whey", "curds", "cream", "ghee", "filet", "brisk", "cheese", "milk", "leather", "meat", "zoomies", "moo"]
word_list_chicken = ["chick", "hen", "cock", "bird", "eggs", "yolk", "meat", "wing", "wings", "thigh", "leg", "legs", "breast", "broth", "soup", "stock", "roast", "fry", "fried", "grill", "feed", "corn", "peck", "coop", "hatch", "cluck", "beak", "down", "plume"]
word_list_horse = ["horse", "foal", "mare", "stud", "colt", "pony", "mane", "tail", "hoof", "hoofs", "hay", "oats", "grain", "reins", "bit", "spur", "barn", "field", "track", "race", "derby", "trot", "walk", "neigh", "leap", "jump"]

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
ANIMALS_BY_DIFFICULTY = {
    GameDifficulty.EASY: ("cow",),
    GameDifficulty.MEDIUM: ("cow", "chicken"),
    GameDifficulty.HARD: ("cow", "chicken", "horse"),
}

random_animal_list : list[str] = []
random_animal_x : list[float] = []
random_animal_y : list[float] = []

# New word color
word_color_cow = (0, 1, 0)
word_color_chicken = (0, 1, 0)
word_color_horse = (0, 1, 0)

# Difficulty screen
x_difficulty = 100
width_difficulty = (engine.width - x_difficulty * 2) / 3 - (20 / 3)
height_difficulty = 300
y_difficulty = 100

# SCORE
score = 5
word_count = 0
faults = 0

# TIMER
timer = 0
seconds = 0

timer_animal = 0

sunset_color = 1, 0.65, 0

# -----------------
# Helper functions
# -----------------

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """

    pass

def start_screen():
    engine.shape_mode = ShapeMode.CORNER
    engine.color = 0, 0, 0

    engine.set_font_size(50)
    engine.draw_text('Moo-ve your fingers', engine.width/2, engine.height/4, True)

    engine.set_font_size(30)
    engine.draw_text('_Press any key to play_', engine.width/2, engine.height*(3/4), True)

# -----------------
# Draw functions
# -----------------

def draw_word(animal: str, x: int | float, y: int | float, font_size: int = 30):
    global word_color_cow, word_color_chicken, word_color_horse
    engine.set_font_size(font_size)
    color_word = 0, 0, 0

    engine.shape_mode = ShapeMode.CORNER

    # COW
    if animal == "cow":
        # Word
        engine.color = color_word
        engine.draw_text(f"{random_word_cow.upper()}", x, y, False)

        # Word colored
        engine.color = word_color_cow
        engine.draw_text(f"{word_colored_cow.upper()}", x, y, False)

    # CHICKEN
    elif animal == "chicken":
        # Word
        engine.color = color_word
        engine.draw_text(f"{random_word_chicken.upper()}", x, y, False)

        # Word colored
        engine.color = word_color_chicken
        engine.draw_text(f"{word_colored_chicken.upper()}", x, y, False)

    # HORSE
    elif animal == "horse":
        # Word
        engine.color = color_word
        engine.draw_text(f"{random_word_horse.upper()}", x, y, False)

        # Word colored
        engine.color = word_color_horse
        engine.draw_text(f"{word_colored_horse.upper()}", x, y, False)

def draw_score():
    engine.color = 0, 0, 0
    engine.draw_text(f"{score}", 20, 20)

def draw_word_count():
    engine.color = 0, 0, 0
    engine.draw_text(f"{word_count}", engine.width - 50, 20)

def draw_timer():
    engine.color = 0, 0, 0
    engine.draw_text(f"{seconds}", 20, engine.height - 40)

def draw_type_animal():
    engine.color = 0, 0, 0
    y = 10

    if current_difficulty == GameDifficulty.EASY:
        engine.draw_text(f"{random_animal_list}", engine.width / 2, y, True)
        for animal in random_animal_list:
            engine.draw_text(f"{animal}", engine.width / 2, y, True)
            y += 20
    elif current_difficulty == GameDifficulty.MEDIUM:
        engine.draw_text(f"{random_animal_list}", engine.width / 2, y, True)
        y = 30
        for animal in random_animal_list:
            engine.draw_text(f"{animal}", engine.width / 2, y, True)
            y += 20
    elif current_difficulty == GameDifficulty.HARD:
        engine.draw_text(f"{random_animal_list}", engine.width / 2, y, True)

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
        engine.draw_text("CHOOSE DIFFICULTY", engine.width / 2, 50, True)
        engine.shape_mode = ShapeMode.CORNER
        #EASY
        engine.draw_rectangle(x_difficulty, y_difficulty, width_difficulty, height_difficulty, False)
        #MEDIUM
        engine.draw_rectangle(x_difficulty + 200 + 10, y_difficulty, width_difficulty, height_difficulty, False)
        #HARD
        engine.draw_rectangle(x_difficulty + 200 * 2 + 20, y_difficulty, width_difficulty, height_difficulty, False)

        # Go back button
        engine.shape_mode = ShapeMode.CENTER
        engine.draw_rectangle(100, engine.height - 75, 100, 50, False)

    elif current_state == GameState.GAMEPLAY:
        engine.background_color = sunset_color

        draw_score()
        draw_word_count()
        draw_type_animal()
        draw_timer()

        # Number word change
        if current_difficulty == GameDifficulty.EASY:
            draw_word("cow", 50 , engine.height - 150)
        elif current_difficulty == GameDifficulty.MEDIUM:
            draw_word("cow", 50, engine.height - 150)
            draw_word("chicken", engine.width / 3, engine.height - 150)
        elif current_difficulty == GameDifficulty.HARD:
            draw_word("cow", 50, engine.height - 150)
            draw_word("chicken", engine.width / 3, engine.height - 150)
            draw_word("horse", engine.width / 3 * 2, engine.height - 150)

    elif current_state == GameState.GAMEOVER:
        engine.background_color = 1, 0, 0
        engine.shape_mode = ShapeMode.CENTER
        engine.draw_text("Your animals are sad", engine.width/2, engine.height/2, True)
        engine.draw_text(f"Word count: {word_count}", engine.width/2, 300, True)
        engine.draw_text(f"Wrongly typed letters: {faults}", engine.width/2, 350, True)
    elif current_state == GameState.HIGHSCORE:
        engine.background_color = 0, 1, 0
        engine.color = 0, 0, 0
        engine.draw_text("Your animals are happy!!", engine.width/2, 50, True)
        engine.draw_text(f"Word count: {word_count}", engine.width/2, 300, True)
        engine.draw_text(f"Wrongly typed letters: {faults}", engine.width/2, 350, True)
    pass

def add_random_animal():
    global timer_animal

    timer_animal += 1 / 60

    if timer_animal > 2 and len(random_animal_list) < 5:
        allowed_animals = ANIMALS_BY_DIFFICULTY[current_difficulty]
        random_animal = random.choice(allowed_animals)
        random_animal_list.append(random_animal)
        timer_animal = 0

def evaluate():
    """
    This function is being executed over and over, as fast as the frame rate. Use to update (not draw).
    """
    global timer, seconds, current_state, sunset_color

    minute = 60

    if current_state == GameState.GAMEPLAY:
        timer += 1
        seconds = int(timer / 60)

        if seconds == minute / 3:
            sunset_color = 0, 1, 1
        elif seconds == minute / 3 * 2:
            sunset_color = 0, 0, 0.502
        elif seconds == minute:
            current_state = GameState.HIGHSCORE

        add_random_animal()
        # move_random_animal()
    pass

# -----------------
# Game logic
# -----------------

def reset_animals():
    random_animal_list.clear()

def mouse_pressed_event(mouse_x: int, mouse_y: int, mouse_button: MouseButton):
    """
    This function is only executed once each time a mouse button was pressed!
    """
    global current_difficulty, current_state

    if current_state == GameState.DIFFICULTY:
        engine.shape_mode = ShapeMode.CORNER
        on_easy = engine.colliding_point_in_rect(engine.mouse_x, engine.mouse_y, x_difficulty, y_difficulty, width_difficulty, height_difficulty)
        on_medium = engine.colliding_point_in_rect(engine.mouse_x, engine.mouse_y, x_difficulty + 200 + 10, y_difficulty, width_difficulty, height_difficulty)
        on_hard = engine.colliding_point_in_rect(engine.mouse_x, engine.mouse_y, x_difficulty + 200 * 2 + 10 * 2, y_difficulty, width_difficulty, height_difficulty)
        # EASY
        if on_easy:
            current_difficulty = GameDifficulty.EASY
            reset_animals()
            current_state = GameState.GAMEPLAY
        # MEDIUM
        elif on_medium:
            current_difficulty = GameDifficulty.MEDIUM
            reset_animals()
            current_state = GameState.GAMEPLAY
        elif on_hard:
            current_difficulty = GameDifficulty.HARD
            reset_animals()
            current_state = GameState.GAMEPLAY
    pass

def remove_one_animal(kind: str) -> bool:
    """
    Verwijdert precies 1 dier van dit type.
    Geeft True terug als het gelukt is, anders False.
    """
    for index in range(len(random_animal_list)):
        if random_animal_list[index] == kind:
            random_animal_list.pop(index)
            return True
    return False

def type_word(key: str):
    global current_index_cow, random_word_cow, random_word_list_cow, word_colored_cow
    global current_index_chicken, random_word_chicken, random_word_list_chicken, word_colored_chicken
    global current_index_horse, random_word_horse, random_word_list_horse, word_colored_horse

    global score, current_state, word_count, faults

    global word_color_cow, word_color_chicken, word_color_horse

    correct = False

    # COW
    word_colored_cow = random_word_cow[:current_index_cow]

    if key.lower() == random_word_list_cow[current_index_cow]:
        correct = True
        current_index_cow += 1
        word_colored_cow = random_word_cow[:current_index_cow]
        word_color_cow = 0, 1, 0

    if current_index_cow == len(random_word_list_cow):
        # Easy mode
        if current_difficulty == GameDifficulty.EASY:
            if remove_one_animal("cow"):
                word_count += 1
                if score < 5:
                    score += 1
            else:
                if score > 0:
                    score -= 1
                else:
                    current_state = GameState.GAMEOVER

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
        word_color_chicken = 0, 1, 0

    if current_index_chicken == len(random_word_list_chicken):
        if current_difficulty in (GameDifficulty.MEDIUM, GameDifficulty.HARD):
            if remove_one_animal("chicken"):
                word_count += 1
                if score < 5:
                    score += 1
            else:
                score -= 1

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
        word_color_horse = 0, 1, 0

    if current_index_horse == len(random_word_list_horse):
        if current_difficulty in GameDifficulty.HARD:
            if remove_one_animal("horse"):
                word_count += 1
                if score < 5:
                    score += 1
            else:
                score -= 1

        print("Horse word complete!")
        random_word_horse = random.choice(word_list_horse)
        random_word_list_horse = list(random_word_horse)
        current_index_horse = 0
        word_colored_horse = ""

    if not correct:
        print("Wrong:", key)
        faults += 1

        word_color_cow = 1, 0, 0
        word_color_chicken = 1, 0, 0
        word_color_horse = 1, 0, 0

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
        engine.color = 0, 0, 0
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
