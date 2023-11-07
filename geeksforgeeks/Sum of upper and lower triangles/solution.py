'''
- Link to Problem: https://www.geeksforgeeks.org/problems/sum-of-upper-and-lower-triangles-1587115621/1
- Time Complexity: O(N^2)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def sumTriangles(self, matrix: List[List[int]], n: int):
        upperTriangle = lowerTriangle = 0
        
        for i in range(n):
            for j in range(n):
                if i <= j: upperTriangle += matrix[i][j]
                if i >= j: lowerTriangle += matrix[i][j]
        
        return upperTriangle, lowerTriangle