'''
- Link to Problem: https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/
- Time Complexity: O(NLogN)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        n, operations = len(nums), 0
        largest = nums[-1]

        for i in range(n - 1, -1, -1):
            if nums[i] != largest:
                operations += n - i - 1
                largest = nums[i]
        
        return operations