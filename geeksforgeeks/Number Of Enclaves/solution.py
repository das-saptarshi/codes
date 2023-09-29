'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/number-of-enclaves/1
- Time Complexity: O(R*C) [R: number of rows, C: number of columns]
- Space Complexity: O(1)
'''

from typing import List
import sys

sys.setrecursionlimit(100000)
class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        self.mergeBoundaryLands(0, 0, rows, cols, grid)
        self.countLands(0, 0, rows, cols, grid)
        
        for i in range(rows):
            self.mergeBoundaryLands(i, 0, rows, cols, grid)
            self.mergeBoundaryLands(i, cols-1, rows, cols, grid)
            
        for j in range(cols):
            self.mergeBoundaryLands(0, j, rows, cols, grid)
            self.mergeBoundaryLands(rows-1, j, rows, cols, grid)
        
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    ans += self.countLands(i, j, rows, cols, grid)
        
        return ans
        
        
        
    
    def mergeBoundaryLands(self, x, y, rows, cols, grid):
        if not(0 <= x < rows and 0 <= y < cols and grid[x][y] == 1):
            return
        
        grid[x][y] = 0
        
        for i, j in ((0,1), (0,-1), (1,0), (-1,0)):
            self.mergeBoundaryLands(x+i, y+j, rows, cols, grid)
    
    
    def countLands(self, x, y, rows, cols, grid):
        if not(0 <= x < rows and 0 <= y < cols and grid[x][y] == 1):
            return 0
        
        grid[x][y] = 0
        ans = 1
        for i, j in ((0,1), (0,-1), (1,0), (-1,0)):
            ans += self.countLands(x+i, y+j, rows, cols, grid)
            
        return ans