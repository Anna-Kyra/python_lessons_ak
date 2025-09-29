
serving = int(input("How many servings would you like? "))

# Ingredients
oliveOil = 60 * serving
chiliFlakes = 0.5 * serving
garlic = 3 * serving
parsley = 8 * serving
linguine = 125 * serving

# Recipe
print(f"PASTA ALGIO E OLIO\n"
      f"--------------------\n"
      f"Ingredients ({serving} servings):\n"
      f"* Extra virgin olive oil: {oliveOil} ml\n"
      f"* Chili flakes: {chiliFlakes} tsp\n"
      f"* Garlic: {garlic} cloves\n"
      f"* Flat-leaf parsley: {parsley} g\n"
      f"* Linguine: {linguine} g\n")