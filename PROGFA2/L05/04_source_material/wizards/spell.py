
class Spell:
    def __init__(self, name, level_requirement, mana_cost, color_code: int = 31):
        """
        :param name: Name of the spell that can be casted.
        :param level_requirement: The minimum level a wizard must have to be able to cast this spell.
        :param mana_cost: The mana cost to buy this spell.
        :param color_code: The ANSII color code in which to display this spell; 31 by default.
        """
        self.name = name
        self.level_requirement = level_requirement
        self.mana_cost = mana_cost
        self.color = color_code

    def __str__(self):
        return f"\033[{self.color}m{self.name}\033[0m"
