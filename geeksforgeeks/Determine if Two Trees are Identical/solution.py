'''
- Link to Problem: https://www.geeksforgeeks.org/problems/determine-if-two-trees-are-identical/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''


class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def isIdentical(self, root1: Node, root2: Node) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        
        if root1.data != root2.data:
            return False
            
        return self.isIdentical(root1.left, root2.left) and self.isIdentical(root1.right, root2.right)