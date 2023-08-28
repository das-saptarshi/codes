# Link to Problem: https://leetcode.com/problems/frog-jump/
# Time Complexity: O(n**2)
# Space Complexity: O(n**2)

from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if len(stones) == 1:
            return True
        
        target = stones[-1]
        stones = set(stones)
        dp = {}

        def solve(position, jumpStrength):
            if position == target:
                return True

            if position not in stones:
                return False

            if jumpStrength <= 0:
                return False
            
            key = (position, jumpStrength)
            if key in dp:
                return dp[key]
            
            canReachEnd = solve(position + jumpStrength, jumpStrength) or solve(position + jumpStrength + 1, jumpStrength + 1) or solve(position + jumpStrength - 1, jumpStrength - 1)
            
            dp[key] = canReachEnd
            return canReachEnd

        return solve(1, 1)