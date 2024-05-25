'''
- Link to Problem: https://leetcode.com/problems/subsets/
- Time Complexity: O(2ᴺ)
- Space Complexity: O(N * N)
'''

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def generate(index, subset):
            if index == len(nums):
                subsets.append(subset[:])
                return
            
            generate(index + 1, subset)
            generate(index + 1, subset + [nums[index]])
        
        subsets = []
        generate(0, [])
        return subsets