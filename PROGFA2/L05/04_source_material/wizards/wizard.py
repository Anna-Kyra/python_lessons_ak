import random
from pathlib import Path
from spell import Spell

class Wizard:
    def __init__(self, name: str, level: int = 1, mana: int = 100):
        self.name = name
        self.level = level
        self.mana = mana
        self.lost = False

        base_path = Path("messages")
        with (base_path / "low_level.txt").open("r") as file:
            self.low_level_messages = file.readlines()
        with (base_path / "low_mana.txt").open("r") as file:
            self.low_mana_messages = file.readlines()
        with (base_path / "successful_cast.txt").open("r") as file:
            self.successful_cast_messages = file.readlines()


    def cast_spell(self, spell: Spell) -> bool:
        if self.level < spell.level_requirement:
            print(random.choice(self.low_level_messages))
            return False
        elif self.mana < spell.mana_cost:
            print(random.choice(self.low_mana_messages))
            return False
        else:
            self.mana -= spell.mana_cost
            if "gandalf" in self.name.lower() and "you shall not pass" in spell.name.lower():
                # Easter egg (:
                print("\033[1mYOU SHALL NOT PASS THIS COURSE!!! MUAHAHAHA\033[0m")
                from PIL import Image
                image = Image.open('Resources/gandalf.jpg')
                image.show()
            else:
                print(random.choice(self.successful_cast_messages).format(spell_name=spell))
            return True

    def regenerate_mana(self, amount: int = 10):
        self.mana += amount
        return f"{self.name} regenerates {amount} mana."

    def __str__(self):
        return f"-> {self.name} (lvl: {self.level})"