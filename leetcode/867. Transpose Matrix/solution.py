'''
- Link to Problem: https://leetcode.com/problems/transpose-matrix/
- Time Complexity: O(R * C) [R = number of rows, C = number of columns]
- Space Complexity: O(R * C)
'''

from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        transpose = [[0] * rows for _ in range(cols)]

        for j in range(rows):
            for i in range(cols):
                transpose[i][j] = matrix[j][i]
        return transpose