'''
- Link to Problem: https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
- Time Complexity: O(NLogN)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return max(nums[i] + nums[n - 1 - i] for i in range(n // 2))