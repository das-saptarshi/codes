'''
- Link to Problem: https://leetcode.com/problems/diagonal-traverse-ii/
- Time Complexity: O(N * M)
- Space Complexity: O(N * M)
'''

from typing import List
from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                d[i+j].append(nums[i][j])
        
        return [value for values in d.values() for value in reversed(values)]