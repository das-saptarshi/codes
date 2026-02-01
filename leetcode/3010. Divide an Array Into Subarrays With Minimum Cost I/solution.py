'''
- Link to Problem: https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        smallest = second_smallest = float('inf')

        for num in nums[1:]:
            if num < smallest:
                smallest, second_smallest = num, smallest
            elif num < second_smallest:
                second_smallest = num
        
        return nums[0] + smallest + second_smallest