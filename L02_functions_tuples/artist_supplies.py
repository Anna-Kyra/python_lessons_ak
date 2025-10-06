import random

digital_supplies = ("tablet", "stylus", "drawing software", 12, 3.14159, "digital brush", "monitor", ("canvas", "easle"))
number_supplies = len(digital_supplies)

print(f"I have about {number_supplies} things I love to use as a technical artist, \n"
      f"but the {random.choice(digital_supplies)} is my favorite!\n"
      f"- The first thing I always use is the {digital_supplies[0]}.\n"
      f"- The last thing I use is the {digital_supplies[-1]}.")

more_info = int(input(f"Which supply would you like more information about? [0,{number_supplies}] "))
print(f"=> '{digital_supplies[more_info]}' is of type {type(digital_supplies[more_info])}")