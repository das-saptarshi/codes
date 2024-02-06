'''
- Link to Problem: https://leetcode.com/problems/longest-consecutive-sequence/
- Time Complexity: O(NLogN)
- Space Complexity: O(N)
'''

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))

        ans = 0
        curr = 0
        prev = float('-inf')
        for num in nums:
            if prev + 1 != num:
                ans = max(ans, curr)
                curr = 1
            else:
                curr += 1
            
            prev = num
        
        return max(ans, curr)