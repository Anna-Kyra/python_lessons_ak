import dae_progfa_lib as pfe
from dae_progfa_lib import ShapeMode, MouseButton
from dae_progfa_lib import MouseButton
from typing import List

from pygame.examples.cursors import image_name

from pokemon import Pokemon

from pathlib import Path
import csv

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(500, 600)

# Set the frame rate to x frames per second:
# engine.set_fps(60)

# TODO: fill this list of pokemon with the data from the csv! (create load_pokemon function)
all_pokemon: List[Pokemon] = []
# pokemon_csv = "data/pokemon.csv"  # WARNING: all pokemon; loading takes a while!
pokemon_csv = "data/pokemon_selection.csv"  # selection of pokemon to limit loading time

path = Path(pokemon_csv)


with path.open("r") as file:
    reader = csv.DictReader(file)
    print(reader.fieldnames)

    for pokemon_row in reader:
        id = pokemon_row["#"]
        name = pokemon_row["Name"]
        type = pokemon_row["Type"]
        generation = pokemon_row["Generation"]
        legendary = pokemon_row["Legendary"]
        image_name = f"{id}-{name}"

        pokemon = Pokemon(id, name, type, generation, legendary, image_name, engine)

        all_pokemon.append(pokemon)

# print(all_pokemon[0])
# for pokemon in all_pokemon:
#     # print(pokemon)
#     pokemon
#     # print(pokemon.type_color)

def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """
    pass


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    engine.background_color = 1, 1, 1

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
