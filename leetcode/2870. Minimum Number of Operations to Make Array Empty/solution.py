'''
- Link to Problem: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from typing import List
from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 0

        for value in freq.values():
            if value == 1: return -1
            ans += value // 3 + int(value % 3 != 0)
        
        return ans