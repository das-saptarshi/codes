'''
- Link to Problem: https://leetcode.com/problems/move-zeroes/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_index += 1
        
        for i in range(zero_index, len(nums)):
            nums[i] = 0