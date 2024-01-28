'''
- Link to Problem: https://leetcode.com/problems/max-consecutive-ones-iii/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        start = end = 0

        for end in range(n):
            if nums[end] == 0:
                k -= 1
            
            if k < 0:
                if nums[start] == 0:
                    k += 1
                start += 1

        return end - start + 1