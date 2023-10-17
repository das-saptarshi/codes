'''
- Link to Problem: https://leetcode.com/problems/validate-binary-tree-nodes/
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from collections import defaultdict
from typing import List

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        children = defaultdict(list)
        hasParent = [False] * n

        for i in range(n):
            x, y = leftChild[i], rightChild[i]

            if x != -1:
                children[i].append(x)
                hasParent[x] = True

            if y != -1: 
                children[i].append(y)
                hasParent[y] = True
        
        seenAt = [-1] * n
        queue = [x for x in range(n) if not hasParent[x]]

        if len(queue) != 1: return False
        time = 0
        while queue:
            for _ in range(len(queue)):
                root = queue.pop(0)

                if seenAt[root] != -1 or len(children[root]) > 2:  return False
                seenAt[root] = time

                for child in children[root]:
                    queue.append(child)
        
        return all(time != -1 for time in seenAt)
