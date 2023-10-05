'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1
- Time Complexity: O(N) [N: number of nodes]
- Space Complexity: O(N)
'''


class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

class Solution:
    def bottomView(self, root: Node):
        if not root:
            return []
            
        queue = [(root, 0)]
        elems = {}
        
        while queue:
            for _ in range(len(queue)):
                root, x = queue.pop(0)
                if root.left: queue.append((root.left, x-1))
                if root.right: queue.append((root.right, x+1))
                elems[x] = root.data
        return [elems[key] for key in sorted(elems.keys())]
