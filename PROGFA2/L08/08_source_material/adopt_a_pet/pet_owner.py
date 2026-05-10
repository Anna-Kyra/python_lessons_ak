from dae_progfa_lib import ProgfaEngine

class PetOwner:
    def __init__(self, name: str, engine: ProgfaEngine):
        self.name = name
        self.image = engine.load_image(f"Resources/people/{name}.png")

    def __str__(self):
        return f"Hi, my name is {self.name}!"

    def display(self, engine: ProgfaEngine, x: float, y: float):
        self.image.draw(x, y)
        engine.color = 0, 0 ,0
        engine.draw_text(self.name, x, y + self.image.height)

