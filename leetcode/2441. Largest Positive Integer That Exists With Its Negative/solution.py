'''
- Link to Problem: https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        negatives = set(num for num in nums if num < 0)
        return max((num for num in nums if num > 0 and -num in negatives), default=-1)