'''
- Link to Problem: https://leetcode.com/problems/maximum-subarray/
- Time Complexity: O(N)
- Space Complexity: O(1)
- Metadata:
    - Algorithm: Kadane's Algorithm
'''

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0

        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)

            if current_sum < 0:
                current_sum = 0
        
        return max_sum