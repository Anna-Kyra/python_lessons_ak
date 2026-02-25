from rating import StarRating

progfa = StarRating("Programming for artists course", 8, 10)
print(progfa)

movies = list()
the_room = StarRating("The Room", 1, 5)
lotr = StarRating("LOTR : Return of the King (2003)", 5, 5)
avatar = StarRating("Avatar : The Way of Water", 3, 5)
inception = StarRating("Inception", 4, 5)
batman = StarRating("Batman-Superman : Dawn of Justice", 2, 5)

movies.append(the_room)
movies.append(lotr)
movies.append(avatar)
movies.append(inception)
movies.append(batman)

def ask_movie():
    name = input("What movie or series did you last see? ")
    score = int(input("What rating (out of 5) would you give it? "))
    new_movie = StarRating(name, score, 5)
    print(new_movie)

print("\n")
ask_movie()
print("\n")
for movie in movies:
    print(movie)