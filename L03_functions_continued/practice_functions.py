#PRINT TITLE
import random


def print_title(title: str, symbol: str, times: int):
    """
    Prints title surrounded by a certain symbol
    :param title: name of the title
    :param symbol: A symbol
    :param times: How many times the symbol needs to print
    :return:
    """
    print(f"\n {symbol * times} {title} {symbol * times}")

print_title("Hello world", "*", 10)
print_title("Bye world", "=", 5)

#TIME FOR A COMPLIMENT
def print_compliment() -> str:
    adjectives = ("artful", "nimble", "brilliant", "expressive", "colorful", "clever",
                  "graceful", "innovative", "vibrant")
    nouns = ("programmer", "designer", "coder", "artist", "creator", "developer",
             "visionary", "architect", "maker", "painter")

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"{adjective} {noun}"

compliment = print_compliment()
print_title("time for a compliment", "=", 10)
print(f"Wow, you are one {compliment}!")
print(f"And did you know your neighbour is a {compliment}?")

#LET OPRAH DECIDE
def oprah_quote(sort_present: str) -> str:
    return (f'"You get a {sort_present}, and you get a {sort_present}, and you get a {sort_present}!"'
            f"\n\t\t\"Everybody get's a {sort_present}!\"")

travel_presents = ("first-class flight to Paris", "5-star hotel stay in Bali",
                   "private island getaway",
                   "luxury cruise ticket")
tech_presents = ("fancy smartphone", "smart home speaker", "virtual reality headset", "brand new laptop")
travel = random.choice(travel_presents)
tech = random.choice(tech_presents)

print_title("let_oprah_decide", "=", 10)
print(f'[OPRAH] {oprah_quote(tech)}')
print(f'[OPRAH] {oprah_quote(travel)}')

#WHAT'S MY CHANGE?
def calculate_change(item_cost: int, paid: int) -> float:
    return paid - item_cost

print_title("get_change", "=", 10)
#Example phrase
item_cost = 123
paid = 150
print(f"If the item costs ${item_cost} and the customer pays ${paid}, their change is ${calculate_change(item_cost, paid)}.")

#User input
# item_cost = int(input(f"[TOTAL] EUR "))
# paid = int(input("[PAID]  EUR "))
# print(f"[CHANGE] EUR {calculate_change(item_cost, paid):.1f}")

#ENGINE COLORS
print_title("make_engine_clr", "=", 10)

def calculate_color(r: int, g: int, b: int) -> str:
    r = r / 255
    g = g / 255
    b = b / 255
    return f"({r}, {g}, {b})"

print(calculate_color(0, 255, 125))
red = int(input("R: "))
green = int(input("G: "))
blue = int(input("B: "))
print(f"color = {calculate_color(red, green, blue)}")


