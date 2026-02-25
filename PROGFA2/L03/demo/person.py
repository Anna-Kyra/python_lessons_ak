class Person :
    def __init__(self, name : str, first_name : str, age : int):
        self.name = name
        self.first_name = first_name
        self.age = age

    def __str__(self):
        return (f"{self.first_name} {self.name} - {self.age} years old")

