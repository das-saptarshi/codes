'''
- Link to Problem: https://leetcode.com/problems/design-graph-with-shortest-path-calculator/
- Time Complexity: 
                    1. Initialization: O(E) [E: length of edges]
                    2. Add Edge: O(1) 
                    3. Shortest Path: O(ELogV) [E: length of edges, V: number of nodes]
- Space Complexity: O(E + V)
'''

import heapq
from typing import List

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = [[] for _ in range(n)] 
        for src, dst, weight in edges:
            self.graph[src].append((dst, weight))

    def addEdge(self, edge: List[int]) -> None:
        src, dst, weight = edge
        self.graph[src].append((dst, weight))

    def shortestPath(self, src: int, dst: int) -> int:
        heap = []
        heapq.heappush(heap, (0, src))

        dist = [float('inf')] * self.n
        dist[src] = 0

        while heap:
            _, node = heapq.heappop(heap)

            for neighbor, weight in self.graph[node]:
                if dist[neighbor] > dist[node] + weight:
                    dist[neighbor] = dist[node] + weight
                    heapq.heappush(heap, (dist[neighbor], neighbor))
        
        return -1 if dist[dst] == float('inf') else dist[dst]