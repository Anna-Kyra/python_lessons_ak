vowels = 'a', 'e', 'i', 'o', 'u'

text = input("Enter your text: ")

for vowel in vowels:
    if text.count(vowel) == 0:
        print(f"{vowel}: not found")
    else:
        print(f"{vowel}: {text.count(vowel)}x")