'''
- Link to Problem: https://leetcode.com/problems/path-with-maximum-gold/
- Time Complexity: O(M * N * (4 ^ G)) [M = number of rows, N = number of cols, G = number of gold cells]
- Space Complexity: O(G)
'''

from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def traverse(r, c):
            if not(0 <= r < row and 0 <= c < col and grid[r][c] > 0):
                return 0
            
            gold = 0
            grid[r][c] *= -1

            for i, j in ((0,1), (0,-1), (1,0), (-1,0)):
                gold = max(gold, traverse(r + i, c + j))
            
            grid[r][c] *= -1
            return gold + grid[r][c]
        
        row, col = len(grid), len(grid[0])
        gold = 0
        for i in range(row):
            for j in range(col):
                gold = max(gold, traverse(i, j))
        
        return gold