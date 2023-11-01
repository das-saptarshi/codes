'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/level-of-nodes-1587115620/1
- Time Complexity: O(V)
- Space Complexity: O(V)
'''

from typing import List

class Solution:
    def nodeLevel(self, V: int, adj: List[List[int]], X: int) -> int:
        
        queue = [0]
        level = 0
        
        visited = [False] * V
        while queue:
            
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node == X:
                    return level
                visited[node] = True
                
                for nextNode in adj[node]:
                    if not visited[nextNode]:
                        queue.append(nextNode)
            level += 1
        
        return -1