'''
- Link to Problem: https://www.geeksforgeeks.org/problems/children-sum-parent/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Solution:
    def isSumProperty(self, root: 'Node'):
        
        def solve(root: 'Node'):
            if not root:
                return True, 0
                
            if not (root.left or root.right):
                return True, root.data
            
            leftCond, leftValue = solve(root.left)
            rightCond, rightValue = solve(root.right)
            
            if leftCond and rightCond and (leftValue + rightValue) == root.data:
                return True, root.data
            
            return False, root.data
        
        ans, _ = solve(root)
        return int(ans)

class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None