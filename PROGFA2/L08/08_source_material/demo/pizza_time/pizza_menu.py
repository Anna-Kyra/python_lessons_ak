from pizza import Topping, Pizza

# TODO 1: create + print a topping instance/object for "tomato sauce"
tomato_sauce = Topping("tomato_sauce", True)


# TODO 2: create topping "mozzarella"
mozzarella = Topping("mozzarella", True)

# TODO 3: create Pizza class in pizza.py (__str__ prints name and toppings)


# TODO 3: create + print pizza "margherita" (tomato sauce, mozzarella)
margherita = Pizza("margherita")
margherita.add_topping_object(tomato_sauce)
margherita.add_topping_object(mozzarella)

print("PIZZA MENU")
print("-------------")
print(margherita)

# TODO 4: create pizza diavola (tomato sauce, mozzarella, salame pikante)
diavola = Pizza("diavola")
diavola.add_topping_object(tomato_sauce)
diavola.add_topping_object(mozzarella)
diavola.add_topping("salame_pikante", False)
print(diavola)

# TODO 5: change __str__ of Pizza to print 🍃 symbol if it is veggie
