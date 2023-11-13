'''
- Link to Problem: https://www.geeksforgeeks.org/problems/shortest-common-supersequence0322/1
- Time Complexity: O(M * N)
- Space Complexity: O(M * N)
'''

class Solution:
    def shortestCommonSupersequence(self, X: str, Y: str, m: int, n: int) -> int:
        lcs = self.findLengthOfLCS(X, Y, m, n)
        return m + n - lcs
        
    def findLengthOfLCS(self, X: str, Y: str, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if X[i - 1] == Y[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]