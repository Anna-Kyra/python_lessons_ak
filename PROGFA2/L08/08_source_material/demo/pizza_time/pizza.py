from tabnanny import check


class Topping:
    def __init__(self, name: str, vegetarian: bool):
        self.name = name
        self.vegetarian = vegetarian

    def __str__(self):
        return f"{self.name} (vegetarian: {self.vegetarian})"

    def __repr__(self):
        """Automatically called when printing a list[Topping]"""
        return self.name


# Symbol for veggie pizza 🍃
class Pizza:
    def __init__(self, name : str):
        self.name = name
        self.toppings = []

    def add_topping(self, name : str, vegetarian : bool):
        topping = Topping(name, vegetarian)
        self.toppings.append(topping)

    def add_topping_object(self, topping : Topping):
        self.toppings.append(topping)

    def _is_vegetarian(self) -> bool:
        #verlopen alle toppings, van zodra 1 niet vegetarisch is => False
        topping : Topping
        for topping in self.toppings:
            if not topping.vegetarian:
                return False
        return True

    def __str__(self):
        veggie = ""
        if self._is_vegetarian():
            veggie = "🍃"
        info = f"{self.name} {veggie}\n"
        info += f"\t{self.toppings}"

        return info