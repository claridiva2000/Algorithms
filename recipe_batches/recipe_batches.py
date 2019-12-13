#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  avail= []

  # for k,v in recipe.items():
  if len(ingredients) != len(recipe):
    return 0
  for r in recipe:
    if recipe[r] <= ingredients[r]:
      avail.append(ingredients[r]//recipe[r])
    # print(avail.values())
    print(avail)
  if len(avail) < len(recipe):
    return 0

  return min(avail) 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 232, 'butter': 150, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))  