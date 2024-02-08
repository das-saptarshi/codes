'''
- Link to Problem: https://leetcode.com/problems/perfect-squares/
- Time Complexity: O(N ^ 3/2)
- Space Complexity: O(1)
'''

from math import sqrt
from functools import lru_cache

class Solution:
    def numSquares(self, n: int) -> int:
        
        @lru_cache(maxsize=None)
        def solve(n):
            if n == 0:
                return 0

            start = int(sqrt(n))

            ans = float('inf')
            for i in range(start, 0, -1):
                square = i * i    
                ans = min(ans, solve(n - square) + 1)
            
            return ans
        
        return solve(n)
