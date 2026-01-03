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

cow_y = 180
horse_y = engine.height - 100
chicken_y = (horse_y + cow_y) / 2

random_animal_alpha : list[float] = []
random_animal_despawn : list[bool] = []

# New word color
word_color_cow = (0, 1, 0)
word_color_chicken = (0, 1, 0)
word_color_horse = (0, 1, 0)

# Difficulty screen
x_difficulty = 100
width_difficulty = (engine.width - x_difficulty * 2) / 3 - (20 / 3)
height_difficulty = 300
y_difficulty = 150

# SCORE
score = 5
word_count = 0
faults = 0

# TIMER
timer = 0
seconds = 0

timer_animal = 0

sunset_color = 1, 0.65, 0


# IMAGES
# -----------------
# Fonts
mono_font = "resources/fonts/PixeloidMono.ttf"
normal_font = "resources/fonts/PixeloidSans.ttf"
bold_font = "resources/fonts/PixeloidSans-Bold.ttf"
title_font = "resources/fonts/AnalogWhispers.ttf"

engine.set_font(normal_font)

# BACKGROUNDS
start_background = engine.load_image("resources/img/start_background.png")
normal_background = engine.load_image("resources/img/normal_background.png")


# DIFFICULTY
title_background_difficulty = engine.load_image("resources/img/title_background_difficulty.png")

difficulty_easy = engine.load_image("resources/img/difficulty_easy.png")
difficulty_medium = engine.load_image("resources/img/difficulty_medium.png")
difficulty_hard = engine.load_image("resources/img/difficulty_hard.png")

# COLORS
# -----------------
primary_text_clr = (0.24, 0.15, 0.19)
highlight_clr = (0.8, 0.87, 0.42)

