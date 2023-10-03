'''
- Link to Problem: https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/
- Time Complexity: O(NlogN)
- Space Complexity: O(N)
'''

from typing import List
from collections import defaultdict

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        neighbors = defaultdict(list)
        inDegree = defaultdict(int)
        ancestors = defaultdict(set)

        for x, y in edges:
            neighbors[x].append(y)
            inDegree[y] += 1
        
        queue = [x for x in range(n) if inDegree[x] == 0]

        while queue:
            x = queue.pop(0)

            for neighbor in neighbors[x]:
                ancestors[neighbor].update(ancestors[x])
                ancestors[neighbor].add(x)
                inDegree[neighbor] -= 1

                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return [sorted(list(ancestors[x])) for x in range(n)]