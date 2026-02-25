class StarRating():
    def __init__(self, movie : str, score : int, score_max : int):
        self.movie = movie
        self.score = score
        self.score_max = score_max

    def __str__(self):
        return f"{self.movie}: {"★" * self.score}{"☆" * (self.score_max - self.score)} ({self.score}/{self.score_max})"