# -----------------
# Helper functions
# -----------------

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """

    pass




# -----------------
# Draw functions
# -----------------

def draw_word(animal: str, x: int | float, y: int | float, font_size: int = 20):
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

    for index, animal in enumerate(random_animal_list):
        engine.color = 0, 0, 0, random_animal_alpha[index]

        if animal == "cow":
            animal_y = cow_y
        elif animal == "chicken":
            animal_y = chicken_y
        else:
            animal_y = horse_y

        engine.draw_text(
            animal,
            random_animal_x[index],
            animal_y,
            True
        )

        engine.shape_mode = ShapeMode.CENTER
        if animal == "cow":
            engine.color = 0, 1, 0
        elif animal == "chicken":
            engine.color = 1, 0, 0
        engine.draw_rectangle(random_animal_x[index], animal_y,100, 50, False)

# SCREENS
def start_screen():
    engine.shape_mode = ShapeMode.CORNER
    start_background.draw_fixed_size(0, 0, engine.width, engine.height, False)
    engine.color = 0, 0, 0

    engine.set_font_size(50)
    # engine.draw_text('Moo-ve your fingers', engine.width/2, engine.height/4, True)

    engine.set_font_size(25)
    engine.set_font(bold_font)
    # Shadow
    engine.color = primary_text_clr
    engine.draw_text('Press any key to play_', engine.width - 228, engine.height - 67, True)
    engine.color = highlight_clr
    engine.draw_text('Press any key to play_', engine.width - 225, engine.height - 70, True)

def difficulty_screen():
    engine.shape_mode = ShapeMode.CORNER
    normal_background.draw_fixed_size(0, 0, engine.width, engine.height, False)

    engine.set_font(title_font)
    engine.set_font_size(60)

    engine.shape_mode = ShapeMode.CENTER
    # engine.draw_rectangle(engine.width / 2, 75, 550, 76, False)
    title_background_difficulty.draw_fixed_size(engine.width / 2, 75, 550 * 1.2, 76 * 1.2, False)
    engine.shape_mode = ShapeMode.CORNER
    engine.color = highlight_clr
    engine.draw_text("CHOOSE DIFFICULTY", engine.width / 2 - 3, 77 + 3, True)
    engine.color = primary_text_clr
    engine.draw_text("CHOOSE DIFFICULTY", engine.width / 2, 77, True)

    # EASY
    # engine.draw_rectangle(x_difficulty, y_difficulty, width_difficulty, height_difficulty, False)
    difficulty_easy.draw_fixed_size(x_difficulty - 10, y_difficulty, width_difficulty, height_difficulty, False)
    # MEDIUM
    # engine.draw_rectangle(x_difficulty + 200 + 10, y_difficulty, width_difficulty, height_difficulty, False)
    difficulty_medium.draw_fixed_size(x_difficulty + 200 + 10, y_difficulty, width_difficulty, height_difficulty, False)
    # HARD
    # engine.draw_rectangle(x_difficulty + 200 * 2 + 20, y_difficulty, width_difficulty, height_difficulty, False)
    difficulty_hard.draw_fixed_size(x_difficulty + 200 * 2 + 30, y_difficulty, width_difficulty, height_difficulty,
                                    False)

    # Go back button
    engine.shape_mode = ShapeMode.CENTER
    engine.draw_rectangle(100, engine.height - 75, 100, 50, False)

def gameplay_screen():
    engine.background_color = sunset_color

    draw_score()
    draw_word_count()
    draw_type_animal()
    draw_timer()

    # Number word change
    if current_difficulty == GameDifficulty.EASY:
        draw_word("cow", engine.width - 150, cow_y - 75)
    elif current_difficulty == GameDifficulty.MEDIUM:
        draw_word("cow", engine.width - 150, cow_y - 75)
        draw_word("chicken", engine.width - 150, chicken_y - 75)
    elif current_difficulty == GameDifficulty.HARD:
        draw_word("cow", engine.width - 150, cow_y - 75)
        draw_word("chicken", engine.width - 150, chicken_y - 75)
        draw_word("horse", engine.width - 150, horse_y - 75)

def gameover_screen():
    engine.background_color = 1, 0, 0
    engine.shape_mode = ShapeMode.CENTER
    engine.draw_text("Your animals are sad", engine.width / 2, engine.height / 2, True)
    engine.draw_text(f"Word count: {word_count}", engine.width / 2, 300, True)
    engine.draw_text(f"Wrongly typed letters: {faults}", engine.width / 2, 350, True)

def highscore_screen():
    engine.background_color = 0, 1, 0
    engine.color = 0, 0, 0
    engine.draw_text("Your animals are happy!!", engine.width / 2, 50, True)
    engine.draw_text(f"Word count: {word_count}", engine.width / 2, 300, True)
    engine.draw_text(f"Wrongly typed letters: {faults}", engine.width / 2, 350, True)

def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    global current_difficulty, current_state


    if current_state == GameState.START:
        start_screen()

    elif current_state == GameState.DIFFICULTY:
        difficulty_screen()

    elif current_state == GameState.GAMEPLAY:
        gameplay_screen()

    elif current_state == GameState.GAMEOVER:
        gameover_screen()

    elif current_state == GameState.HIGHSCORE:
        highscore_screen()
    pass

def add_random_animal():
    global timer_animal

    timer_animal += 1 / 60

    if timer_animal > 2 and len(random_animal_list) < 5:
        allowed_animals = ANIMALS_BY_DIFFICULTY[current_difficulty]
        random_animal = random.choice(allowed_animals)
        random_animal_list.append(random_animal)

        random_animal_x.append(-100)
        random_animal_y.append(random.uniform(30, engine.height - 150))

        random_animal_alpha.append(1.0)
        random_animal_despawn.append(False)

        timer_animal = 0

def move_animal():
    global score, current_state

    for index in range(len(random_animal_x) - 1, -1, -1):

        if random_animal_despawn[index]:
            random_animal_alpha[index] -= 0.1   # fade out

            if random_animal_alpha[index] <= 0:
                random_animal_list.pop(index)
                random_animal_x.pop(index)
                random_animal_y.pop(index)
                random_animal_alpha.pop(index)
                random_animal_despawn.pop(index)
        else:
            random_animal_x[index] += 1

            if random_animal_x[index] > engine.width - 250:
                random_animal_list.pop(index)
                random_animal_x.pop(index)
                random_animal_y.pop(index)
                random_animal_alpha.pop(index)
                random_animal_despawn.pop(index)

                if score > 0:
                    score -= 1
                else:
                    current_state = GameState.GAMEOVER


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
        move_animal()
        print(random_animal_alpha)
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
    for index in range(len(random_animal_list)):
        if random_animal_list[index] == kind and not random_animal_despawn[index]:
            random_animal_despawn[index] = True
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
        if current_difficulty == GameDifficulty.HARD:
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
    global current_state, score, timer
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
        timer = 0
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
