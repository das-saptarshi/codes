'''
- Link to Problem: https://leetcode.com/problems/fruit-into-baskets/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        elems = defaultdict(int)
        n = len(fruits)
        start = end = 0
        maxFruits = 1
        while end < n:
            x = fruits[end]
            elems[x] += 1

            while start <= end and len(elems) > 2:
                x = fruits[start]
                elems[x] -= 1
                if elems[x] == 0: del elems[x]
                start += 1

            maxFruits = max(maxFruits, end - start + 1)
            end += 1
        return maxFruits