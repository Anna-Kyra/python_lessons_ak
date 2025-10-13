#PRINT TITLE
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

