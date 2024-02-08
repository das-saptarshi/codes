'''
- Link to Problem: https://www.geeksforgeeks.org/problems/leaf-at-same-level/1
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

class Node:
    def __init__(self, data: int, left: 'Node' = None, right: 'Node' = None) -> None:
        self.data = data
        self.left = left
        self.right = right

class Solution:
    def check(self, root: Node) -> bool:
        def solve(root: Node, level: int) -> bool:
            nonlocal lowestLevel
            
            if not root:
                return True
                
            if not (root.left or root.right):
                if lowestLevel == None:
                    lowestLevel = level
                    return True
                elif lowestLevel == level:
                    return True
                else:
                    return False
            
            return solve(root.left, level + 1) and solve(root.right, level + 1)
        
        lowestLevel = None
        return solve(root, 0)