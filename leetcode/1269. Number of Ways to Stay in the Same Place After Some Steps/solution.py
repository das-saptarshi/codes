'''
- Link to Problem: https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/
- Time Complexity: O(Steps^2)
- Space Complexity: O(Steps)
'''

from functools import cache

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        @cache
        def solve(index, steps):
            if not (0 <= index < arrLen):
                return int(index == 0)

            if steps == 0:
                return int(index == 0)
            
            return (solve(index, steps - 1) + solve(index - 1, steps - 1) + solve(index + 1, steps - 1)) % MOD
            
        MOD = 10**9 + 7
        return solve(0, steps)