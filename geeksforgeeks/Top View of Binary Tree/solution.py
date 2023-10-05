'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1
- Time Complexity: O(N) [N: number of nodes]
- Space Complexity: O(N)
'''

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def topView(self, root: Node):
        elems = {}
        queue = [(root, 0)]
        
        while queue:
            for _ in range(len(queue)):
                root, x = queue.pop(0)
                if root.left: queue.append((root.left, x - 1))
                if root.right: queue.append((root.right, x + 1))
                if x not in elems: elems[x] = root.data
        
        return [elems[key] for key in sorted(elems.keys())]