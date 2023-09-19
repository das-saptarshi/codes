'''
- Link to Problem: https://leetcode.com/problems/shortest-path-visiting-all-nodes/
- Time Complexity: O(2**n * n)
- Space Complexity: O(2**n * n)
'''

from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph) == 1:
            return 0
        
        n = len(graph)
        queue = [(node, 1 << node) for node in range(n)]
        seen = set(queue)
        endMask = (1 << n) - 1
        steps = 0
        
        while queue:
            
            for _ in range(len(queue)):
                node, mask = queue.pop(0)
                
                if mask == endMask:
                    return steps
                
                for neighbor in graph[node]:
                    nextMask = (mask | (1 << neighbor))
                    if (neighbor, nextMask) in seen:
                        continue
                    seen.add((neighbor, nextMask))
                    queue.append((neighbor, nextMask))
            
            steps += 1
        
        return -1
    