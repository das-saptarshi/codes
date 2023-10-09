'''
- Link to Problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
- Time Complexity: O(LogN)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [
            self.findFirstOccurance(nums, target),
            self.findLastOccurance(nums, target)
        ]

        
    def findFirstOccurance(self, nums, target):
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return start if 0 <= start < len(nums) and nums[start] == target else -1
    
    def findLastOccurance(self, nums, target):
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1

        return end if 0 <= end < len(nums) and nums[end] == target else -1