'''
- Link to Problem: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
- Time Complexity: O(R*C)
- Space Complexity: O(R*C)
'''

from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        def helper(r, c, prev):
            if not (0 <= r < rows and 0 <= c < cols and matrix[r][c] > prev):
                return 0

            if dp[r][c] != -1:
                return dp[r][c]
            
            prev = matrix[r][c]
            ans = 0
            for i, j in ((0,1), (0,-1), (1,0), (-1,0)):
                ans = max(ans, helper(r + i, c + j, prev))

            dp[r][c] = ans + 1
            return dp[r][c]
        
        ans = 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[-1]*cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                ans = max(ans, helper(r, c, -1))
        return ans