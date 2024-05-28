'''
- Link to Problem: https://www.geeksforgeeks.org/problems/minimum-cost-to-fill-given-weight-in-a-bag1956/1
- Time Complexity: O(N * W)
- Space Complexity: O(W)
'''

from typing import List

class Solution:
    def minimumCost(self, n : int, w : int, cost : List[int]) -> int:
        memo = [float('inf')] * (w + 1)
        memo[0] = 0
        
        for i in range(n):
            for j in range(i + 1, w + 1):
                memo[j] = min(memo[j], cost[i] + memo[j - i - 1])
        
        return memo[w]