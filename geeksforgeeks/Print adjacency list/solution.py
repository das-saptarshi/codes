'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/print-adjacency-list-1587115620/1
- Time Complexity: O(K) [K = number of edges]
- Space Complexity: O(K)
'''

from typing import List


class Solution:
    def printGraph(self, V : int, edges : List[List[int]]) -> List[List[int]]:
        adjList = [[] for _ in range(V)]
        
        for x, y in edges:
            adjList[x].append(y)
            adjList[y].append(x)
        
        return adjList