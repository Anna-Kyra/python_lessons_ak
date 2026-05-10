class Pigeon:
    def __init__(self, name: str, identity: str,snack: str, security_level: int):
        """
        :param name: actual (original) name of the pigeon
        :param identity: new name to cover identity
        :param snack: favorite snack with which one can bribe this pigeon
        :param security_level: a NUMBER from 1-5, 1 being lowest and 5 being highest
        """
        levels = {
            1 : "very low",
            2 : "low",
            3 : "medium",
            4 : "high",
            5 : "very high"
        }
        self.name = name
        self.identity = identity
        self.favorite_snack = snack
        self.security_level = levels[int(security_level)]  # TODO: get level name from dictionary (low, medium,...); do not save number!

    def __str__(self):
        return f"[{self.security_level.upper()} RISK] {self.identity} ({self.favorite_snack})"
