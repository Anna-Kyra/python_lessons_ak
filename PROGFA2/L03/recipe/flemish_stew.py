from ascii_frame import AsciiFrame
from progress_bar import ProgressBar
from rating import StarRating
from task import Task

ingredients = {
    "Onions": 2,
    "Butter": "1 knob",
    "Beef": "1,000 g",
    "Pepper": "to taste",
    "Salt": "1 pinch",
    "Brown beer": "2 bottles",
    "Bay leaves": 2,
    "Thyme sprigs": 2,
    "Clove": 1,
    "Liège syrup": "2 tbsp",
    "Slice of bread": 1,
    "Mustard": "2 tbsp",
    "Vinegar": "1 dash",
}
recipe_steps = [
    "Peel the onions and chop them into medium-sized pieces.",
    "Heat a large stew pot and melt a knob of butter. Sauté the onions over medium heat without letting them brown.",
    "Heat a frying pan over medium heat and melt a knob of butter.",
    "Sear the beef pieces in the frying pan until they develop a golden-brown crust. Season with freshly ground pepper and a pinch of salt while cooking.",
    "Transfer the seared meat to the stew pot with the onions. Keep the frying pan with the browned bits. Pour the beer into the pan and scrape up all the flavorful bits while bringing it to a boil (deglazing).",
    "Once the beer is boiling, pour it into the stew pot.",
    "Tie the bay leaves and fresh thyme sprigs together with kitchen twine. Add the herb bundle to the pot.",
    "Add the clove and the Liège syrup (apple-pear syrup).",
    "Spread a generous layer of mustard on the slice of brown bread and place it in the pot, mustard side down.",
    "Let the stew simmer over low heat for 1.5 to 3 hours without a lid. The cooking time depends on the quality of the meat. Stir occasionally and check if the meat is tender.",
    "Once the sauce has reached the desired thickness, place the lid on the pot.",
    "Finish with a small dash of vinegar and stir well.",
    "Taste and adjust with extra freshly ground pepper and a pinch of salt if needed.",
    "Serve with hand-cut Belgian fries and mayonnaise!!"
]

title = AsciiFrame("Flemish stew")
rating = StarRating("Overall Belgian rating: ", 9, 10)
print(title)
print(rating)

print(AsciiFrame("Ingredients", "`"))

for key, value in ingredients.items():
    ingredient = Task(f"{key}: {value}")
    ingredient.is_finished = True
    print(ingredient)

print(AsciiFrame("Steps", "`"))

for index, step in enumerate(recipe_steps, start=1):
    print(f"{index}. {step}")



