'''
- Link to Problem: https://www.geeksforgeeks.org/problems/clone-graph/1
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from sys import setrecursionlimit
from typing import List

class Solution():
    def cloneGraph(self, node: 'Node'):
        nodes = {}
        
        def solve(node: 'Node'):
            if node.val in nodes:
                return nodes[node.val]
            
            clone = Node(node.val, list())
            nodes[clone.val] = clone
            
            for neighbor in node.neighbors:
                clone.neighbors.append(solve(neighbor))
            
            return clone
        
        
        return solve(node)

class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors: List[Node] = neighbors

setrecursionlimit(100000)