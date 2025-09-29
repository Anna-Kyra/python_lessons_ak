#Apple
apple_number = int(input("How many apples do you like? "))
apple_cost = 0.45 * apple_number
print(f"=> {apple_number} apples cost ${apple_cost:.2f}")

#Banana
banana_number = int(input("How many bananas do you like? "))
banana_cost = 0.371 * banana_number
print(f"=> {banana_number} bananas cost ${banana_cost:.2f}")

#Cherry
cherry_number = int(input("How many cherries do you like? "))
cherry_cost = 0.094 * cherry_number
print(f"=> {cherry_number} cherries cost ${cherry_cost:.2f}")
discount = int(input("You are such a loyal customer, I shall give you a deal. How much discount would you like? "))

#Result
total_without = apple_cost + banana_cost + cherry_cost
discount_of_total = total_without * (discount / 100)
total_with = total_without - discount_of_total

print(f"[TOTAL] ${total_without}\n"
      f"[DISCOUNT %] {discount}%\n"
      f"=> With a discount of ${discount_of_total:.2f}, you owe ${total_with:.2f}")

pay = int(input("How much can you pay? $"))
change = pay - total_with
print(f"Here is your change: ${change:.2f}")