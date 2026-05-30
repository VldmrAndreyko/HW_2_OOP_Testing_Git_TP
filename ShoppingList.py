from Ingredient import Ingredient
from Recipe import Recipe


class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")

        recipe = recipe.scale(portions)
        for ingredient in recipe.ingredients:
            self._items.append((ingredient, recipe.title))

    def remove_recipe(self, title: str):
        result = []
        for item in self._items:
            if item[1] != title:
                result.append(item)

        self._items = result

    def get_list(self):
        shopping_list = dict()

        for ingredient, recipe_title in self._items:
            if (ingredient.name, ingredient.unit) in shopping_list:
                shopping_list[(ingredient.name, ingredient.unit)] += ingredient.quantity
            else:
                shopping_list[(ingredient.name, ingredient.unit)] = ingredient.quantity

        result = []
        for (name, unit) in shopping_list:
            quantity = shopping_list[(name, unit)]
            result.append(Ingredient(name, quantity, unit))

        result.sort(key=lambda a: a.name)

        return result

    def __add__(self, other: object):

        if not isinstance(other, ShoppingList):
            return NotImplemented

        result = ShoppingList()
        result._items = self._items + other._items

        return result
