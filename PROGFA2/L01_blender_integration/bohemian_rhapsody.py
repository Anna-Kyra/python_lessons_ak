# BOHEMIAN RHAPSODY
lyrics = "Is this the real life? Is this just fantasy? Caught in a landslide. No escape from reality. Open your eyes, look up to the skies and see..."

lyrics_list = list(lyrics.split())


for index, lyric in enumerate(lyrics_list):

    if lyric[-1] == ".":
        if index % 4 == 0:
            print(lyric.upper(), end="\n")
        else:
            print(lyric, end="\n")
    elif lyric[-1] == "?":
        if index % 4 == 0:
            print(lyric.upper(), end="\n")
        else:
            print(lyric, end="\n")
    elif index % 4 == 0:
        print(lyric.upper(), end=" ")
    else:
        print(lyric, end=" ")


