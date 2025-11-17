# number = 4

# print(f"Table of {number}")
# print(f"1 x {number} = {1 * number}")

def calculate_multiplication_table(number: int):
    print(f"Table of {number} is calculated as follows:")

    for i in range(1, 11):
        print(f"{i} x {number} = {i * number}")
    print("Beep boop", end =" ")
    print("The computer is smart")

#FUNCTION CALL
calculate_multiplication_table(4)


# while True:
#     print("What??")

i = 1
max_number = 5
while i < max_number:
    print("wooohoo!")
    i += 1

# zolang de input niet nul is, roep de functie op met de gegeven functie
number = int(input("Please enter a number for the multiplication table "))
while number != 0:
    calculate_multiplication_table(number)
    number = int(input("Please enter a number for the multiplication table "))

print("Ooh.. you wanna stop the multiplication table.. A pity!")