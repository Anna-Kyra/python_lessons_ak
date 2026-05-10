warrior = {
    "name": "PixelWarrior",
    "hair_color": "blue",
    "outfit": "armor",
    "inventory": ["sword", "shield"]
}

knight = {
    "name": "ShadowKnight",
    "hair_color": "black",
    "outfit": "cloak",
    "inventory": ["dagger", "bow"]
}

def print_avatar(avatar : dict):
    print(f"{"=" * (len(avatar["name"]) + 8)}\n"
          f"\t{avatar["name"].upper()}\n"
          f"{"=" * (len(avatar["name"]) + 8)}")
    print(f"* This creature has {avatar["hair_color"]} hair and is wearing some {avatar["outfit"]}.\n"
          f"* Current inventory: {avatar["inventory"]}")

print_avatar(warrior)
print_avatar(knight)


def build_avatar():
    print(f"\n[BUILD YOUR OWN AVATAR]")

    my_avatar = {}
    my_avatar["name"] = input("\t-> What name do you choose? ")
    my_avatar["hair_color"] = input("\t-> Which hair color would you like? ")
    my_avatar["outfit"] = input("\t-> What is teh name of your outfit? ")
    my_avatar["inventory"] = list(input("\t-> Give me a list of your inventory separated bij ',': ").split(","))

    # print(my_avatar)
    print_avatar(my_avatar)

build_avatar()