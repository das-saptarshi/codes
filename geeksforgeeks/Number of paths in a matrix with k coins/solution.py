'''
- Link to Problem: https://www.geeksforgeeks.org/problems/number-of-paths-in-a-matrix-with-k-coins2728/1
- Time Complexity: O(N^2)
- Space Complexity: O(N^2)
'''

from functools import lru_cache

class Solution:
    def numberOfPath (self, n, k, arr):
        
        @lru_cache(maxsize=None)
        def solve(r, c, coins):
            if not (0 <= r < n and 0 <= c < n and coins >= 0):
                return 0
                
            coins -= arr[r][c]
            
            if (r, c) == target and coins == 0:
                return 1
            
            return solve(r + 1, c, coins) + solve(r, c + 1, coins)
        
        target = (n - 1, n - 1)
        return solve(0, 0, k)