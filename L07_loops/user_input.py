#1 CHECK USER INPUT
def is_valid_code(t: str) -> bool:
    if t.isdigit():
        return True
    else:
        return False


def get_ansi_color_code():
    color_code = input("Please choose an ANSI color code: ")
    while is_valid_code(color_code) != True:
        color_code = input("That is not a valid color code. Try again: ")
    print("Hello world!")

get_ansi_color_code()

#2 PRINT A TABLE OF ANSI COLORS
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

print("FOREGROUND:\n"
      "-----------")

get_colored_text("hello", 30)