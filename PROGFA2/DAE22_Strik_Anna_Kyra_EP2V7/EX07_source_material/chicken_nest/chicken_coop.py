import dae_progfa_lib as pfe
from dae_progfa_lib import MouseButton, ShapeMode

from chicken import Chicken
from nest import Nest

# Create an instance of ProgfaEngine and set window size (width, height):
engine = pfe.ProgfaEngine(800, 600)

# Set the frame rate to x frames per second:
engine.fps = 60

img_background = engine.load_image('Resources/background.png')
img_nest = engine.load_image('Resources/nest.png')
img_egg = engine.load_image('Resources/egg.png')

nest_x = 100
nest_x_gap = 250
nest_y = 325


Jenny = Nest(nest_x, nest_y, "Jenny", img_nest, img_egg, engine)
Chantal = Nest(nest_x + nest_x_gap, nest_y, "Chantal", img_nest, img_egg, engine)
Henk = Nest(nest_x + (nest_x_gap*2), nest_y, "Henk", img_nest, img_egg, engine)

nests : list[Nest] = [Jenny, Chantal, Henk]

revealed_eggs = {}

for nest in nests:
    revealed_eggs[nest.name] = nest.egg_number

print(revealed_eggs)
def setup():
    """
    Only executed ONCE (at the start); use to load files and initialize.
    """

    pass


def render():
    """
    This function is being executed over and over, as fast as the frame rate. Use to draw (not update).
    """
    engine.shape_mode = ShapeMode.CORNER
    img_background.draw_fixed_size(0, 0, engine.width, engine.height)

    for nest in nests:
        nest.display()
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
    global nest
    if key == "ENTER":
        for nest in nests:
            nest.reveal()
            if nest.has_egg:
                nest.egg_number += 1
                revealed_eggs[nest.name] = nest.egg_number
        print(revealed_eggs)


    elif key == "ESCAPE":
        for nest in nests:
            nest.cover()

    pass


# Engine stuff; best not to mess with this:
engine._setup = setup
engine._evaluate = evaluate
engine._render = render
engine._mouse_pressed_event = mouse_pressed_event
engine._key_up_event = key_up_event

# Start the game loop:
engine.play()
