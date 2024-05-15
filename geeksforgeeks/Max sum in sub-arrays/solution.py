'''
- Link to Problem: https://www.geeksforgeeks.org/problems/max-sum-in-sub-arrays0824/0
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def pairWithMaxSum(self, nums: List[int], n: int) -> int:
        return max(nums[i] + nums[i + 1] for i in range(n - 1))