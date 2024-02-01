'''
- Link to Problem: https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/
- Time Complexity: O(NlogN)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] > k: return []
            result.append(nums[i: i + 3])
        
        return result
        