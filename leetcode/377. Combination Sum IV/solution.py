'''
- Link to Problem: https://leetcode.com/problems/combination-sum-iv/
- Time Complexity: O(N * target)
- Space Complexity: O(target)
'''


from typing import List
from functools import cache


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if min(nums) > target:
            return 0

        @cache
        def solve(total):
            if total == target:
                return 1
            if total > target:
                return 0

            combinations = 0
            for x in nums:
                combinations += solve(total + x)

            return combinations
        
        return solve(0)