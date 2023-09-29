'''
- Link to Problem: https://leetcode.com/problems/monotonic-array/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = False
        decreasing = False

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                if decreasing: return False
                increasing = True
            elif nums[i - 1] > nums[i]:
                if increasing: return False
                decreasing = True
        
        return True