'''
- Link to Problem: https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
- Time Complexity: O(N ^ 3)
- Space Complexity: O(N ^ 2)
'''

from typing import List
from functools import lru_cache


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @lru_cache(None)
        def solve(i, j):
            if i + 2 > j:
                return 0
            
            if i + 2 == j:
                return values[i] * values[i + 1] * values[j]
            
            return min(
                (values[i] * values[k] * values[j] + solve(i, k) + solve(k, j))
                for k in range(i + 1, j)
            )
        

        return solve(0, len(values) - 1)