'''
- Link to Problem: https://leetcode.com/problems/first-missing-positive/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n, i = len(nums), 0

        while i < n:
            correct = nums[i] - 1

            if 0 <= correct < n and nums[correct] != nums[i]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
            
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1