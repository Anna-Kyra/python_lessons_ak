class Task:
    def __init__(self, task : str):
        self.task = task
        self.is_finished = False
    def __str__(self):
        if self.is_finished:
            return f"☑ - {self.task}"
        else:
            return f"☐ - {self.task}"