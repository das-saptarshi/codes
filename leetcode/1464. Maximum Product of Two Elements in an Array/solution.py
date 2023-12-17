'''
- Link to Problem: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = max(nums)
        nums.remove(first)
        second = max(nums)
        
        return (first-1)*(second-1)