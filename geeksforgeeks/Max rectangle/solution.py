'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/max-rectangle/1
- Time Complexity: O(R * C) [R: rows, C: cols]
- Space Complexity: O(C)
'''

from typing import List

class Solution:
    def maxArea(self, matrix: List[List[int]], n: int, m: int):
        maxArea = self.maxAreaUnderHist(matrix[0])
        
        for i in range(1, n):
            for j in range(m):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i - 1][j]
                    
            maxArea = max(maxArea, self.maxAreaUnderHist(matrix[i]))
        
        return maxArea
    
    def maxAreaUnderHist(self, hist: List[int]):
        stack = []
        maxArea = i = 0
        
        while i < len(hist):
            if not stack or hist[stack[-1]] <= hist[i]:
                stack.append(i)
                i += 1
            else:
                maxArea = max(maxArea, self.calculateArea(hist, stack, i))
                
        while stack:
            maxArea = max(maxArea, self.calculateArea(hist, stack, i))
        
        return maxArea
    
    def calculateArea(self, hist: List[int], stack: List[int], i: int):
        tos = stack.pop()
        return hist[tos] * ((i - stack[-1] - 1) if stack else i)