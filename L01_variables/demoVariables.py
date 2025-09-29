#dit is een comentaarlijn
personName = "Anna-Kyra"
print(f"Hello, {personName}")
print(f"What do you want me to say, {personName}?!")
message = input("Type something here: ")
print(f'Oke fine. "{message}"')
print("Ok, that's not enough")
print("How many times do you want me to say this?")
times = int(input())
message = message + " " #extra spatie na message
print(f" - {times * message.upper()}")
