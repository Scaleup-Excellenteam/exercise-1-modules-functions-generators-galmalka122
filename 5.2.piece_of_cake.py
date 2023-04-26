def get_recipe_price(prices: dict, optionals=None, **ingredients):
  """This function calculates the total price of a recipe based on the prices of its ingredients and the quantity
  of each ingredient used in the recipe. The optional ingredients are excluded from the calculation.

  Args:
  
    prices: A dictionary of ingredient names and their respective prices per 100 grams.
    optionals: A list of optional ingredients that should be excluded from the calculation. Defaults to None.
    **ingredients: representing the quantity of each ingredient used in the recipe.
    
  Returns:

    final_price (int): The total price of the recipe."""
    
  final_price = 0
  
  # For every ingredient check if it's not in the optionals list, if not add the price for the quantity used.
  for ingredient, price in prices.items():
    if ingredient not in optionals:
      final_price += price * ingredients[ingredient] // 100
      
  return final_price