'''
- Link to Problem: https://leetcode.com/problems/loud-and-rich/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from typing import List

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        neighbors = [[] for _ in range(n)]
        inDegree = [0]*n
        result = list(range(n))

        for a, b in richer:
            neighbors[a].append(b)
            inDegree[b] += 1
        
        queue = [x for x in range(n) if inDegree[x] == 0]

        while queue:
            x = queue.pop(0)
            
            for neighbor in neighbors[x]:
                a, b = result[neighbor], result[x]
                if quiet[a] > quiet[b]:
                    result[neighbor] = b

                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        return result