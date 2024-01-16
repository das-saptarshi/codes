'''
- Link to Problem: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def helper(root: TreeNode, cur_max, cur_min):
            if not root:
                return cur_max - cur_min
            
            cur_max = max(cur_max, root.val)
            cur_min = min(cur_min, root.val)
            left = helper(root.left, cur_max, cur_min)
            right = helper(root.right, cur_max, cur_min)
            return max(left, right)
        return helper(root, root.val, root.val)
        