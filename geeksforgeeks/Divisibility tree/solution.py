'''
- Link to Problem: https://www.geeksforgeeks.org/problems/divisibility-tree1902/1
- Time Complexity: O(N)
- Space Complexity: O(N)
'''

from typing import List
from collections import defaultdict


class Solution:
    def minimumEdgeRemove(self, n : int, edges : List[List[int]]) -> int:
        tree = defaultdict(list)
        subtree_size = defaultdict(int)
        
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        def dfs(node, parent):
            size = 1
            
            for child in tree[node]:
                if child == parent: continue
                size += dfs(child, node)
            
            subtree_size[node] = size
            return size
        
        
        dfs(1, -1)
        
        return sum(1 for size in subtree_size.values() if size % 2 == 0) - 1