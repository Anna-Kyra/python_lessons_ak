from dae_progfa_lib import ProgfaEngine

class Pokemon:
    def __init__(self, id : int, name : str, type : str, generation : int, legendary : bool, image_name : str, engine: ProgfaEngine):
        self.id = id
        self.name = name
        self.type = type
        self.generation = generation
        self.legendary = legendary
        image_path = f"Resources/pokemon/{image_name}.png"
        self.image = engine.load_image(image_path)

    def __str__(self):
        return f"{self.id} : {self.name.upper()} {self.type.split("-")} -- GEN {self.generation} --"

    def _draw_type(self, engine: ProgfaEngine, x: float, y: float, poke_type: str):
        """
        Draws a rectangle of SIZE: 60 x 18 in the requested position (x,y).
        The color of the rectangle is determined by the type (look up in dictionary).
        Next, the poke_type name is drawn on top of it in WHITE, font size 13.
        :param x: the x position (left) to draw the colored type block in
        :param y: the y position (top) to draw the colored type block in
        :param poke_type: the type name of the pokemon (Grass, Normal,..)
        """
        # TODO: finish method to use given dictionary and draw type rectangle (see docstring).
        type_colors = {
            "Normal": (0.64, 0.67, 0.69),
            "Grass": (0.61, 0.8, 0.31),
            "Poison": (0.73, 0.5, 0.79),
            "Water": (0.27, 0.57, 0.77),
            "Flying": (0.24, 0.78, 0.94),
            "Fire": (0.99, 0.49, 0.14),
            "Bug": (0.45, 0.62, 0.25),
            "Ghost": (0.48, 0.38, 0.64),
            "Electric": (0.93, 0.84, 0.21),
            "Dragon": (0.95, 0.43, 0.34),
            "Fighting": (0.84, 0.4, 0.14),
            "Steel": (0.62, 0.72, 0.72),
            "Fairy": (0.99, 0.73, 0.91),
            "Psychic": (0.95, 0.4, 0.73),
            "Ground": (0.97, 0.87, 0.25),
            "Ice": (0.32, 0.77, 0.91),
            "Rock": (0.64, 0.55, 0.13),
            "Dark": (0.44, 0.44, 0.44),
        }

        width = 60
        height = 18

        color = type_colors.get(poke_type, (0.5, 0.5, 0.5))
        engine.color = color
        engine.draw_rectangle(x, y, width, height)

        engine.color = (1, 1, 1)
        engine.draw_text(poke_type, x + 5, y + 13, 13)

        # self.engine = engine
        # self.x = x
        # self.y = y
        # self.poke_type = type_colors[self.type.split("-")]
        # self.poke_color = type_colors[poke_type]
        # self.image.draw(x, y)
        # self.type_color = type_colors[self.type.split("-")]

        # print(self.image)

    def display(self, x : float, y : float):
        


