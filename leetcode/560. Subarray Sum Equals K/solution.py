'''
- Link to Problem: https://leetcode.com/problems/subarray-sum-equals-k/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count = defaultdict(int)
        prefix_sum = total = 0

        for num in nums:
            prefix_sum += num

            target = prefix_sum - k
            if prefix_sum == k: total += 1
            total += prefix_sum_count[target]
 
            prefix_sum_count[prefix_sum] += 1
        
        return total