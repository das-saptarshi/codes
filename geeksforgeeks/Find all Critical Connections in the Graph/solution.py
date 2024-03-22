'''
- Link to Problem: https://www.geeksforgeeks.org/problems/critical-connections/1
- Time Complexity: O(V + E)
- Space Complexity: O(V)
'''

from typing import List

class Solution:
    def criticalConnections(self, v: int, adj: List[int]) -> List[List[int]]:
        def bridge(node: int) -> None:
            nonlocal time
            
            visited[node] = True
            disc[node] = time
            low[node] = time
            time += 1
            
            for nextNode in adj[node]:
                
                if not visited[nextNode]:
                    parent[nextNode] = node
                    bridge(nextNode)
                    
                    low[node] = min(low[node], low[nextNode])
                    
                    if low[nextNode] > disc[node]:
                        bridges.append([min(node, nextNode), max(node, nextNode)])
                        
                elif nextNode != parent[node]:
                    low[node] = min(low[node], disc[nextNode])
            
        
        time = 0
        visited = [False] * v
        disc = [False] * v
        low = [False] * v
        parent = [-1] * v
        bridges = []
        
        for i in range(v):
            if not visited[i]:
                bridge(i)
        
        return sorted(bridges)