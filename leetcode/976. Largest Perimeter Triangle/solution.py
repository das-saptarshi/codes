'''
- Link to Problem: https://leetcode.com/problems/largest-perimeter-triangle/
- Time Complexity: O(NlogN)
- Space Complexity: O(1)
'''

from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(n - 3, -1, -1):
            if nums[i] + nums[i + 1] > nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        
        return 0