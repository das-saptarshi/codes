'''
- Link to Problem: https://leetcode.com/problems/find-the-safest-path-in-a-grid/
- Time Complexity: O(N * N * LogN)
- Space Complexity: O(N * N)
'''

import heapq
from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = []
        directions = ((1,0), (-1,0), (0,1), (0,-1))

        def is_valid_cell(n, r, c):
            return (0 <= r < n and 0 <= c < n)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                grid[i][j] -= 1
        
        while queue:
            for _ in range(len(queue)):
                row, col = queue.pop(0)
                safeness = grid[row][col]

                for i, j in directions:
                    r, c = row + i, col + j

                    if is_valid_cell(n, r, c) and grid[r][c] == -1:
                        grid[r][c] = safeness + 1
                        queue.append((r, c))

        
        priority_queue = [(-grid[0][0], 0, 0)]
        grid[0][0] = -1


        while priority_queue:
            safeness, row, col = heapq.heappop(priority_queue)

            if row == n - 1 and col == n - 1: 
                return -safeness

            for i, j in directions:
                r, c = row + i, col + j

                if is_valid_cell(n, r, c) and grid[r][c] != -1:
                    heapq.heappush(priority_queue, (-min(-safeness, grid[r][c]), r, c))
                    grid[r][c] = -1
            
        
        return -1