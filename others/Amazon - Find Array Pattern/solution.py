'''
- Problem: There are four types of patterns. Monotonic Increasing, Monotonic Decreasing, Increasing then Decreasing, and Decreasing then Increasing. Given an array, identify accordingly.
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def checkPattern(self, nums: List[int]):
        isMonotonicIncreasing, monotonicIncreasingIndex = self.isMonotonicIncreasing(nums)
        isMonotonicDecreasing, monotonicDecreasingIndex = self.isMonotonicDecreasing(nums)
        
        if isMonotonicIncreasing:
            return 'Monotonic Increasing'
        elif isMonotonicDecreasing:
            return 'Monotonic Decreasing'
        
        isDecreasingThenIncreasing, _ = self.isMonotonicIncreasing(nums[monotonicDecreasingIndex:])
        isIncreasingThenDecreasing, _ = self.isMonotonicDecreasing(nums[monotonicIncreasingIndex:])
        
        if isDecreasingThenIncreasing:
            return 'Increasing then Decreasing'
        elif isIncreasingThenDecreasing:
            return 'Decreasing then Increasing'
            
        return 'Unknown Pattern'
    
    def isMonotonicIncreasing(self, nums):
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                continue
            else:
                return False, i
        
        return True, len(nums) - 1
    
    def isMonotonicDecreasing(self, nums):
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                continue
            else:
                return False, i
        
        return True, len(nums) - 1