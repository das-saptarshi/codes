'''
- Link to Problem: https://leetcode.com/problems/partition-array-for-maximum-sum/
- Time Complexity: O(N * K)
- Space Complexity: O(N)
'''

from typing import List
from functools import lru_cache

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        @lru_cache(maxsize=None)
        def solve(index: int):
            if index >= n: return 0

            ans = 0
            currMax = arr[index]
            for i in range(1, k + 1):
                if index + i - 1 >= n:
                    break
                currMax = max(currMax, arr[index + i - 1])
                ans = max(ans, currMax * i + solve(index + i))
            
            return ans
        
        n = len(arr)
        return solve(0)
            
            