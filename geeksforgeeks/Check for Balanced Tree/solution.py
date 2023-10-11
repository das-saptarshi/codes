'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/check-for-balanced-tree/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: Node):
        def solve(root: Node):
            if not root:
                return 0
            
            left, right = solve(root.left), solve(root.right)
            if abs(left - right) > 1:
                self.balanced = False
            
            return max(left, right) + 1
        
        self.balanced = True
        solve(root)
        return self.balanced