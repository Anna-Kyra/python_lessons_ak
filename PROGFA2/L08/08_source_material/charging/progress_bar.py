from openpyxl.styles.builtins import percent


class ProgressBar:
    def __init__(self, name: str, percentage: int = 0):
        self.name = name
        self.percentage = percentage

    def __str__(self):
        num_chars = int(self.percentage / 10)
        num_empty = 10 - num_chars
        return f"{self.name}: [{num_chars * '='}{num_empty * ' '}] {self.percentage}%"
