'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/flattening-a-linked-list--170645/1
- Time Complexity: O(N * M) [N: number of root nodes, M: maximum length of bottom chain]
- Space Complexity: O(N)
'''

from typing import List
import math

class Node:
    def __init__(self, data):
        self.data = data
        self.next=None
        self.bottom=None

class Solution():
    
    def flatten(self, root: Node):
        roots: List[Node] = []
        
        while root:
            roots.append(root)
            root = root.next
        
        result = curr = Node(0)
        while True:
            value = math.inf
            rootIndex = -1
            for i in range(len(roots)):
                if roots[i] and roots[i].data < value:
                    value = roots[i].data
                    rootIndex = i
            if rootIndex == -1:
                break
            roots[rootIndex] = roots[rootIndex].bottom
            curr.bottom = Node(value)
            curr = curr.bottom
        
        return result.bottom