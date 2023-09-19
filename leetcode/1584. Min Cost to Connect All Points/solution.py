'''
- Link to Problem: https://leetcode.com/problems/min-cost-to-connect-all-points/
- Time Complexity: O(V^2 LogV)
- Space Complexity: O(V)
'''


from typing import List
from collections import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        indexMap = {}
        parent = []
        heap = []

        for i in range(len(points)):
            x = tuple(points[i])
            if x not in indexMap:
                index = len(parent)
                parent.append(index)
                indexMap[x] = index

            for y in points[i+1: ]:
                y = tuple(y)
                dist = abs(x[0] - y[0]) + abs(x[1] - y[1])
                heapq.heappush(heap, (dist, x, y))
        
        mstEdges = total = 0
        while mstEdges != len(parent) - 1:
            dist, x, y = heapq.heappop(heap)
            xIndex, yIndex = indexMap[x], indexMap[y]
            xParent, yParent = self.find(parent, xIndex), self.find(parent, yIndex)
            if xParent == yParent:
                continue
            total += dist
            mstEdges += 1
            self.union(parent, xIndex, yIndex)
        
        return total

    def find(self, parent, i):
        if parent[i] == i:
            return i
        parent[i] = self.find(parent, parent[i])
        return parent[i]
    
    def union(self, parent, i, j):
        iParent = self.find(parent, i)
        jParent = self.find(parent, j)

        parent[iParent] = jParent