'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/duplicate-subtree-in-binary-tree/1
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None

from collections import defaultdict

class Solution:
    def dupSub(self, root: Node):
        subTrees = defaultdict(int)
        
        def solve(root: Node):
            if not root:
                return 'N'
                
            subTree = str(root.data)
            if not (root.left or root.right):
                return subTree
            
            subTree += '|' + solve(root.left) + solve(root.right)
            subTrees[subTree] += 1
            return subTree
            
        solve(root)
        return int(any(value > 1 for value in subTrees.values()))