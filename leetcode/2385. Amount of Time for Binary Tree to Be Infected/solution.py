'''
- Link to Problem: https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left:'TreeNode'=None, right:'TreeNode'=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root: return 0

        graph = defaultdict(list)

        def traverse(root: TreeNode):
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                traverse(root.left)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                traverse(root.right)

        traverse(root)

        queue = [start]
        visited = set([start])
        time = -1
        while queue:
            time += 1
            for _ in range(len(queue)):
                root = queue.pop(0)

                for node in graph[root]:
                    if node not in visited:
                        visited.add(node)
                        queue.append(node)
        
        return time
