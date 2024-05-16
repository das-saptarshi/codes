'''
- Link to Problem: https://leetcode.com/problems/evaluate-boolean-binary-tree/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import Optional

class Solution:
    def evaluateTree(self, root: Optional['TreeNode']) -> bool:
        if not root: return True

        if root.val < 2:
            return bool(root.val)
        
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)

        if root.val == 2:
            return left or right
        else:
            return left and right
        
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right