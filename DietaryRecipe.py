from Ingredient import Ingredient
from Recipe import Recipe


class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients: list[Ingredient]):
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio: float):
        recipe = super().scale(ratio)

        result = DietaryRecipe(recipe.title, self.diet_type, recipe.ingredients)

        return result

    def __str__(self):
        return f"[{self.diet_type}] {super().__str__()}"
