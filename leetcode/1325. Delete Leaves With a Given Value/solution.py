'''
- Link to Problem: https://leetcode.com/problems/delete-leaves-with-a-given-value/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''


from typing import Optional

class Solution:
    def removeLeafNodes(self, root: Optional['TreeNode'], target: int) -> Optional['TreeNode']:
        if not root: return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if root.val == target and not (root.left or root.right):
            return None
        
        return root


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right