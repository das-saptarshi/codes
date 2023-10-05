'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/right-view-of-binary-tree/1
- Time Complexity: O(N) [N: number of nodes in the tree]
- Space Complexity: O(1)
'''

class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def rightView(self, root: Node):
        view = []
        
        def solve(root, index):
            if not root:
                return
            
            if len(view) == index:
                view.append(root.data)
            
            solve(root.right, index + 1)
            solve(root.left, index + 1)
        
        solve(root, 0)
        return view