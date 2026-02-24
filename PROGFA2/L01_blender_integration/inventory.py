items = "Apples", "Milk", "Bread", "Eggs", "Cheese", "Rice", "Chicken", "Pasta"
quantities = 150, 42, 24, 0, 35, 80, 0, 20

for item, quantity in zip(items, quantities):
    if quantity > 0:
        print(f"- {item} ({quantity})")