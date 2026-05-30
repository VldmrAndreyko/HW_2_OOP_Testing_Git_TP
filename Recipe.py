from packaging.pylock import is_valid_pylock_path

from Ingredient import Ingredient


class Recipe:
    def __init__(self, title: str, ingredients: list[Ingredient] = None):
        self.title = title
        if ingredients is None:
            self.ingredients = []
        else:
            self.ingredients = ingredients

    def add_ingredient(self, ingredient: Ingredient):
        for i in self.ingredients:
            if i == ingredient:
                i.quantity += ingredient.quantity
                return

        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        try:
            return float(ratio) > 0
        except(TypeError, ValueError):
            return False

    def scale(self, ratio: float):

        if not self.is_valid_ratio(ratio):
            raise ValueError("Количество порций должно быть положительным числом")

        new_ingredients = []

        for i in self.ingredients:
            new_quantity = i.quantity * ratio
            new_ingredient = Ingredient(i.name, new_quantity, i.unit)

            new_ingredients.append(new_ingredient)

        return Recipe(self.title, new_ingredients)

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        result = f"{self.title}: "

        for i in self.ingredients:
            result += f"{i} "

        return result