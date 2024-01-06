'''
- Link to Problem: https://leetcode.com/problems/maximum-profit-in-job-scheduling/
- Time Complexity: O(NLogN)
- Space Complexity: O(N)
'''

from typing import List
from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        numberOfJobs = len(jobs)
        dp = [0] * (numberOfJobs + 1)

        for i, (currentEndTime, currentStartTime, currentProfit) in enumerate(jobs):
            pos = bisect_right(jobs, currentStartTime, hi=i, key=lambda x: x[0])
            dp[i + 1] = max(dp[i], dp[pos] + currentProfit)
        
        return dp[numberOfJobs]