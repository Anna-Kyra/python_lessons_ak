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

def print_compliment() -> str:
    adjectives = ("artful", "nimble", "brilliant", "expressive", "colorful", "clever",
                  "graceful", "innovative", "vibrant")
    nouns = ("programmer", "designer", "coder", "artist", "creator", "developer",
             "visionary", "architect", "maker", "painter")

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"{adjective} {noun}"

compliment = print_compliment()
print(f"Wow, you are one {compliment}!")
print(f"And did you know your neighbour is a {compliment}?")




