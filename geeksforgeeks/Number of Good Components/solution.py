'''
- Link to Problem: https://www.geeksforgeeks.org/problems/number-of-good-components--170647/1
- Time Complexity: O(V + E) [V = number of nodes, E = number of edges]
- Space Complexity: O(V + E)
'''

from typing import List
from collections import defaultdict

class Solution:
    def findNumberOfGoodComponent(self, e : int, v : int, edges : List[List[int]]) -> int:
        adj = defaultdict(set)
        
        for x, y in edges:
            adj[x].add(y)
            adj[y].add(x)
            
        def make_group(node):
            visited[node] = True
            group = [node]
            
            for next_node in adj[node]:
                if visited[next_node]: continue
                
                group.extend(make_group(next_node))
            
            return group
        
        
        visited = [False] * (v + 1)
        
        groups = []
        
        for node in range(1, v + 1):
            if not visited[node]:
                groups.append(make_group(node))
        
        
        good_components = 0
        
        
        for group in groups:
            degree = len(group) - 1
            
            if all(len(adj[node]) == degree for node in group):
                good_components += 1
        
        return good_components