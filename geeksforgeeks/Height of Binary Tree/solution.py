'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/height-of-binary-tree/1
- Time Complexity: O(N) [N: number of nodes]
- Space Complexity: O(1)
'''

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def height(self, root: Node):
        if not root:
            return 0
        
        return max(self.height(root.left), self.height(root.right)) + 1