import random


def get_wizard_name(full_name: str) -> str:
    """
    This function ges a full name and returns a wizard name.
    :param full_name: input from the user
    :return: string, wizard name
    """
    wizard_prefixes = ("Grand", "Mysterious", "Archmage", "Elder", "Sorcerer",
                       "Enchanter", "Warlock")
    wizard_suffixes = ("of the Myst", "the Wise", "the All-Knowing", "of the Eternal Flame", "the Spellbinder")

    first_name, last_name = full_name.split()
    prefix = random.choice(wizard_prefixes)
    suffix = random.choice(wizard_suffixes)
    return f"{prefix} {first_name} {suffix}"

def get_colored_text(text: str, color_code: int) -> str:
    """
    This function gets a text and a specified color code
    :param text: text of type string
    :param color_code: color code of type int
    :return: colored text, using the given color
    """
    prefix = f"\033[{color_code}m"
    suffix = f"\033[0m"
    return f"{prefix}{text}{suffix}"

#result of return functions should be saved in a variable (or printed)
result = get_wizard_name("Anna-Kyra Strik")
print(result)

your_name = input("Enter your full name and let the story begin: ")
print(get_wizard_name(your_name))

print(f"{get_wizard_name(your_name)} "
      f"casts a spell on {get_colored_text("Fizzling Fluffstorm", 91)}!")
print(f"{get_wizard_name(your_name)} "
      f"casts a spell on {get_colored_text("Sizzling Puffstorm", 94)}!")
