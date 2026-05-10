"""
HOW TO PLAY A SOUND (EXAMPLE):

# 0. imports + initialize:
import pygame  # we will use this library to play sound, while remaining in console
import time    # allows us to make the program 'wait' a moment

pygame.mixer.init()  # ONLY ONCE: prepare mixer to play sound

# 1. Load a sound from your folder structure
sound = pygame.mixer.Sound("SoundEffects/439073__fourthwoods__kara-woohoo.ogg")

# 2. Play the sound
# sound.play()

# 3. Wait a second; once the program stops, the sound stops as well!
# time.sleep(1)
"""
import random

import pygame
import time

pygame.mixer.init()

sound = pygame.mixer.Sound("SoundEffects/439073__fourthwoods__kara-woohoo.ogg")

sound.play()
time.sleep(1)

sound_library = {
    "meow": "214759__peridactyloptrix__cat-meowing-x5.wav",
    "woohoo": "439073__fourthwoods__kara-woohoo.ogg",
    "punch": "573378__johnloser__cyber-punch-03.wav",
    "slap": "490768__steveuk87__punch-1-loud-slap.ogg",
    "laugh": "582751__martina_leitschuh__people_laughing_outdoors_001.wav",
    "giggle": "421025__ceebee90__squaky-giggle.m4a",
    "laser": "344312__musiclegends__laser-shoot7.wav",
    "evil laugh": "270469__littlerobotsoundfactory__laugh_evil_02.wav",
    "scream": "270474__littlerobotsoundfactory__scream_male_03.wav",
    "thunder": "351526__littlerainyseasons__thunder.mp3",
    "drip": "290515__littlerobotsoundfactory__drip_00.wav",
    "splat": "237926__foolboymedia__messy-splat-2.wav",
    "fart": "237652__delphidebrain__delphis-fart-03.wav",
    "woosh": "396189__pivanladbrouille__woosh-fx-2.wav",
    "whip": "734691__geoff-bremner-audio__whip-8.wav",
    "kiss": "506405__max_cristos__long-kiss.wav",
    "knock": "256513__deleted_user_4772965__knock-on-the-door.wav",
    "yes": "520266__hisoul__eris-yes-whisper_1.wav",
    "nope": "520262__hisoul__eris-disagree-answer-stupid_2.wav",
    "cry": "520285__hisoul__zisa-cry-scream-sad-weep-hysteric_7.wav",
    "attack": "520277__hisoul__kali-recharge-to-attack-scream-furious_6.wav",
    "help": "213283__aderumoro__how-can-i-help-you-female-friendly-professional.wav",
}

def play_sound(chosen_sound : str):
    sound_file = sound_library[chosen_sound]
    sound = pygame.mixer.Sound(f"SoundEffects/{sound_file}")
    sound.play()
    time.sleep(1)
    pass

def ask_sound():
    chosen_sound = ""
    while True:
        chosen_sound = input("What sound would you like to play? ")
        if chosen_sound in sound_library:
            play_sound(chosen_sound)
            print(f"-> Playing: {sound_library[chosen_sound]}")
        elif chosen_sound == "exit":
            print("[BYE! Thank you for using our sound effect player!]")
            break
        else:
            print(f'Sorry, "{chosen_sound}" is not as valid sound in our library.\n'
                  f'There are {len(sound_library)} options to choose from.\n'
                  f'Options: {sound_library.keys()}')

ask_sound()