'''
- Link to Problem: https://leetcode.com/problems/find-mode-in-binary-search-tree/
- Time Complexity: O(N)
- Space Complexity: O(1)
'''

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        elements = []
        currentElement = float('-inf')
        freq = currentFreq = 0
        

        def solve(root: TreeNode):
            nonlocal elements, freq, currentElement, currentFreq
            if not root:
                return 
            
            solve(root.left)
            if currentElement == root.val:
                currentFreq += 1
            else:
                currentElement = root.val
                currentFreq = 1
            
            if currentFreq > freq:
                freq = currentFreq
                elements = [currentElement]
            elif currentFreq == freq:
                elements.append(currentElement)
            
            solve(root.right)
        
        solve(root)
        return elements