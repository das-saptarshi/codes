'''
- Link to Problem: https://leetcode.com/problems/number-of-good-pairs/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from typing import List
from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = Counter(nums)
        return sum(x * (x - 1) // 2 for x in freq.values())