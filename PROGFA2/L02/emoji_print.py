# emoji_print.py -> given dictionary
emoji_dict = {
    ":)": "🙂",
    ":D": "😄",
    ":(": "☹️",
    ":P": "😜",
    ";)": "😉",
    ":O": "😯",
    ":*": "😘",
    ":'(": "😢",
    ":|": "😐",
    ":/": "😕"
}

# emoji_print.py -> example text to use in todo 3:
# I thought I nailed the joke :D, but my friend just gave me a blank stare :|. I shrugged and said, 'Guess I'll try again!' :P ;)

for key, value in emoji_dict.items():
    print(f"{key}\t---->\t{value}")

def take_emoji():
    while True:
        emoji_order = input("emoji: ")
        if emoji_order == "stop":
            break
        if emoji_order in emoji_dict.keys():
            print(emoji_dict[emoji_order])
        else:
            print("unkown smiley")

# take_emoji()

def text_emoji():
    text = input("Insert your text: ")
    for key, value in emoji_dict.items():
        text = text.replace(key, value)
    print(text)

text_emoji()