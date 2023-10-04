'''
- Link to Problem: https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/
- Time Complexity: O(X + Y) [X: number of recipes, Y: number of ingredients]
- Space Complexity: O(X * Y)
'''

from typing import List
from collections import defaultdict

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        possibleRecipes = defaultdict(list)
        degree = defaultdict(int)

        for i in range(len(recipes)):
            recipe = recipes[i]
            for ingredient in ingredients[i]:
                possibleRecipes[ingredient].append(recipe)
                degree[recipe] += 1

        recipes = set(recipes)
        result = []
        while supplies:
            ingredient = supplies.pop(0)
            if ingredient in recipes:
                result.append(ingredient)
            
            for recipe in possibleRecipes[ingredient]:
                degree[recipe] -= 1

                if degree[recipe] == 0:
                    supplies.append(recipe)
        
        return result

