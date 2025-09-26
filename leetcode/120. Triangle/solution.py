'''
- Link to Problem: https://leetcode.com/problems/triangle/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List
from functools import lru_cache


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)

        @lru_cache(maxsize=None)
        def solve(row, col):
            if not (row < rows and col < len(triangle[row])):
                return float('inf')
            
            minPath = min(solve(row + 1, col), solve(row + 1, col + 1))

            if minPath == float('inf'):
                minPath = 0
            
            return triangle[row][col] + minPath
        
        return solve(0, 0)