# SALES
items = "T-Shirt", "Blue Jeans", "Winter Coat", "Cotton Socks", "Leather Belt"
# ==== prices ====
prices = 20, 45.00, 120.50, 9.00, 25.00
# ==== discounts ====
discounts = 10, 20, 50, 0, 15

print("SALES ~ SALES ~ SALES ~ SALES")

for item, price, discount in zip(items, prices, discounts):
    if discount == 0:
        print(f"{item}: {price * ((100 - discount) / 100)} (no sale)")
    else:
        print(f"{item}: {price * ((100 - discount)/ 100)} (-{discount}%)")
