'''
- Link to Problem: https://leetcode.com/problems/unique-paths/
- Time Complexity: O(m*n)
- Space Complexity: O(m*n)
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for _ in range(m)]
        dp[m-1][n-1] = 1

        def solve(r, c):
            if not (0 <= r < m and 0 <= c < n):
                return 0
            
            if dp[r][c] != -1:
                return dp[r][c]
            
            dp[r][c] = solve(r + 1, c) + solve(r, c + 1)
            return dp[r][c]
        
        return solve(0, 0)
        