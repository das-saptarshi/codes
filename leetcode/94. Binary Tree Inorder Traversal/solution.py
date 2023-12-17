'''
- Link to Problem: https://leetcode.com/problems/binary-tree-inorder-traversal/
- Time Complexity: O(N) [N = number of nodes]
- Space Complexity: O(N)
'''

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)