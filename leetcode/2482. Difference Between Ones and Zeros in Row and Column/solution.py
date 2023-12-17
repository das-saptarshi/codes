'''
- Link to Problem: https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/
- Time Complexity: O(R * C) [R = number of rows, C = number of columns]
- Space Complexity: O(R * C)
'''

from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        onesInRow = [0] * rows
        onesInCol = [0] * cols

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    onesInRow[i] += 1
                    onesInCol[j] += 1
        
        diff = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                diff[i][j] = 2 * (onesInRow[i] + onesInCol[j]) - (rows + cols)
        
        return diff