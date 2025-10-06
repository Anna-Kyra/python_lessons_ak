import random

hogwarts_houses = ("Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin")
spells = ("Accio", "Expelliarmus", "Expecto Patronum", "Avada Kedavra", "Wingardium Leviosa", "Crucio", "Alohomora", "Lumos", "Stupefy")
students = (
            ("Harry", "Potter"),
            ("Hermione", "Granger"),
            ("Ron", "Weasley"),
            ("Draco", "Malfoy"),
            ("Neville", "Longbottom"),
            ("Luna", "Lovegood"),
            ("Ginny", "Weasley"),
            ("Fred", "Weasley"),
            ("George", "Weasley"),
            ("Cedric", "Diggory"),
            ("Cho", "Chang"),
            ("Seamus", "Finnigan"),
            ("Dean", "Thomas"),
            ("Lavender", "Brown"),
            ("Pansy", "Parkinson"),
            ("Parvati", "Patil"),
            ("Padma", "Patil")
        )

friend = random.choice(students)
friend_first_name, friend_last_name = friend

enemy = random.choice(students)
enemy_first_name, enemy_last_name = enemy


def assign_house():
    """
    Randomly asigns hogwarts house
    :return:
    """
    print(f"The sorting hat has spoken! Welcome to {random.choice(hogwarts_houses)}")

def favorite_spell():
    """
    Randomly get a favorite spell
    :return:
    """
    print(f'Your wand hums with power every time you cast your favorite spell: "{random.choice(spells)}"!')

def show_frenemy():
    """
    Randomly generate friend and enemy
    :return:
    """
    print(f"Your new best friend is {friend_first_name} {friend_last_name},\n"
          f"\u2014\u2014\u2014 but watch out - {enemy_first_name} {enemy_last_name} may not have your best interest at heart!")


assign_house()
favorite_spell()
show_frenemy()
