'''
- Link to Problem: https://www.geeksforgeeks.org/problems/sequence-of-sequence1155/1
- Time Complexity: O(M * N)
- Space Complexity: O(M * N)
'''

from functools import lru_cache

class Solution:
    def numberSequence(self, m: int, n: int) -> int:
        
        @lru_cache(maxsize=None)
        def solve(x: int, n: int) -> int:
            if n == 0:
                return 1
            ans = 0
            for i in range(2 * x, m + 1):
                ans += solve(i, n - 1)
            
            return ans
        
        ans = 0
        for i in range(1, m + 1):
            ans += solve(i, n - 1)
        
        return ans