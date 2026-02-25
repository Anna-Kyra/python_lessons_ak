class AsciiFrame():
    def __init__(self, title : str , symbol : str = "*", level : int = 0):
        self.title = title
        self.symbol = symbol
        self.level = level
    def __str__(self):
        tabs = '\t' * self.level
        number_symbols = len(self.title) + 4
        return (f"{tabs}{self.symbol * number_symbols}\n"
                f"{tabs}| {self.title.upper()} |\n"
                f"{tabs}{self.symbol * number_symbols}")