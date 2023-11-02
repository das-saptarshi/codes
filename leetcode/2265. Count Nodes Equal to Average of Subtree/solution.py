'''
- Link to Problem: https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def solve(root: TreeNode):
            if not root: return 0, 0, 0

            leftTotal, leftNodes, leftAvgNodes = solve(root.left)
            rightTotal, rightNodes, rightAvgNodes = solve(root.right)

            avgNodes = leftAvgNodes + rightAvgNodes
            avg = (root.val + leftTotal + rightTotal) // (leftNodes + rightNodes + 1)

            if avg == root.val:
                avgNodes += 1
            
            return (
                leftTotal + rightTotal + root.val,
                leftNodes + rightNodes + 1,
                avgNodes
            )
        
        _, _, ans = solve(root)
        return ans