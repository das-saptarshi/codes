'''
- Link to Problem: https://leetcode.com/problems/design-graph-with-shortest-path-calculator/
- Time Complexity:
                    1. O(V^3) [V: number of nodes]
                    2. O(V^2) [V: number of nodes]
                    3. O(1)

- Space Complexity: O(V^2)
'''


from typing import List

class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.distance = [[float('inf')]*n for _ in range(n)]

        for i in range(n):
            self.distance[i][i] = 0

        for src, dst, weight in edges:
            self.distance[src][dst] = weight

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    self.distance[i][j] = min(
                        self.distance[i][j],
                        self.distance[i][k] + self.distance[k][j]
                    )

    def addEdge(self, edge: List[int]) -> None:
        src, dst, weight = edge
        if self.distance[src][dst] <= weight:
            return
        
        for i in range(self.n):
            for j in range(self.n):
                self.distance[i][j] = min(
                    self.distance[i][j],
                    self.distance[i][src] +  weight + self.distance[dst][j]
                )

    def shortestPath(self, src: int, dst: int) -> int:
        distance = self.distance[src][dst]
        return -1 if distance == float('inf') else distance