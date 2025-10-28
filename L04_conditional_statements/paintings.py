# PRINT TITLE
def print_title(title: str, symbol: str, times: int):
    """
    Prints title surrounded by a certain symbol
    :param title: name of the title
    :param symbol: A symbol
    :param times: How many times the symbol needs to print
    :return:
    """
    print(f"\n {symbol * times} {title} {symbol * times}")
#
# def is_vip_painter(painter_name: str) -> bool:
#     vip_painters = ("Vincent", "Pablo", "Leonardo", "Claude", "Rembrandt",
#                     "Michelangelo", "James")
#
#     return painter_name in vip_painters
#
# print_title("is_vip_painter", "=", 10)
# name_painter = input("Welcome! What's your name? ")
# is_vip_painter(name_painter)
#
# if is_vip_painter(name_painter):
#     print("Welcome, VIP artist! Your canvas awaits!")
# else:
#     print("Hello, artist! Let's get started with your masterpiece.")

# ARE YOU READY
# def ready_to_paint() -> bool:
#     ready = input("Are you ready to paint (yes/no)? ")
#
#     return ready.lower() == 'yes'
#
# print_title("ready_to_paint", "=", 10)
# if ready_to_paint():
#     print("This artist is ready to print: True")
# else:
#     print("This artist is ready to print: False")


# WHAT'S MY COLOR
def whats_my_color(color: tuple) -> str:
    """
    Based on the r, g, b values, this function tells you what color you have. The recognized colors are red, green, blue, white, black.
    :param color:
    :return:
    """
    if color == (1, 0, 0):
        return "red"
    elif color == (0, 1, 0):
        return "green"
    elif color == (0, 0, 1):
        return "blue"
    elif color == (0, 0, 0):
        return "black"
    elif color == (1, 1, 1):
        return "white"
    else:
        return "Choose another color"

print_title("whats_my_color", "=", 10)
print(f"If r, g, and b are all 0, the color is {whats_my_color((0, 0, 0))}.")
r = int(input("r [0-1]: "))
g = int(input("g [0-1]: "))
b = int(input("b [0-1]: "))
print(f"-> You created the color: {whats_my_color((r, g, b))}.")

