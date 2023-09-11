'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/insert-a-node-in-a-bst/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def insert(self,root, Key):
        if not root:
            return Node(Key)
        
        if Key < root.data:
            root.left = self.insert(root.left, Key)
        if Key > root.data:
            root.right = self.insert(root.right, Key)
    
        return root