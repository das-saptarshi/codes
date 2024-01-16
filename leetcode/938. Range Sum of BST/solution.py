'''
- Link to Problem: https://leetcode.com/problems/range-sum-of-bst/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.ans = 0

        def BSTSum(root: TreeNode):
            if(root == None):
                return
            
            if(L<=root.val<=R):
                self.ans += root.val
            if(L< root.val):
                BSTSum(root.left)
            if(root.val < R):
                BSTSum(root.right)

        BSTSum(root)
        return self.ans