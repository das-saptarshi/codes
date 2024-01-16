'''
- Link to Problem: https://leetcode.com/problems/leaf-similar-trees/
- Time Complexity: O(N + M)
- Space Complexity: O(N + M)
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leafValueSequence1 = self.leafValueSequence(root1)
        leafValueSequence2 = self.leafValueSequence(root2)
        
        return leafValueSequence1 == leafValueSequence2

    
    def leafValueSequence(self, root: TreeNode):
        if not root:
            return []
        
        
        if not root.left and not root.right:
            return [root.val]
        
        ans = self.leafValueSequence(root.left)
        ans += self.leafValueSequence(root.right)
        return ans
        