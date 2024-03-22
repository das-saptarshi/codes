'''
- Link to Problem: https://leetcode.com/problems/invert-binary-tree/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Solution:
    def invertTree(self, root: 'TreeNode') -> 'TreeNode':
        if not root: return root

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root
    
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right