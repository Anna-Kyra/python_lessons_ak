class ProgressBar():
    def __init__(self, name : str, percentage : int):
        self.name = name
        self.percentage = percentage
    def __str__(self):
        return f"Loading {self.name}: [{"=" * int(self.percentage / 10)}{" " * (10 - int(self.percentage / 10))}] {self.percentage}%"