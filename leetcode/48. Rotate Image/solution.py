'''
- Link to Problem: https://leetcode.com/problems/rotate-image/
- Time Complexity: O(N * N)
- Space Complexity: O(1)
'''

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        
        for a in range(n//2):
            
            for b in range(a, n-1-a):
                i = a
                j = b
                temp = matrix[i][j]
                for _ in range(4):
                    x, y = j, n - i - 1
                    matrix[x][y], temp = temp, matrix[x][y]
                    i, j = x, y
        