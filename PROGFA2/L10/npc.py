import random
from dae_progfa_lib import ProgfaEngine, ShapeMode

from map import Map
from enum import Enum
from pathlib import Path

class DialogueProgression(Enum):
    NO = 0,
    BEGIN = 1,
    CONVERSATION = 2,
    FINISHED = 3
dialogue_state = DialogueProgression.NO

class NPC:
    def __init__(self, name : str, map : Map, engine: ProgfaEngine):
        self.engine = engine
        self.map = map
        self.name = name
        self.progression = dialogue_state
        self._load_dialogue()
        self.invite_counted = False
        row, col = self.map.get_random_walkable_tile()

        self.x = col * self.map.CELL_SIZE
        self.y = row * self.map.CELL_SIZE

        self.size = self.map.CELL_SIZE
        self.color = random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)

        print(self.x)


    def display(self):
        self.engine.shape_mode = ShapeMode.CORNER
        self.engine.color = self.color
        self.engine.draw_square(self.x, self.y, self.size, 0)

    def _load_dialogue(self):
        self.dialogue_data = {}

        file = Path("resources/csv_files/dialogue") / f"{self.name}.txt"

        state = None

        for line in file.read_text(encoding="utf-8").splitlines():
            line = line.strip()

            if line.startswith("[") and line.endswith("]"):
                state = line[1:-1]
                self.dialogue_data[state] = []

            elif line and state:
                self.dialogue_data[state].append(line)

    def draw_dialogue(self):
        if self.progression in (
                DialogueProgression.NO,
                DialogueProgression.FINISHED
        ):
            return

        self.engine.color = 0, 0, 0, 0.8
        self.engine.shape_mode = ShapeMode.CORNER
        self.engine.draw_rectangle(
            25,
            self.engine.height - 225,
            500,
            200,
            0
        )

        self.engine.color = 1, 1, 1
        self.engine.set_font_size(20)

        self.engine.draw_text(
            self.name,
            50,
            self.engine.height - 200,
            False
        )

        if self.progression == DialogueProgression.BEGIN:
            lines = self.dialogue_data["BEGIN"]

        elif self.progression == DialogueProgression.CONVERSATION:
            lines = self.dialogue_data["CONVERSATION"]

        else:
            lines = []

        y = self.engine.height - 170
        for line in lines:
            self.engine.draw_text(line, 50, y, False)
            y += 30

        self.engine.draw_text("(press ENTER to continue)", 280, self.engine.height - 60, False)

    def start_dialogue(self):
        if self.progression == DialogueProgression.NO:
            self.progression = DialogueProgression.BEGIN


    def progress_dialogue(self, key):
        if key == "ENTER":
            if self.progression == DialogueProgression.BEGIN:
                self.progression = DialogueProgression.CONVERSATION
            elif self.progression == DialogueProgression.CONVERSATION:
                self.progression = DialogueProgression.FINISHED
            
    def can_move(self) -> bool:
        if not (self.progression == DialogueProgression.NO or self.progression == DialogueProgression.FINISHED):
            print(self.progression)
            return False
        return True

    def minus_invite(self):
        if (
                self.progression == DialogueProgression.FINISHED
                and not self.invite_counted
        ):
            self.invite_counted = True
            return 1

        return 0