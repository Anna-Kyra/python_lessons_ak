from dae_progfa_lib.progfa_image import ProgfaImage
from dae_progfa_lib import  ProgfaEngine

class Pet:
    def __init__(self, name: str, animal_type: str, image: ProgfaImage):
        self.name = name
        self.animal_type = animal_type
        self.image = image

    def __str__(self):
        return f"{self.name} is a {self.animal_type}."


    def display(self, engine: ProgfaEngine, left: float, bottom: float):
        self.image.draw(left, bottom - self.image.height)

        engine.color = 0, 0, 0
        engine.draw_text(self.name, left + 5, bottom - self.image.height - 18)
