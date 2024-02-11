'''
- Link to Problem: https://leetcode.com/problems/cherry-pickup-ii/
- Time Complexity: O((R * C) ^ 2)
- Space Complexity: O((R * C) ^ 2)
'''

from typing import List
from functools import lru_cache

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        @lru_cache(maxsize=None)
        def solve(r: int, cA: int, cB: int) -> int:
            if not (r < rows and 0 <= cA < cols and 0 <= cB < cols):
                return 0
            if r == rows: 
                return 0
            cherries = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if (cA + x) == (cB + y): continue
                    cherries = max(cherries, solve(r + 1, cA + x, cB + y))

            return cherries + grid[r][cA] + grid[r][cB]

        rows, cols = len(grid), len(grid[0])
        return solve(0, 0, cols - 1)
