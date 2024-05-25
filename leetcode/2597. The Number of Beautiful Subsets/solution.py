'''
- Link to Problem: https://leetcode.com/problems/the-number-of-beautiful-subsets/
- Time Complexity: 
- Space Complexity: 
'''

from typing import List
from collections import defaultdict

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        freq_map = defaultdict(int)
        nums.sort()
        return self.count_beautiful_subsets(nums, k, freq_map, 0) - 1

    def count_beautiful_subsets(self, nums, difference, freq_map, i):
        
        if i == len(nums):
            return 1

        total_count = self.count_beautiful_subsets(nums, difference, freq_map, i + 1)

        if nums[i] - difference not in freq_map:
            freq_map[nums[i]] += 1  

            total_count += self.count_beautiful_subsets(
                nums, difference, freq_map, i + 1
            )
            freq_map[nums[i]] -= 1

            if freq_map[nums[i]] == 0:
                del freq_map[nums[i]]

        return total_count