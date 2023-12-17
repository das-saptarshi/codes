'''
- Link to Problem: https://leetcode.com/problems/design-a-food-rating-system/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

import heapq
from typing import List
from collections import defaultdict

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
       self.foodWiseDetails = {}
       self.cuisineWiseRatings = defaultdict(list)
       for food, cuisine, rating in zip(foods, cuisines, ratings):
           self.foodWiseDetails[food] = (cuisine, rating)
           heapq.heappush(self.cuisineWiseRatings[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.foodWiseDetails[food]
        self.foodWiseDetails[food] = (cuisine, newRating)
        heapq.heappush(self.cuisineWiseRatings[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while self.cuisineWiseRatings[cuisine]:
            rating, food = self.cuisineWiseRatings[cuisine][0]
            if self.foodWiseDetails[food] == (cuisine, -rating):
                return food
            heapq.heappop(self.cuisineWiseRatings[cuisine])