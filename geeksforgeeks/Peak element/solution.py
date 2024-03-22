'''
- Link to Problem: https://www.geeksforgeeks.org/problems/peak-element/1
- Time Complexity: O(LogN)
- Space Complexity: O(1)
'''

from typing import List

class Solution:   
    def peakElement(self, nums: List[int], n: int) -> int:
        
        left, right = 0, n - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[mid + 1]:
                if nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    right = mid - 1
            else:
                left = mid + 1
        
        return left