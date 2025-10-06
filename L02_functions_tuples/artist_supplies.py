import random

def favorite_supplies():
    digital_supplies = ("tablet", "stylus", "drawing software", 12, 3.14159, "digital brush", "monitor",
                        ("canvas", "easle"))
    number_supplies = len(digital_supplies)
    print(f"I have about {number_supplies} things I love to use as a technical artist, \n"
      f"but the {random.choice(digital_supplies)} is my favorite!\n"
      f"- The first thing I always use is the {digital_supplies[0]}.\n"
      f"- The last thing I use is the {digital_supplies[-1]}.")

favorite_supplies()


def supply_info():
    supply_box = ("tablet", "stylus", "drawing software", 12, 3.14159, "digital brush", "monitor",
                    ("canvas", "easel"))
    number_supply_box = len(supply_box)
    more_info = int(input(f"Which supply would you like more information about? [0,{number_supply_box}] "))
    print(f"=> '{supply_box[more_info]}' is of type {type(supply_box[more_info])}")

supply_info()

