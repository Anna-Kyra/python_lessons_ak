drinks = {
    "espresso": 2.50,
    "cappuccino": 3.00,
    "caffe latte": 3.50,
    "green tea": 2.00,
    "apple juice": 3.20,
    "iced coffee": 3.80,
    "mocktail": 4.50
}

menu = {
    "drinks": {
        "espresso": 2.50,
        "cappuccino": 3.00,
        "caffe latte": 3.50,
        "green tea": 2.00,
        "apple juice": 3.20,
        "iced coffee": 3.80,
        "mocktail": 4.50
    },
    "snacks": {
        "crisps": 2.30,
        "muffin": 3.00,
        "brownie": 3.50,
        "cheese": 5.00
    },
    "desserts": {
        "tiramisu": 4.50,
        "cheesecake": 4.80,
        "ice cream": 3.50
    }
}

def print_menu():
    print(f"{"--MENU" * 3}--")
    for key, value in drinks.items():
        print(f"{key} : EUR {value}")

def add_item():
    drinks["biertje"] = 3.0


# add_item()
# print_menu()

def take_order():
    order = {}
    while True:
        drink_name = input("What do you want to drink (stop to end)? ")
        if drink_name == "stop":
            break
        else:
            if drink_name in drinks.keys():
                if drink_name in order.keys():
                    order[drink_name] += 1
                else:
                    order[drink_name] = 1
            else:
                print("Not Available")
        print_order(order)

def print_order(ordered_drinks : dict):
    print("YOUR ORDER")
    sum = 0
    for key, value in ordered_drinks.items():
        price = drinks[key]
        sum += price * value
        print(f"{key} : {value * price}")
    print(f"TOTAL AMOUNT = EUR {sum}")

# print_menu()
# take_order()
def print_full_menu():
    for category, menu_items in menu.items():
        print(category.upper())
        for name, price in menu_items.items():
            print(f"\t{name}\t:\tEUR {price}")

print_full_menu()