'''
- Link to Problem: https://leetcode.com/problems/distribute-coins-in-binary-tree/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import Optional

class Solution:
    def distributeCoins(self, root: Optional['TreeNode']) -> int:
        moves = 0

        def dfs(root):
            nonlocal moves

            if not root: return 0

            left = dfs(root.left)
            right = dfs(root.right)

            coins = root.val + left + right - 1
            moves += abs(left) + abs(right)

            return coins
        
        dfs(root)
        return moves
    
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right