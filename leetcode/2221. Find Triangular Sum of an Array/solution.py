'''
- Link to Problem: https://leetcode.com/problems/find-triangular-sum-of-an-array/
- Time Complexity: O(N ^ 2)
- Space Complexity: O(N)
'''

from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        for _ in range(n - 1):
            nums = [(nums[i - 1] + nums[i]) % 10 for i in range(1, len(nums))]
        
        return sum(nums)
                        