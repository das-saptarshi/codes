'''
- Link to Problem: https://www.geeksforgeeks.org/problems/binary-tree-to-cdll/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def bTreeToClist(self, root: Node) -> Node:
        head: Node = None
        prev: Node = None

        def solve(root: Node) -> None:
            nonlocal head, prev
            
            if not root:
                return
            
            solve(root.left)
            if not head:
                head = root
                
            if prev:
                prev.right = root
            
            root.left = prev
            prev = root
            solve(root.right)
        
        solve(root)
        head.left, prev.right = prev, head
        return head