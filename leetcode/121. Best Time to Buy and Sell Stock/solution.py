'''
- Link to Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = prices[0]
        result = 0

        for price in prices:
            min_ = min(min_, price)
            result = max(result, price - min_)
        return result