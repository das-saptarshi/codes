'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/transitive-closure-of-a-graph0930/1
- Time Complexity: O(N^3)
- Space Complexity: O(N^2)
'''

from collections import defaultdict
from typing import List

class Solution:
    def transitiveClosure(self, N: int, graph: List[List[int]]) -> List[List[int]]:
        closure = [[0] * N for _ in range(N)]
        graph = self.buildGraph(N, graph)
        
        for node in range(N):
            self.traverse(N, node, graph, closure)
        
        return closure
        
    def traverse(self, N: int, node: int, graph: List[List[int]], closure: List[List[int]]) -> None:
        queue = graph[node][:]
        
        seen = [False] * N
        closure[node][node] = 1
        
        while queue:
            x = queue.pop(0)
            if seen[x]:
                continue
            seen[x] = True
            
            closure[node][x] = 1
            for neighbor in graph[x]:
                queue.append(neighbor)
        
    
    def buildGraph(self, N: int, graph: List[List[int]]) -> defaultdict(list):
        adj = defaultdict(list)
        
        for i in range(N):
            for j in range(N):
                if graph[i][j] == 1:
                    adj[i].append(j)
        
        return adj