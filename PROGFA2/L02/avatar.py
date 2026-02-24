# avatar.py -> given dictionaries
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

def title(title : str):
    print("=" * 40)
    print(f"\t {title.upper()}")
    print("=" * 40)

def print_avatar(avatar : dict):
    title(avatar["name"])
    print(f"* This creature has {avatar["hair_color"]} hair and is wearing some {avatar["outfit"]}.")
    print(f"* Current inventory: {avatar["inventory"]}")

def new_avatar():
    print("\n[BUILD YOUR OWN AVATAR]")
    my_avatar = {}
    my_avatar["name"] = input("\t-> What name do you choose? ")
    my_avatar["hair_color"] = input("\t-> What hair color would you like? ")
    my_avatar["outfit"] = input("\t-> What is the name of your outfit? ")
    my_avatar["inventory"] = list(input("\t-> Give me a list of your inventory, seperated by ',': "))
    # print_avatar(my_avatar["name"])
    print(my_avatar)
    print(my_avatar["name"])
    print_avatar(my_avatar)

print_avatar(warrior)
print_avatar(knight)
new_avatar()



