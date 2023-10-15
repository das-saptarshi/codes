'''
- Link to Problem: https://leetcode.com/problems/painting-the-walls/
- Time Complexity: O(N^2)
- Space Complexity: O(N)
'''

from typing import List
from functools import cache

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        postfixTime = time[:]
        for i in range(len(time) - 2, -1, -1):
            postfixTime[i] += postfixTime[i + 1]
        
        @cache
        def solve(index, cumulativeTime):
            if index == len(cost):
                return 0 if cumulativeTime >= 0 else float('inf')
            
            if cumulativeTime >= len(time) - index:
                return 0

            if cumulativeTime + postfixTime[index] < 0:
                return float('inf')

            return min(
                solve(index + 1, cumulativeTime - 1),
                cost[index] + solve(index + 1, cumulativeTime + time[index])
            )
            
        return solve(0 , 0)