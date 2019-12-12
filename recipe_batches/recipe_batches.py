#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  avail= {}

  for k,v in recipe.items():
    if len(ingredients) < len(recipe):
      return 0
    if v > ingredients[k]:
      return 0
    else:
      avail.update({k:ingredients[k]//v})
      print(avail)
      return min(avail.values())  


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 50, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients)) 