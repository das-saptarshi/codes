'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram-1587115620/1
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from typing import List

class Solution:
    def getMaxArea(self, histogram: List[int]):
        stack = []
        maxArea = i = 0
        
        while i < len(histogram):
            if not stack or histogram[stack[-1]] <= histogram[i]:
                stack.append(i)
                i += 1
            else:
                maxArea = max(maxArea, self.getArea(histogram, stack, i))
                
        while stack:
            maxArea = max(maxArea, self.getArea(histogram, stack, i))
        
        return maxArea
        
    
    def getArea(self, histogram: List[int], stack: List[int], i: int):
        tos = stack.pop()
        return histogram[tos] * ((i - stack[-1] - 1) if stack else i)