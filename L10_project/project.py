#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2-12-2025

@author: anna-
"""
import random
import dae_progfa_lib as pfe
from collections import Counter
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
class Animal:
    def __init__(self, kind: str, x: float, y: float, speed: float):
        self.kind = kind      # "cow", "chicken", "horse"
        self.x = x
        self.y = y
        self.speed = speed

animals_easy = "cow"
animals_medium = "cow", "chicken"
animals_hard = "cow", "chicken", "horse"

if current_difficulty == GameDifficulty.MEDIUM:
    random_animal = random.choice(animals_medium)
elif current_difficulty == GameDifficulty.HARD:
    random_animal = random.choice(animals_hard)

random_animal_list : list[str] = [random_animal,]
random_animal_counter = Counter([random_animal])
animals: list[Animal] = []

animal_type = random.choice(animals_hard)
new_animal = Animal(animal_type, 0, 200, 2)
animals.append(new_animal)

random_animal_counter[animal_type] += 1


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

# Spritesheet test
sprite_columns = 12
sprite_rows = 15
spritesheet = engine.load_image("images/among_us_hats.png")
spritesheet.resize(1300, 1300)

all_frames = spritesheet.cut_all_frames(sprite_rows, sprite_columns)
cow_img = all_frames[0]
chicken_img = all_frames[1]
horse_img = all_frames[2]

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

    #
    y = 10

    if current_difficulty == GameDifficulty.EASY:
        engine.draw_text(f"{animals_easy}", engine.width / 2, y, True)
    elif current_difficulty == GameDifficulty.MEDIUM:
        for animal in animals:
            print(animal.kind)
            if animal.kind == "cow":
                cow_img.draw(engine.width/2, 20)
            elif animal.kind == "chicken":
                chicken_img.draw(engine.width/2, 20)



    elif current_difficulty == GameDifficulty.HARD:
        # for index, animal in enumerate(random_animal_list):
        #     engine.draw_text(f"{animal}", engine.width / 2, y, True)
        text = ", ".join(f"{animal}: {count}"
                         for animal, count in random_animal_counter.items()
                         if count > 0)
        engine.draw_text(text, engine.width / 2, y, True)


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
    global random_animal, timer_animal

    timer_animal += 1 / 60

    if timer_animal > 2:
        if current_difficulty == GameDifficulty.MEDIUM:
            random_animal = random.choice(animals_medium)
        elif current_difficulty == GameDifficulty.HARD:
            random_animal = random.choice(animals_hard)

        random_animal_counter[random_animal] += 1
        timer_animal = 0
    pass



# def move_random_animal():
#     """
#     Beweegt alle crewmates richting de rechterkant.
#     Als een crewmate buiten beeld gaat, keert hij links terug.
#     :return:
#     """
#     # Om crwemate te verplaatsen / restten: index, x breedte
#     for index, x, animal in enumerate(zip(random_animal_x, random_animal_list)):
#         random_animal_x[index] += 4
#     pass

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
        for animal in animals:
            animal.x += animal.speed

        # move_random_animal()
    pass

# -----------------
# Game logic
# -----------------

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
            current_state = GameState.GAMEPLAY
        # MEDIUM
        elif on_medium:
            current_difficulty = GameDifficulty.MEDIUM
            current_state = GameState.GAMEPLAY
        elif on_hard:
            current_difficulty = GameDifficulty.HARD
            current_state = GameState.GAMEPLAY
    pass

def remove_one_animal(kind: str):
    for animal in animals:
        if animal.kind == kind:
            animals.remove(animal)
            return True
    return False

def type_word(key: str):
    global current_index_cow, random_word_cow, random_word_list_cow, word_colored_cow
    global current_index_chicken, random_word_chicken, random_word_list_chicken, word_colored_chicken
    global current_index_horse, random_word_horse, random_word_list_horse, word_colored_horse

    global score, current_state, word_count, faults
    global random_animal, random_animal

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
            word_count += 1
            if score < 5:
                score += 1


        elif current_difficulty in (GameDifficulty.MEDIUM, GameDifficulty.HARD):
            if random_animal_counter["cow"] > 0 and remove_one_animal("cow"):
                random_animal_counter["cow"] -= 1
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
        if random_animal_counter["chicken"] > 0 and remove_one_animal("chicken"):
            random_animal_counter["chicken"] -= 1
            word_count += 1
            if score < 5:
                score += 1
        else:
            if score > 0:
                score -= 1
            else:
                current_state = GameState.GAMEOVER

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
        if random_animal_counter["horse"] > 0 and remove_one_animal("horse"):
            random_animal_counter["horse"] -= 1
            word_count += 1
            if score < 5:
                score += 1
        else:
            if score > 0:
                score -= 1
            else:
                current_state = GameState.GAMEOVER

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
