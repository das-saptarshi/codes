'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/eventual-safe-states/1
- Time Complexity: O(V)
- Space Complexity: O(V)
'''

from typing import List

class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        safeState = [None] * V
        
        for node in range(V):
            if safeState[node] is None:
                self.isSafe(node, adj, safeState)
        
        
        return [node for node in range(V) if safeState[node]]
        
    
    def isSafe(self, node: int, adj: List[List[int]], safeState: List[int]):
        if safeState[node] is not None:
            return safeState[node]
        
        safeState[node] = False
        
        for nextNode in adj[node]:
            if not self.isSafe(nextNode, adj, safeState):
                return False
        
        safeState[node] = True
        return True