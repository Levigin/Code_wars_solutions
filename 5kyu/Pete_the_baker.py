def cakes(recipe: dict, available: dict):

    if len(recipe) > len(available):
        return 0

    result = 10000
    for key in recipe:
        if key in available:
            result = min(available[key] // recipe[key], result)
        else:
            return 0

    return result


recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
print(cakes(recipe, available))
