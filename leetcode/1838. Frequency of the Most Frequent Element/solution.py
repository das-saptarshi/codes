
'''
- Link to Problem: https://leetcode.com/problems/frequency-of-the-most-frequent-element/
- Time Complexity: O(NLogN)
- Space Complexity: O(1)
'''
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxFreq = j = total = 0

        for i in range(len(nums)):
            total += nums[i]
            while (i - j + 1) * nums[i] - total > k:
                total -= nums[j]
                j += 1

            maxFreq = max(maxFreq, i - j + 1)
            
        return maxFreq