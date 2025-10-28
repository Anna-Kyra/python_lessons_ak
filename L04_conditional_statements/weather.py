# MOMS KNOWS BEST
from unicodedata import category


# def ask_mom(condition: str) -> str:
#     conditions = ("rainy", "sunny", "cold", "snowy", "windy")
#     outfits = ("raincoat", "sun hat", "sweater", "scarf and gloves", "beanie")
#     if conditions[0]:
#         return f"Oh, then you should wear a {outfits[0]}"
#     elif conditions[1]:
#         return f"Oh, then you should wear a {outfits[1]}"
#     elif conditions[2]:
#         return f"Oh, then you should wear a {outfits[2]}"
#     elif conditions[3]:
#         return f"Oh, then you should wear a {outfits[3]}"
#     elif conditions[4]:
#         return f"Oh, then you should wear a {outfits[4]}"
#     else:
#         return "Well.. I have no idea, honey."
#
#     pass
#
# print("[You] Mom, what should I wear?\n"
#       "[MOM] What's the weather like?\n"
#       "('rainy', 'sunny', 'cold', 'snowy', 'windy')")
# weather_today = input("[YOU] It's ")
# print(ask_mom(weather_today))

# WEATHER FORECAST
def weather(kmh: int):
    min_kmh = (0, 5, 29, 50)
    max_kmh = (5, 28, 49, 74)
    category = ("calm", "breeze", "strong breeze", "gale", "storm")
    description = ("No wind, or barely noticeable. Smoke rises straight up, leaves are still.",
                   "Light to moderate breeze. Leaves rustle, small branches move, flags flutter.",
                   "Large branches sway, dust and paper blow around. Difficult to use an umbrella.",
                   "Trees in motion, walking against the wind is hard. Minor structural damage possible.",
                   "Severe winds, tree branches break, roofs and buildings may suffer damage. Dangerous.")

    def wheather_layout(index: int, kmh: int):
        print(f"{category[index].upper()}\n"
              f"{"-" * len(category[index])}\n"
              f"Wind: {kmh} km/h\n"
              f"{description[index]}\n")

    if kmh < min_kmh[0]:
        print("UNDEFINED\n"
              "---------\n"
              f"Wind: {kmh} km/h\n"
              f"Invalid km per hour value (cannot be negative).\n")
    elif min_kmh[0] < kmh < max_kmh[0]:
        wheather_layout(0, kmh)
    elif min_kmh[1] < kmh < max_kmh[1]:
        wheather_layout(1, kmh)
    elif min_kmh[2] < kmh < max_kmh[2]:
        wheather_layout(2, kmh)
    elif min_kmh[3] < kmh < max_kmh[3]:
        wheather_layout(3, kmh)
    elif kmh > max_kmh[3]:
        wheather_layout(4, kmh)

weather(-4)
weather(34)

wind_user = int(input("How strong is the wind (km/h)? "))
weather(wind_user)
