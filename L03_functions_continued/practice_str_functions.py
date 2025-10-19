#MOVIE NAME
# movie_name = input("Enter a movie name: ") #LORD OF THE RINGS : fellowship of the ring
# print(f"* WHATCH NOW * {movie_name.title().replace('Of', 'of').replace('The', 'the')}")

#WORD GUESS
word_guess = input("Enter a word to guess: ")
print(f"* This word is secret: "
      f"{word_guess.lower()
      .replace('a', '*')
      .replace('e', '*')
      .replace('i', '*')
      .replace('o', '*')
      .replace('u', '*')}\n"
      f".\n.\n.\n.\n"
      f"* psst.. don't tell anyone.. the actual word is '{word_guess}'!")
