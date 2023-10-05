'''
- Link to Problem: https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1
- Time Complexity: O(N)
- Space Complexity: O(N)
'''


class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None


def LeftView(root: Node):
    elems = []
    
    def solve(root: Node, index):
        if not root:
            return
        if len(elems) == index:
            elems.append(root.data)
        solve(root.left, index + 1)
        solve(root.right, index + 1)
    
    solve(root, 0)
    return elems