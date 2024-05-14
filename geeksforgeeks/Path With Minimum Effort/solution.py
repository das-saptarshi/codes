'''
- Link to Problem: https://www.geeksforgeeks.org/problems/path-with-minimum-effort/1
- Time Complexity: O(R * C)
- Space Complexity: O(R * C) 
'''

from typing import List
import heapq

class Solution:
    def MinimumEffort(self, rows : int, cols : int, heights : List[List[int]]) -> int:
        priority_queue = [(0, 0, 0)]
        efforts = {}
        
        while priority_queue:
            effort, row, col = heapq.heappop(priority_queue)
            
            if (row == rows - 1 and col == cols - 1): return effort
            
            for i, j in ((1,0), (-1,0), (0,1), (0,-1)):
                r = row + i
                c = col + j
                
                if not (0 <= r < rows and 0 <= c < cols): continue
                
                new_effort = max(effort, abs(heights[row][col] - heights[r][c]))
                
                if new_effort < efforts.get((r, c), float('inf')):
                    efforts[(r, c)] = new_effort
                    heapq.heappush(priority_queue, (new_effort, r, c))
        
        return -1