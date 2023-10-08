'''
- Link to Problem: https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/
- Time Complexity: O(R * C) [R: number of rows, C: number of cols]
- Space Complexity: O(R * C)
'''

from typing import List

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def solve(i, j, prev):
            if not (0 <= i < r and 0 <= j < c and grid[i][j] != -1 and grid[i][j] > prev):
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]

            num, grid[i][j] = grid[i][j], -1
            ans = 1
            for x, y in ((1,0), (-1,0), (0,1), (0,-1)):
                ans = (ans + solve(i + x, j + y, num)) % MOD
            dp[i][j] = ans
            grid[i][j] = num
            return dp[i][j]

        MOD = 10**9 + 7
        r, c = len(grid), len(grid[0])
        dp = [[-1]*c for _ in range(r)]
        ans = 0
        for i in range(r):
            for j in range(c):
                ans += solve(i, j, 0) % MOD
        
        return ans % MOD