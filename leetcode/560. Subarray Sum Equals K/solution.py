'''
- Link to Problem: https://leetcode.com/problems/subarray-sum-equals-k/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        prev = {}
        ans = 0
        for num in nums:
            if num == k:
                ans += 1
            if (num - k) in prev:
                ans += prev[num-k]
            prev[num] = prev.get(num, 0) + 1
        return ans