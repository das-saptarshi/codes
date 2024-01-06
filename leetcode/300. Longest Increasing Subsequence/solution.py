'''
- Link to Problem: https://leetcode.com/problems/longest-increasing-subsequence/
- Time Complexity: O(NlogN)
- Space Complexity: O(N)
'''

from typing import List
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = []
        
        for x in nums:
            pos = bisect_left(dp, x)
            if pos == len(dp):
                dp.append(x)
            else:
                dp[pos] = x
        return len(dp)