'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/check-if-tree-is-isomorphic/1
- Time Complexity: O(N**2) [N = min(nodes in root1, nodes in root2)]
- Space Complexity: O(1)
'''


'''
class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def isIsomorphic(self, root1, root2):
        if not (root1 or root2):
            return True
        if not (root1 and root2) or root1.data != root2.data:
            return False
            
        if self.isIsomorphic(root1.left, root2.left) and self.isIsomorphic(root1.right, root2.right):
            return True
        elif self.isIsomorphic(root1.left, root2.right) and self.isIsomorphic(root1.right, root2.left):
            return True
        
        return False