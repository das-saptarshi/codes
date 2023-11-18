'''
- Link to Problem: https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/
- Time Complexity: O(K * N) [K: avg len of group in groups, N: len of nums]
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i = 0
        for group in groups:
            for j in range(i, len(nums)):
                if nums[j: j + len(group)] == group:
                    i = j + len(group)
                    break
            else:
                return False
        
        return True