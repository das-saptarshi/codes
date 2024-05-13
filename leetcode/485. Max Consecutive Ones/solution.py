'''
- Link to Problem: https://leetcode.com/problems/max-consecutive-ones/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_ones_count = 0
        ones_count = 0

        for num in nums:
            if num == 1: ones_count += 1
            else: 
                max_ones_count = max(max_ones_count, ones_count)
                ones_count = 0
        
        return max(max_ones_count, ones_count)