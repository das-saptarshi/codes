'''
- Link to Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        unique_index = 0
        index = 0
        
        while index < n:
            index += 1
            while index < n and nums[index - 1] == nums[index]:
                index += 1
            
            nums[unique_index] = nums[index - 1]
            unique_index += 1
        
        return unique_index
            
