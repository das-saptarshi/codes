'''
- Link to Problem: https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
- Time Complexity: O(NLogN)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles) // 3
        return sum(x for x in piles[1:-n:2])