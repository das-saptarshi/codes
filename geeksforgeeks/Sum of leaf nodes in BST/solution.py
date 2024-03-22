'''
- Link to Problem: https://www.geeksforgeeks.org/problems/sum-of-leaf-nodes-in-bst/1
- Time Complexity: O(N) [N = number of nodes in the tree]
- Space Complexity: O(1)
'''

class Solution:
    def sumOfLeafNodes(self, root: 'Node') -> int:
        if not root: return 0
        
        if not (root.left or root.right):
            return root.data
        
        return self.sumOfLeafNodes(root.left) + self.sumOfLeafNodes(root.right)

class Node:
    def __init__(self, data=0):
        self.data=0
        self.left=None
        self.right=None