'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/normal-bst-to-balanced-bst/1
- Time Complexity: O(N)
- Space Complexity: O(N)
'''


from typing import List

class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def buildBalancedTree(self, root: Node):
        return self.buildBST(
                self.inorderTraversal(root)
            )
        
    def inorderTraversal(self, root: Node):
        if not root:
            return []
        
        return self.inorderTraversal(root.left) + [root.data] + self.inorderTraversal(root.right)
    
    def buildBST(self, elems: List[int]):
        if not elems:
            return None
        
        mid = len(elems) // 2
        
        root = Node(elems[mid])
        root.left = self.buildBST(elems[:mid])
        root.right = self.buildBST(elems[mid + 1:])