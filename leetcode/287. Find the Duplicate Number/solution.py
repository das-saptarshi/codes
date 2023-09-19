'''
- Link to Problem: https://leetcode.com/problems/find-the-duplicate-number
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        freq = [0]*n

        for x in nums:
            if freq[x] > 0:
                return x
            freq[x] = 1