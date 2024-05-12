'''
- Link to Problem: https://leetcode.com/problems/largest-local-values-in-a-matrix/
- Time Complexity: O(N ^ 2)
- Space Complexity: O(N ^ 2)
'''

from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        local_grid = []

        for i in range(n - 2):
            local_grid.append(list())
            for j in range(n - 2):
                local_grid[i].append(self.find_largest_local_value(grid, i, j))
        
        return local_grid
    

    def find_largest_local_value(self, grid: List[List[int]], row: int, col: int) -> int:
        largest = 0
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                largest = max(largest, grid[i][j])
        
        return largest