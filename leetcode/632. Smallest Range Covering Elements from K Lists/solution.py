'''
- Link to Problem: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
- Time Complexity: O(KLogK + NLogK)
- Space Complexity: O(K)
'''

import heapq
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        max_ = float('-inf')
        x, y = float('-inf'), float('inf')
        
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
            max_ = max(max_, nums[i][0])
        
        while heap:
            min_, index, position = heapq.heappop(heap)

            if (max_ - min_) < (y - x):
                x = min_
                y = max_
            
            position += 1
            if position == len(nums[index]):
                break
            
            heapq.heappush(heap, (nums[index][position], index, position))
            max_ = max(max_, nums[index][position])
        
        return (x, y)
