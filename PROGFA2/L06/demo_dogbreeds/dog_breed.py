from dae_progfa_lib.progfa_image import ProgfaImage
from typing import List

class DogBreed:
    def __init__(self, name: str,
                       image: ProgfaImage,
                       lifespan: int,
                       coat_varieties: List[str]):
        self.name = name
        self.image = image
        self.lifespan = lifespan
        self.coat_varieties = coat_varieties

    def __str__(self):
        info = f"The {self.name.upper()} has an average lifespan of {self.lifespan} years.\n"
        info += f"\tThe following {len(self.coat_varieties)} coat varieties are officially registered:\n"
        for variety in self.coat_varieties:
            info += f"\t- {variety}\n"
        return info

    def display(self, x: float, y: float):
        self.image.draw(x, y)