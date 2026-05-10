# ============== EX02 =================
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

# def get_smiley(smiley : str) -> str:
#     new_smiley = emoji_dict[smiley]
#     return new_smiley
#
# emoji = input("give me a smiley ")
# print(get_smiley(emoji))

for key, value in emoji_dict.items():
    print(f"{key} ----> {value}")

def text_emoji():
    text = input("Insert your text: ")
    for key, value in emoji_dict.items():
        text = text.replace(key, value)
    print(text)

text_emoji()