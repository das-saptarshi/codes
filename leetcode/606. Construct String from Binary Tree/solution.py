'''
- Link to Problem: https://leetcode.com/problems/construct-string-from-binary-tree/
- Time Complexity: O(N) [N = number of nodes]
- Space Complexity: O(1)
'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''

        ans = str(root.val)
        if root.left or root.right:
            ans += f'({self.tree2str(root.left)})'
        if root.right:
            ans += f'({self.tree2str(root.right)})'
        
        return ans
        