'''
- Link to Problem: https://leetcode.com/problems/subsets-ii/
- Time Complexity: O(2^N)
- Space Complexity: O(N)
'''

from typing import List
from collections import Counter

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def solve(index, subset):
            if index == n:
                subsets.append(subset[:])
                return
            
            totalCount = counter[elems[index]]

            for count in range(totalCount + 1):
                solve(index + 1, subset + [elems[index]] * count)
            
        subsets = []
        counter = Counter(nums)
        elems = list(counter.keys())
        n = len(elems)
        solve(0, [])

        return subsets