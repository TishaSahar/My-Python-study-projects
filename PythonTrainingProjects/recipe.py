class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure


    def __str__(self):
        return self.name + ': ' + str(self.volume) + ', ' + self.measure


class Recipe:
    def __init__(self, *ings):
        self.ingredients = []
        for i in ings:
            self.ingredients.append(i)

    
    def add_ingredient(self, ingredient):
        if type(ingredient) == Ingredient:
            self.ingredients.append(ingredient)


    def remove_ingredient(self, ingredient):
        if type(ingredient) == Ingredient:
            for ing in self.ingredients:
                if ing.name == ingredient.name:
                    self.ingredients.remove(ing)
                    break


    def get_ingredients(self):
        return (ing for ing in self.ingredients)
    

    def __len__(self):
        return len(self.ingredients)
    

recipe = Recipe()
i1 = Ingredient("Соль", 1, "столовая ложка")
r2 = Recipe(i1, Ingredient("Соль", 1, "столовая ложка"))
print(len(r2))
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
recipe.remove_ingredient(Ingredient("Соль", 1, "столовая ложка"))
ings = recipe.get_ingredients()
n = len(recipe) # n = 3
print(n)