'''
- Link to Problem: https://leetcode.com/problems/path-with-minimum-effort/
- Time Complexity: O(Rows*Cols)
- Space Complexity: O(Rows*Cols)
'''

from typing import List
import heapq
import math

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
      
        dist = [[math.inf]*cols for _ in range(rows)]
        heap = [(0, 0, 0)]

        while heap:
            effort, x, y = heapq.heappop(heap)

            if x == rows - 1 and y == cols - 1:
                return effort
            
            for i, j in ((1,0), (-1,0), (0,1), (0,-1)):
                nx, ny = x+i, y+j
                if not (0 <= nx < rows and 0 <= ny < cols):
                    continue
                new_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                if new_effort >= dist[nx][ny]:
                    continue
                dist[nx][ny] = new_effort
                heapq.heappush(heap, (new_effort, nx, ny))