#MOVIE NAME
# movie_name = input("Enter a movie name: ") #LORD OF THE RINGS : fellowship of the ring
# print(f"* WATCH NOW * {movie_name.title().replace('Of', 'of').replace('The', 'the')}")


#WORD GUESS
# word_guess = input("Enter a word to guess: ")
# print(f"* This word is secret: "
#       f"{word_guess.lower()
#       .replace('a', '*')
#       .replace('e', '*')
#       .replace('i', '*')
#       .replace('o', '*')
#       .replace('u', '*')}\n"
#       f".\n.\n.\n.\n"
#       f"* psst.. don't tell anyone.. the actual word is '{word_guess}'!")

#HIDDEN WORD
# hidden_word = "occurrence"
# print("*" * len(hidden_word))
#
# character = input(f"Please enter a single character you want to find in my hidden word {hidden_word}: ")
# print(f"* NUMBER OF TIMES THE CHARACTER IS IN THIS WORD: {hidden_word.count(character.lower())}")
# print(f"* FIRST INDEX OF THE CHARACTER IN THIS WORD: {hidden_word.find(character.lower())}")
# print(f"* FIRST INDEX OF THE CHARACTER IN THIS WORD: {hidden_word.rfind(character.lower())}")

#FILENAME
filename = input("Enter the filename of your project (group_lastName_FirstName) : ")
group, last_name, first_name = filename.split("_")
print(f"* FIRST NAME: {first_name}\n"
      f"* LAST NAME: {last_name}\n"
      f"* GROUP: {group}")

