'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/binary-tree-to-bst/1
- Time Complexity: O(NlogN) (2N to traverse the tree, and NlogN to sort the tree)
- Space Complexity: O(N)
'''


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def binaryTreeToBST(self, root: Node) -> Node:
        values = sorted(self.getValues(root))
        self.makeBST(root, values)
        return root
        
    
    def makeBST(self, root, values):
        if not root:
            return
        
        self.makeBST(root.left, values)
        root.data = values.pop(0)
        self.makeBST(root.right, values)
    
    def getValues(self, root):
        if not root:
            return []
        
        return self.getValues(root.left) + [root.data] + self.getValues(root.right)