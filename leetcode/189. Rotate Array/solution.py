'''
- Link to Problem: https://leetcode.com/problems/rotate-array/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        if k == 0: return

        self.rotate_range(nums, 0, (n - k))
        self.rotate_range(nums, (n - k), n)
        self.rotate_range(nums, 0, n)
    
    def rotate_range(self, nums: List[int], left: int, right: int) -> None:
        right -= 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1