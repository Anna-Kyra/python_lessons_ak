import random

# first_name = "Ryan"
# last_name = "O'Conner"
# trait = "nap king"
# age = 21


person = ("Ryan", "O'Conner", "nap king", 21)
first_name, last_name, trait, age = person

print(f'{first_name} "{trait.title()}" {last_name} enrolled in DAE.')
print(f"=> Welcome, {first_name}! We waited {age} years for you.")

person2 = ("Britt", "McMahon", "gossip", 21)
first_name, last_name, trait, age = person2

print(f'{first_name} "{trait.title()}" {last_name} enrolled in DAE.')
print(f"=> Welcome, {first_name}! We waited {age} years for you.")

actors = ('Tom Hanks', 'Emma Stone', 'Scarlett Johansson', "Chris Hemsworth",
"Pedro Pascal", "Robert Pattinson",
"Margot Robbie", "Benedict Cumberbatch", "Meryl Streep", "Michael B. Jordan")
movies = ('Inception', 'Titanic', 'Matrix', 'La La Land', 'Avengers', "The Shawshank Redemption", "The Godfather",
"The Dark Knight", "Schindler's List", "Pulp Fiction", "The Lord ofthe Rings: The Return of the King",
"Forrest Gump", "Fight Club")

actor1 = random.choice(actors)
actor2 = random.choice(actors)
actor3 = random.choice(actors)
movie = random.choice(movies)

print(f"* NEWSFLASH: {actor1} and {actor2} join forces for a remake of {movie}")
print(f"* GOSSIP: apparently, the last actor considered was {actor3}")