import pytest
import ipytest

from Ingredient import Ingredient
from Recipe import Recipe
from ShoppingList import ShoppingList


def test_ingredient_init():
    test = Ingredient("Мука", 500, "г")

    assert test.name == "Мука"
    assert test.quantity == 500.0
    assert test.unit == "г"

def test_ingredient_str():
    test = Ingredient("Мука", 500, "г")

    assert str(test) == "Мука: 500 г"

def test_ingredient_eq():
    test1 = Ingredient("Мука", 300, "г")
    test2 = Ingredient("Мука", 500, "г")
    test3 = Ingredient("Кокос", 100, "г")
    test4 = Ingredient("Порошок", 100, "г")
    test5 = Ingredient("Кокос", 100, "кг")

    assert test1 == test2
    assert test3 != test4
    assert test3 != test5

def test_recipe_init():
    test = Recipe("кокос", [Ingredient("Мука", 300, "г")])


    assert test.title == "кокос"
    assert test.ingredients == [Ingredient("Мука", 300, "г")]

def test_recipe_add_ingredient():
    test = Recipe("кокос", [Ingredient("Мука", 300, "г")])

    ingredient1 = Ingredient("Порошок", 100, "г")
    test.add_ingredient(ingredient1)

    assert len(test) == 2

    ingredient2 = Ingredient("Порошок", 300, "г")
    test.add_ingredient(ingredient2)

    assert len(test) == 2 and test.ingredients[1].quantity == 400

def test_recipe_scale():
    test = Recipe("кокос", [Ingredient("Мука", 300, "г")])

    new_recipe = test.scale(5)

    assert test != new_recipe

    assert new_recipe.ingredients[0].quantity == 1500

    with pytest.raises(ValueError):
        test.scale(-1)

def test_recipe_len():
    test = Recipe("кокос", [Ingredient("Мука", 300, "г")])
    ingredient1 = Ingredient("Порошок", 100, "г")
    test.add_ingredient(ingredient1)


    ingredient2 = Ingredient("Порошок", 300, "г")
    test.add_ingredient(ingredient2)

    assert len(test) == 2

def test_shoppinglist_add_recipe():
    test = ShoppingList()

    recipe = Recipe("кокос", [Ingredient("Мука", 300, "г"), Ingredient("Порошок", 100, "г")])

    test.add_recipe(recipe, 2)

    assert len(test._items) == 2
    assert test._items[0][0].quantity == 600 and test._items[1][0].quantity == 200

    with pytest.raises(ValueError):
        test.add_recipe(recipe, 0)

def test_shoppinglist_remove_recipe():
    test = ShoppingList()

    recipe1 = Recipe("кокос", [Ingredient("Мука", 300, "г")])
    recipe2 = Recipe("торт", [Ingredient("Порошок", 100, "г")])

    test.add_recipe(recipe1, 1)
    test.add_recipe(recipe2, 1)

    test.remove_recipe("торт")
    assert len(test._items) == 1

    test.remove_recipe("черемша")
    assert len(test._items) == 1

def test_shoppinglist_get_list():
    test = ShoppingList()

    recipe1 = Recipe("кокос", [Ingredient("Мука", 300, "г")])
    recipe2 = Recipe("торт", [Ingredient("Порошок", 100, "г"), Ingredient("Мука", 200, "г")])

    test.add_recipe(recipe2, 1)
    test.add_recipe(recipe1, 1)

    result = test.get_list()

    assert len(result) == 2

    assert result[0].name == "Мука" and result[1].name == "Порошок"
    assert result[0].quantity == 500

def test_shoppinglist_add():
    list1 = ShoppingList()
    list2 = ShoppingList()
    test = ShoppingList()



    recipe1 = Recipe("кокос", [Ingredient("Мука", 300, "г")])
    recipe2 = Recipe("торт", [Ingredient("Порошок", 100, "г")])

    list1.add_recipe(recipe1, 1)
    list2.add_recipe(recipe2, 1)

    test = list1 + list2

    assert len(test._items) == 2

    assert len(list1._items) == 1
    assert len(list2._items) == 1
