'''
- Link to Problem: https://www.geeksforgeeks.org/problems/symmetric-tree/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class Solution:
    def isSymmetric(self, root: Node) -> bool:
        if not root:
            return True
        
        def solve(root1: Node, root2: Node) -> bool:
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False
            
            
            if root1.data != root2.data: return False
            
            return solve(root1.left, root2.right) and solve(root1.right, root2.left)
        
        return solve(root.left, root.right)