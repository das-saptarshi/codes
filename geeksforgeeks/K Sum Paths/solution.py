'''
- Link to Problem: https://www.geeksforgeeks.org/problems/k-sum-paths/1
- Time Complexity: O(N)
- Space Complexity: O(LogN)
'''


from collections import defaultdict

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def sumK(self, root: Node, k: int) -> int:
        
        prev = defaultdict(int)
        
        def solve(root, total):
            if not root:
                return 0
            
            total += root.data
            ans = int(k == total) + prev[total - k]
            prev[total] += 1
            ans += solve(root.left, total) + solve(root.right, total)
            prev[total] -= 1
            return ans
        
        return solve(root, 0)