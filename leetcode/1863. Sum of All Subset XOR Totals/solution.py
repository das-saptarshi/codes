'''
- Link to Problem: https://leetcode.com/problems/sum-of-all-subset-xor-totals/
- Time Complexity: O(2 ^ N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def generate_subsets(index, current_xor):
            if index == len(nums): return current_xor

            with_element = generate_subsets(index + 1, current_xor ^ nums[index])
            without_element = generate_subsets(index + 1, current_xor)

            return with_element + without_element
        
        return generate_subsets(0, 0)