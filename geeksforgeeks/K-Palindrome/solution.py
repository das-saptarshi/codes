'''
- Link to Problem: https://www.geeksforgeeks.org/problems/find-if-string-is-k-palindrome-or-not1923/1
- Time Complexity: O(N ^ 2)
- Space Complexity: O(N ^ 2)
'''

class Solution:
    def kPalindrome(self, s: str, n: int, k: int) -> int:
        
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif s[i - 1] == s[n - j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return 1  if n - dp[n][n] <= k else 0